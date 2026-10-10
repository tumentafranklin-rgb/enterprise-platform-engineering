# Terraform Workflow

## 1. Purpose

This document describes how Terraform will be used to provision and manage
infrastructure for the Enterprise Platform Engineering project.

## 2. Workflow Stages

### Stage 1: Initialize

Run:

    terraform init

This downloads the required Terraform providers and initializes the working directory.

### Stage 2: Format

Run:

    terraform fmt -recursive

This formats Terraform configuration files consistently.

### Stage 3: Validate

Run:

    terraform validate

This checks whether the Terraform configuration is syntactically valid.

### Stage 4: Review Changes

Run:

    terraform plan

Review the proposed changes before applying them. Confirm which resources
will be created, changed, or destroyed.

### Stage 5: Apply Changes

Run:

    terraform apply

Apply changes only after reviewing the plan and confirming the intended
infrastructure changes.

### Stage 6: Verify

Use the appropriate AWS CLI commands and AWS console pages to verify that
the intended resources were created and configured correctly.

### Stage 7: Clean Up

When the environment is no longer needed, review the resources and their
dependencies before considering:

    terraform destroy

**Warning:** `terraform destroy` can delete infrastructure and cause data loss.
Never run it without reviewing what will be removed.

## 3. Security Practices

- Never commit AWS access keys or secret credentials.
- Use least-privilege IAM permissions.
- Protect Terraform state because it may contain sensitive information.
- Keep Terraform state files and local secret files out of Git.
- Review plans before applying infrastructure changes.
- Avoid making manual changes that cause Terraform state drift.
- Use separate environments when appropriate.

## 4. Cost Controls

- Prefer local testing when possible.
- Review planned resources for potential AWS charges.
- Avoid unnecessary NAT gateways and always-on resources.
- Verify that resources are removed when they are no longer needed.
- Check the AWS billing console after experiments.

## 5. Implementation Status

This document describes the intended Terraform workflow. Infrastructure
must be implemented and tested before being marked as operational.
