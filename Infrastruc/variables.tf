variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "image_url" {
  description = "Docker image URL (DockerHub or ECR)"
  type        = string
}