# AWS Infrastructure Architecture

## 1. Purpose

This document describes the planned AWS infrastructure for the Enterprise Platform Engineering project.

Infrastructure will be created with Terraform and reviewed before deployment.

## 2. Planned AWS Components

| Component | Purpose |
|---|---|
| VPC | Isolate project networking |
| Public subnet | Host resources that require public connectivity |
| Private subnet | Keep resources that should not be publicly accessible |
| Security groups | Control network traffic |
| IAM roles | Grant services only the permissions they require |
| EC2 | Run the application when needed |
| Amazon ECR | Store container images |
| Systems Manager | Support controlled instance management |
| S3 | Store selected artifacts and logs |
| KMS | Encrypt supported resources |
| CloudTrail | Record supported AWS API activity |
| CloudWatch | Collect supported logs and metrics |

## 3. Security Requirements

- Apply least-privilege IAM permissions.
- Do not expose private resources directly to the internet.
- Allow only necessary network traffic.
- Enable encryption for supported storage resources.
- Keep AWS credentials out of Git.
- Review Terraform plans before applying changes.
- Check existing AWS resources before creating new ones.

## 4. Cost Controls

- Avoid creating paid AWS resources until they are needed.
- Stop or remove resources when they are no longer required.
- Remember that stopping EC2 does not eliminate every possible charge.
- Check for billable resources such as storage, public IPv4 addresses, and NAT gateways.
- Verify the actual AWS bill after experiments.

## 5. Implementation Status

This document describes the intended design. Each component must be configured and tested before being marked as implemented.
