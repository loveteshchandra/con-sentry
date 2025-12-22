# =============================================================================
# Main Terraform Configuration
# =============================================================================
# This file contains the primary resource definitions for the project.
# =============================================================================

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "terraform"
    }
  }
}

# =============================================================================
# TODO: Add your infrastructure resources below
# =============================================================================
# 
# Examples of resources you might add:
#
# 1. VPC and Networking:
#    - aws_vpc
#    - aws_subnet
#    - aws_internet_gateway
#    - aws_route_table
#
# 2. Compute:
#    - aws_instance (EC2)
#    - aws_lambda_function
#    - aws_ecs_cluster / aws_ecs_service
#
# 3. Storage:
#    - aws_s3_bucket
#    - aws_dynamodb_table
#
# 4. API:
#    - aws_api_gateway_rest_api
#    - aws_apigatewayv2_api (HTTP API)
#
# =============================================================================

# Placeholder data source to validate AWS connectivity
# Remove this once you add actual resources
data "aws_caller_identity" "current" {}
