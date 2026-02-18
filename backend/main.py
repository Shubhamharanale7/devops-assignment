from fastapi import FastAPI
from celery.result import AsyncResult
from worker import write_log_celery
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/notify/")
async def notify_user(email: str):
    """Endpoint that triggers the background task in Celery."""
    task = write_log_celery.delay(f"Notification sent to {email}")
    # task is a AsyncResult, a promise to a result that will be available later.
    return {"message": f"Email will be sent to {email}", "task_id": task.id}


@app.get("/task_status/{task_id}")
async def get_task_status(task_id: str):
    """Endpoint to check the status of the task."""
    task_result = AsyncResult(task_id)  # Get the task result using the task ID
    if task_result.ready():  # If the task is done
        return {"task_id": task_id, "status": "completed", "result": task_result.result}
    elif task_result.failed():  # If the task failed
        return {"task_id": task_id, "status": "failed"}
    else:  # If the task is still in progress
        return {"task_id": task_id, "status": "in progress"}

@app.post("/health/")
async def health():
    """Endpoint that checks the health of the application."""
    return {"message": "OK"}