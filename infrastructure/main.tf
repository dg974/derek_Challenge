terraform {
    required_providers {
        aws = {
            version = "~> 3.0"
        }
    }
}

provider "aws" {
  region = "us-east-1"
}