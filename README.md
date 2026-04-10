# Overview

This repository contains a production-ready deployment of a containerized FastAPI microservice on AWS.  
The solution leverages ECS Fargate for serverless container orchestration, ensuring high availability and security while minimizing operational overhead.

---
## Repo Structure
```
.
├── app/
│   ├── app.py           
│   ├── requirements.txt  
│   └── Dockerfile       
└── Infrastruc/
    ├── main.tf          
    ├── variables.tf     
    ├── outputs.tf       
└── README.md        
```
---

## Architecture & Design Decisions
I prioritized low-complexity infrastructure and implemented security and health checks.

### 1. Compute: AWS ECS Fargate
- Chosen over EKS or GKE for simplicity.
- Ideal for a single microservice: reliability, scaling, and no Kubernetes control plane overhead.
- Faster "Time to Production" with enterprise-grade orchestration.

### 2. Networking
- **Public/Private Split**: Application runs in private subnets (not directly reachable from the internet).
- **ALB Ingress**: Application Load Balancer resides in public subnets, acting as the secure gateway.
- **Outbound Traffic**: NAT Gateway allows ECS tasks to pull images/updates securely from Docker Hub.

### 3. Security
- **Security Group Chaining**: ECS tasks only accept traffic from the ALB security group on port 8080.
- **Egress Control**: Outbound rules limited to necessary data pulling.

### 4. Infrastructure as Code (IaC)
- Uses the official AWS VPC Terraform Module.
- Organized into logical blocks (Networking, IAM, ECS, Load Balancing) for clarity.

---

## Prerequisites
- Terraform (>= 1.5.0)  
- AWS CLI configured with appropriate permissions  
- Docker (if building the image locally)  

## Authentication
Export your AWS credentials to your terminal session:

## Authentication
Export your AWS credentials to your terminal session:

```powershell
$env:AWS_ACCESS_KEY_ID="your_access_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret_key"
```

## Deployment

Navigate to the infrastructure directory and initialize the stack:

```Powershell/Vscode terminal

cd Infrastruc/
terraform init
terraform plan
terraform apply
```
**Once resources are deployed, you will be given a URL.**
**Paste it into your browser to access the app.**
**Note: Please wait at least 1–2 minutes after receiving the URL. The ALB needs time to complete health checks before routing requests.**

---

## Cleanup
To avoid unnecessary AWS costs, destroy the infrastructure after review: Run
```
terraform destroy
```