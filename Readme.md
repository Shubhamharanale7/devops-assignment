🚀 DevOps Assignment – Production-Grade AWS Deployment
📌 Overview

This project demonstrates a production-style cloud-native deployment of a containerized application on AWS using Infrastructure as Code and DevOps best practices.

The solution includes:
Dockerized microservices
AWS EC2 compute layer
Amazon ElastiCache (Redis)
Application Load Balancer (ALB)
CloudWatch logging & monitoring
IAM role-based security
Terraform-based infrastructure provisioning

This implementation focuses on:
Security
Scalability
Observability
Infrastructure automation
Clean teardown lifecycle

🏗 Architecture Overview
🔷 High-Level Architecture
                ┌──────────────────────────┐
                │        End User          │
                │     (Browser / API)      │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │ Application Load Balancer│
                │   (HTTP / HTTPS ready)   │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │        EC2 Instance      │
                │     Docker Containers    │
                │                          │
                │  - Backend (FastAPI)     │
                │  - Worker (Celery)       │
                │  - Frontend (Nginx)      │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │  Amazon ElastiCache      │
                │        Redis             │
                └──────────────────────────┘

                EC2 → CloudWatch Logs



🧩 System Components
1️⃣ Application Load Balancer (ALB)
Distributes incoming traffic
Performs health checks
Routes traffic to EC2 target group
Designed for HTTPS (TLS termination ready)
Production-ready entry layer



2️⃣ EC2 Instance
Hosts containerized services:
FastAPI backend
Celery worker
Nginx frontend



Features:
IAM role attached (no static credentials)
CloudWatch logging enabled
Security group hardened
Managed via Terraform



3️⃣ Amazon ElastiCache (Redis)
Managed Redis service
Used as:
Celery message broker
Caching layer
Deployed inside VPC
Not publicly accessible
Security group allows access only from EC2


4️⃣ CloudWatch
Centralized logging
Application logs streamed securely
IAM-based access control
Enables operational visibility



5️⃣ Terraform (Infrastructure as Code)
Provisioned resources:
Default VPC & Subnets



Security Groups
IAM Role & Instance Profile
EC2 Instance
ElastiCache Cluster
Application Load Balancer



Target Group & Listener
Deployment:
terraform init
terraform apply
terraform destroy
Infrastructure is reproducible and disposable.



🔒 Security Implementation
This deployment follows industry best practices.
SSH Hardening
Port 22 restricted to a single trusted IP address
No public SSH exposure
Redis Isolation
Redis not publicly accessible
Access allowed only via EC2 security group reference
IAM Best Practices
No hardcoded AWS credentials
EC2 uses IAM role for CloudWatch access
Principle of least privilege followed
Network Security
Controlled inbound rules
Outbound traffic restricted appropriately
Internal service communication secured



🔐 HTTPS & TLS (Production Design)
In a real production deployment:
AWS Certificate Manager (ACM) issues SSL certificate
ALB listens on:
Port 80 (redirect to HTTPS)
Port 443 (TLS termination)
Encrypted traffic from user to ALB
Backend communication remains internal
Traffic Flow:

User (HTTPS)
    ↓
ALB (TLS Termination)
    ↓
EC2 Backend (HTTP internal)




Benefits:
Encrypted client communication
Centralized certificate management
Industry-standard load balancing



📊 Observability & Monitoring
ALB health checks
Target group monitoring
Redis cluster health monitoring
CloudWatch centralized logging
IAM-integrated logging pipeline
This ensures visibility across application and infrastructure layers.



📦 Containerization
Application services are containerized using Docker:
docker-compose up -d --build
Services include:
Backend (FastAPI)
Worker (Celery)
Frontend (Nginx)
Architecture is stateless and horizontally scalable.



📸 Deployment Screenshots
1️⃣ EC2 Running Instance
Instance state: Running
Public IP visible
IAM role attached



2️⃣ Amazon ElastiCache – Redis
Cluster ID: devops-redis
Engine: Redis
Node type: cache.t3.micro
Status: Available
Primary endpoint visible



3️⃣ Application Load Balancer
Type: Application
Status: Active
DNS name visible



4️⃣ Target Group Health
EC2 instance registered
Port 8000
Health check configuration visible



5️⃣ CloudWatch Logs
Log group created
Log streams active
Application logs visible



6️⃣ Security Groups
SSH restricted
Redis secured
Backend port controlled



📈 Scalability Design
This architecture supports horizontal scaling.



Future improvements:
Attach EC2 to Auto Scaling Group
Multi-AZ deployment
Redis replication group
WAF integration
Route53 domain integration
CI/CD pipeline for automated Terraform deployment
S3 backend for Terraform state locking



🧠 Engineering Decisions
Decision	Reason
ElastiCache over self-hosted Redis	Managed, scalable, production-ready
ALB over direct EC2 exposure	Industry-standard traffic routing
IAM role usage	Secure credential management
Terraform	Reproducible infrastructure
Dockerized services	Portability & consistency



⚙️ How to Reproduce
Clone repository
Configure AWS credentials
Update terraform.tfvars



Run:
terraform init
terraform apply
Deploy application on EC2
Access ALB DNS endpoint



🧹 Cleanup
To avoid AWS charges:
terraform destroy



🛠 Challenges Faced & Solutions
Docker Socket Permission Issue
Resolved by adding EC2 user to docker group and restarting session.
ACM Validation Timeout
Understood requirement for DNS validation and production domain ownership.
Target Group Health Check Failures
Resolved by verifying backend port exposure and security group configuration.
Security Group Duplication Errors
Refactored Terraform configuration to remove duplicate resources.



🎯 What This Demonstrates
Infrastructure as Code expertise
Secure AWS networking
Managed services integration
Container orchestration
Observability implementation
Production deployment mindset
Clean resource lifecycle management



👨‍💻 Author
Shubham Haranale
DevOps | Cloud | Infrastructure Automation

🏁 Final Result

This implementation reflects real-world DevOps engineering principles and demonstrates the ability to design, deploy, secure, and manage cloud-native infrastructure in AWS using automation and best practices.
