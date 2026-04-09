# particle41Devops
particle41Devops Challange assessment

# DevOps Challenge – Python App + Terraform Infrastructure

## Overview
This project contains:
- A simple Python web application (`app/app.py`) served with **FastAPI** and **Uvicorn**.
- A Dockerfile to containerize the app.
- Terraform configuration (`Infrastruc/`) to provision AWS infrastructure:
  - VPC, subnets, security groups
  - ECS cluster and service
  - Application Load Balancer (ALB)

The goal is to deploy the Python app on AWS ECS Fargate behind an ALB.

---

## Project Structure
Repo/ 
 ├── app/ 
 │   ├── app.py 
 │   ├── requirements.txt 
 │   └── Dockerfile 
└── Infrastruc/ 
 ├── main.tf  
 ├── variables.tf 
 ├── outputs.tf 
 └── terraform.lock.hcl
 

---

## Prerequisites
- **AWS account** with permissions to create ECS, ALB, VPC, IAM.
- **Terraform >= 1.5.0**
- **Docker** (to build and push images to DockerHub)

---

## AWS Credentials
This setup uses environment variables for AWS authentication.  
Export your keys before running Terraform:

```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key

## Variables
The Default Region is ap-south-1

for the imageurl you can either use my public dockerhub repo which is aslo in the default variable or create your own image from the dockerfile provided in the app folder.

