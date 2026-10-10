# Enterprise Platform Engineering

## Project Overview

Enterprise Platform Engineering is a hands-on project focused on building
automated, secure, and observable application delivery workflows.

The target design combines CI/CD automation, Infrastructure as Code,
container security, Kubernetes deployment, monitoring, and operational
documentation.

## Project Goals

- Automate application build and test workflows.
- Integrate security checks into CI/CD.
- Package applications with Docker.
- Publish container images to Amazon ECR.
- Manage AWS infrastructure with reusable Terraform modules.
- Practice Kubernetes deployment and health checks locally.
- Explore monitoring with Prometheus and Grafana.
- Document troubleshooting, rollback, and incident response.

## Planned Technology Stack

- AWS: EC2, ECR, IAM, Systems Manager, VPC, and S3
- Terraform: Infrastructure as Code
- Jenkins and GitHub Actions: CI/CD
- Docker: Containerization
- Gitleaks, Semgrep, and Trivy: Security scanning
- Minikube: Local Kubernetes learning environment
- Prometheus and Grafana: Monitoring and visualization
- Nexus Repository: Artifact management

## Architecture and Workflows

- [Platform Architecture](documentation/architecture/overview.md)
- [AWS Infrastructure](documentation/architecture/aws-infrastructure.md)
- [CI/CD Pipeline](documentation/workflows/cicd-pipeline.md)
- [Terraform Workflow](documentation/workflows/terraform-workflow.md)
- [Incident Response](documentation/workflows/incident-response.md)

## Implementation Status

This project is being developed in phases. Planned components will be
marked as implemented only after they have been configured and tested.

## Cost and Security

- Prefer local Kubernetes learning with Minikube over a paid EKS cluster.
- Review Terraform plans before creating or changing AWS resources.
- Use least-privilege IAM permissions.
- Never commit credentials, access keys, tokens, or Terraform state files.
- Verify security scans and application health before declaring a release successful.
