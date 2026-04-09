variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "image_url" {
  description = "Docker image URL (DockerHub or ECR)"
  type        = string
  default = "himandevo/simple-time-app_image:latest"

}