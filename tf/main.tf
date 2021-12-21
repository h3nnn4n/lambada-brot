terraform {
  backend "s3" {
    bucket = "h3nnn4n-terraform-state"
    key    = "lambada-brot/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = "us-east-1"
}
