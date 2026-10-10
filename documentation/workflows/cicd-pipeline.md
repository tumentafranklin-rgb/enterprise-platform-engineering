# CI/CD Pipeline Workflow

## 1. Purpose

This document describes the planned Continuous Integration and Continuous
Delivery workflow for the Enterprise Platform Engineering project.

The pipeline will automate application testing, security scanning, image
building, and deployment validation.

## 2. Pipeline Stages

1. **Source Control**
   - Developers push changes to GitHub.
   - Changes are reviewed before merging into the main branch.

2. **Automated Validation**
   - GitHub Actions runs automated checks.
   - The pipeline checks the application code and project configuration.

3. **Security Scanning**
   - Gitleaks checks for exposed secrets.
   - Semgrep checks source code for security issues.
   - Trivy scans container images for known vulnerabilities.

4. **Build and Test**
   - Build the application.
   - Run automated tests.
   - Build a Docker image only after the required checks pass.

5. **Image Publishing**
   - Authenticate securely to Amazon ECR.
   - Publish the approved image using an identifiable tag.
   - Avoid embedding credentials in the image.

6. **Deployment**
   - Deploy to the selected environment using an approved workflow.
   - Use AWS Systems Manager for supported EC2 deployment operations.
   - Use Minikube for local Kubernetes deployment practice.

7. **Health Verification**
   - Check whether the application starts successfully.
   - Verify its health endpoint or expected response.
   - Review logs if the deployment fails.

## 3. Tool Responsibilities

| Tool | Responsibility |
|---|---|
| GitHub | Source control |
| GitHub Actions | Automated validation and security workflows |
| Jenkins | Build and deployment orchestration |
| Gitleaks | Secret detection |
| Semgrep | Source-code security analysis |
| Docker | Container image creation |
| Trivy | Container vulnerability scanning |
| Amazon ECR | Container image storage |
| AWS Systems Manager | Supported EC2 management and deployment |
| Minikube | Local Kubernetes practice |

GitHub Actions and Jenkins must have clearly defined responsibilities.
Avoid configuring both systems to publish or deploy the same release
without coordination.

## 4. Failure Handling

- Stop the pipeline when a required security check fails.
- Do not publish an image that has failed a required validation stage.
- Preserve useful logs for troubleshooting.
- Investigate the cause before retrying a failed deployment.
- Verify application health after recovery.

## 5. Rollback Strategy

- Retain previously approved image versions.
- Identify the last known-good release.
- Redeploy that version using the approved deployment process when necessary.
- Verify application health after rollback.
- Document the cause and corrective action.

## 6. Implementation Status

This document describes the planned workflow. Each stage must be configured
and tested before being described as operational.
