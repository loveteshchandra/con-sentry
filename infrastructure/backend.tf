# =============================================================================
# Terraform Backend Configuration
# =============================================================================
# Configure where Terraform stores its state file.
# =============================================================================

# -----------------------------------------------------------------------------
# Local Backend (Default for Development)
# -----------------------------------------------------------------------------
# Using local backend by default. State is stored on your local machine.
# This is fine for development but NOT recommended for team environments.

terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}

# -----------------------------------------------------------------------------
# TODO: Enable S3 Backend for Production
# -----------------------------------------------------------------------------
# For team environments and CI/CD, use S3 with DynamoDB for state locking.
# Uncomment and configure the block below, then remove the local backend above.
#
# Prerequisites:
# 1. Create an S3 bucket for state storage
# 2. Create a DynamoDB table for state locking (primary key: LockID)
# 3. Configure appropriate IAM permissions
#
# terraform {
#   backend "s3" {
#     bucket         = "your-terraform-state-bucket"
#     key            = "holier-than-prompt/terraform.tfstate"
#     region         = "us-east-1"
#     encrypt        = true
#     dynamodb_table = "terraform-state-lock"
#     
#     # TODO: Uncomment for cross-account deployments
#     # role_arn = "arn:aws:iam::ACCOUNT_ID:role/TerraformRole"
#   }
# }
# -----------------------------------------------------------------------------
