# 🚀 DevOps Assignment – Journey Documentation

## 📌 Objective

The goal of this project was to design and deploy a production-style containerized application on AWS using Infrastructure as Code (Terraform) and Docker.

---

## 🏗 Architecture Overview

- FastAPI backend
- Celery worker
- Redis (AWS ElastiCache)
- Nginx frontend
- EC2 instance (Docker host)
- Application Load Balancer
- CloudWatch logging
- IAM role-based authentication

All infrastructure was provisioned using Terraform.

---

## 🛠 Key Challenges & Solutions

### 1️⃣ Docker Compose Issues
- Initial build errors due to incorrect build context.
- Fixed Dockerfile COPY paths and ensured proper directory structure.

### 2️⃣ Redis Migration
- Initially used local Redis container.
- Migrated to AWS ElastiCache.
- Updated environment variables and secured Redis using security groups.

### 3️⃣ Security Hardening
- Restricted SSH to personal IP.
- Removed public Redis access.
- Used IAM role instead of static credentials.
- Followed least privilege principle.

### 4️⃣ Load Balancer Health Checks
- Target group showed unhealthy initially.
- Verified backend running on correct port.
- Adjusted health check path and security group rules.

---

## 🔐 Security Decisions

- SSH restricted to /32 IP
- Redis accessible only from EC2 security group
- IAM role attached to EC2 for CloudWatch
- Infrastructure fully codified in Terraform

---

## 📊 Observability

- CloudWatch log groups configured
- Docker container logs forwarded
- Enables centralized monitoring

---

## 💰 Cost Awareness

- Used Free Tier compatible services
- Deployed temporarily for screenshots
- Destroyed infrastructure after validation
- Practiced cost control discipline

---

## 🔮 Production Improvements (Future Scope)

If deploying in production, I would:

- Add Auto Scaling Group
- Use HTTPS with ACM certificate
- Enable Multi-AZ Redis
- Add WAF
- Add CI/CD pipeline (GitHub Actions)
- Add Infrastructure modules
- Implement Blue-Green deployment

---

## 🎯 What This Project Demonstrates

- Infrastructure as Code
- AWS networking fundamentals
- Secure architecture design
- Container orchestration basics
- Cloud cost discipline
- Production-style thinking

---

## 🧠 Key Learning

This project reinforced the importance of:

- Security first mindset
- Reproducible infrastructure
- Managed services over self-hosted
- Observability and logging
- Clean teardown practices

---

End of Journey Documentation.
