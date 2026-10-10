# Enterprise Platform Engineering — Architecture Overview

## 1. Purpose

This document describes the target architecture for the Enterprise Platform
Engineering project. Components will be marked as implemented only after
they have been configured and tested.

## 2. High-Level Architecture

```mermaid
flowchart TD
    DEV["Developer"]
    GH["GitHub Repository"]
    GA["GitHub Actions"]
    SEC["Security Checks<br/>Gitleaks and Semgrep"]
    JEN["Jenkins CI/CD"]
    BUILD["Build and Test"]
    DOCKER["Docker Image"]
    TRIVY["Trivy Image Scan"]
    ECR["Amazon ECR"]
    DEPLOY{"Choose Deployment Target"}
    EC2["AWS EC2 Deployment<br/>via Systems Manager"]
    K8S["Local Kubernetes<br/>via Minikube"]
    MON["Monitoring<br/>Prometheus and Grafana"]
    TF["Terraform Modules"]
    AWS["AWS Infrastructure"]
    NEXUS["Nexus Artifact Repository"]
    DOCS["Documentation and Runbooks"]

    DEV --> GH
    GH --> GA
    GA --> SEC
    SEC --> JEN
    JEN --> BUILD
    BUILD --> DOCKER
    DOCKER --> TRIVY
    TRIVY -->|Pass| ECR
    ECR --> DEPLOY
    DEPLOY --> EC2
    DEPLOY --> K8S
    EC2 --> MON
    K8S --> MON
    TF --> AWS
    AWS --> EC2
    NEXUS -. "Optional artifact storage" .-> BUILD
    DOCS -. "Operational guidance" .-> MON
## 3. Component Responsibilities

| Component | Responsibility |
|---|---|
| GitHub | Source control and collaboration |
| GitHub Actions | Automated validation and security workflows |
| Jenkins | Build, test, and deployment orchestration |
| Gitleaks | Detect exposed secrets |
| Semgrep | Analyze source code for security issues |
| Docker | Package the application |
| Trivy | Scan container images for vulnerabilities |
| Amazon ECR | Store versioned container images |
| Terraform | Manage infrastructure as code |
| AWS Systems Manager | Support controlled deployment to EC2 |
| Minikube | Local Kubernetes learning environment |
| Prometheus | Collect metrics |
| Grafana | Visualize metrics |
| Nexus | Store selected build artifacts |
| Runbooks | Document troubleshooting and recovery |

## 4. Security Principles

- Use least-privilege IAM permissions.
- Keep credentials out of source control.
- Require security checks to pass before publishing images.
- Use immutable image tags or image digests for releases.
- Review Terraform plans before applying infrastructure changes.
- Restrict network access to required ports and sources.
- Verify deployment health before declaring success.

## 5. Cost Considerations

- Use Minikube for initial Kubernetes experiments instead of paid EKS.
- Check existing AWS resources before reusing them.
- Avoid unnecessary NAT gateways and always-on infrastructure.
- Review AWS costs before creating resources.

## 6. Implementation Status

This is the target architecture. Individual integrations must be tested before
they are described as operational. GitHub Actions and Jenkins will have clearly
defined responsibilities to avoid duplicate publishing or conflicting deployments.
