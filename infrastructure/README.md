# Infrastructure

Terraform configuration for AWS infrastructure.

## Prerequisites

- [Terraform](https://www.terraform.io/downloads) >= 1.0 (or use [tfenv](https://github.com/tfutils/tfenv))
- AWS CLI configured with appropriate credentials
- AWS account access

## Quick Start

```bash
# Initialize Terraform
terraform init

# Validate configuration
terraform validate

# Preview changes
terraform plan

# Apply changes (when ready)
terraform apply
```

## Structure

| File | Description |
|------|-------------|
| `main.tf` | AWS provider and resource definitions |
| `variables.tf` | Input variable definitions |
| `outputs.tf` | Output value definitions |
| `backend.tf` | State storage configuration |
| `versions.tf` | Terraform and provider version constraints |

## Configuration

Set variables via `terraform.tfvars` or environment variables:

```hcl
# terraform.tfvars
aws_region   = "us-west-2"
environment  = "staging"
project_name = "holier-than-prompt"
```

Or via CLI:

```bash
terraform plan -var="environment=prod"
```

## TODO

- [ ] Configure S3 backend for remote state (see `backend.tf`)
- [ ] Add actual infrastructure resources
- [ ] Set up environment-specific `.tfvars` files
- [ ] Configure CI/CD deployment pipeline
