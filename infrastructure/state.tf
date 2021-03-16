# FYI, typically I use s3 backend with dynamodb locking

terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}