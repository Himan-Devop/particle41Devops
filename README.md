Overview
This repository contains a production-ready deployment of a containerized FastAPI microservice on AWS. 
The solution leverages ECS Fargate for serverless container orchestration, ensuring high availability and security while minimizing operational overhead.

## Architecture & Design Decisions
I prioritized low complexity infra and implemented the security and health checks on it.

1. Compute: AWS ECS Fargate
I chose ECS Fargate over EKS or GKE.For a single microservice, Fargate provides the necessary reliability and scaling without the management overhead of a Kubernetes control plane.
It allows for a faster "Time to Production" while still providing enterprise-grade container orchestration.

2. Networking: 
Public/Private Split: Following best practices, the application lives in private subnets. It is not reachable from the public internet.

ALB Ingress: The Application Load Balancer is the only component in the public subnets, serving as the secure gateway to the application.

Outbound Traffic: A NAT Gateway is provisioned to allow private ECS tasks to securely pull updates and images from Docker Hub without exposing the instances.

3. Security:
Security Group Chaining: The ECS tasks are protected by a security group that only accepts traffic from the ALB's security group on port 8080.

Egress Control: Outbound rules are only there for the necessary data pulling for the app.

4. Infrastructure as Code (IaC)

The code utilizes the official AWS VPC Terraform Module.
While kept in a single main.tf for ease of review and debugging, the code is organized into distinct logical blocks (Networking, IAM, ECS, and Load Balancing)

.
├── app/
│   ├── app.py           
│   ├── requirements.txt  
│   └── Dockerfile       
└── Infrastruc/
    ├── main.tf          
    ├── variables.tf     
    ├── outputs.tf       
|----Readme     
## Prerequisites

Terraform(>= 1.5.0) 

AWS CLI configured with appropriate permissions given to the User.

Docker (if building the image locally).

1. Authentication
Export your AWS credentials to your terminal session:

$env:AWS_ACCESS_KEY_ID="your_access_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret_key"

2. Deployment
Navigate to the infrastructure directory and initialize the stack:


cd Infrastruc/
terraform init
terraform plan
terraform apply

Once The resources are deployed you will be given a URL which you can paste at the browser and access the app.
Note - please wait for atleast 1-2 minutes once you get the Url since it take some time for the ALB to complete health checks and redirect requests.

## Cleanup
To avoid unnecessary AWS costs, please destroy the infrastructure after the review:

terraform destroy