# =============================================================================
# Terraform Outputs
# =============================================================================
# Define outputs for resources created by this configuration.
# These can be used by other Terraform configurations or CI/CD pipelines.
# =============================================================================

output "aws_account_id" {
  description = "AWS Account ID where resources are deployed"
  value       = data.aws_caller_identity.current.account_id
}

output "environment" {
  description = "Current deployment environment"
  value       = var.environment
}

# TODO: Add outputs for your infrastructure resources
# Examples:
#
# output "vpc_id" {
#   description = "ID of the VPC"
#   value       = aws_vpc.main.id
# }
#
# output "api_endpoint" {
#   description = "API Gateway endpoint URL"
#   value       = aws_apigatewayv2_api.main.api_endpoint
# }
#
# output "s3_bucket_name" {
#   description = "Name of the S3 bucket"
#   value       = aws_s3_bucket.main.id
# }
