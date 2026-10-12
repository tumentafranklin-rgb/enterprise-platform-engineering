# Enterprise Platform Engineering Architecture

This diagram shows the application's development workflow, security checks, containerization, and Kubernetes deployment.

## Architecture Diagram

```mermaid
flowchart TD
    A["Developer"] --> B["GitHub Repository"]
    B --> C["GitHub Actions CI Pipeline"]

    subgraph Security["Continuous Integration and Security"]
        C --> D["Python Unit Tests"]
        C --> E["Gitleaks Secret Scanning"]
        C --> F["Semgrep Code Scanning"]
        C --> G["Docker Image Build"]
        G --> H["Trivy Vulnerability Scanning"]
    end

    subgraph Local["Local Deployment"]
        I["Docker Image v1.1"] --> J["Minikube Kubernetes Cluster"]
        J --> K["Kubernetes Deployment"]
        K --> L["API Pod 1"]
        K --> M["API Pod 2"]
        L --> N["Kubernetes Service"]
        M --> N
        N --> O["Application Port 8000"]
    end

    A --> I

    subgraph Future["Planned Cloud Infrastructure"]
        P["Terraform"] -.-> Q["AWS Infrastructure"]
        Q -.-> R["Amazon ECR"]
        R -.-> S["AWS Deployment"]
    end

    subgraph Monitoring["Planned Monitoring"]
        T["Prometheus"] -.-> U["Grafana Dashboard"]
    end
```

## Implemented Tools

- **Git and GitHub:** Source control and code hosting.
- **GitHub Actions:** Automated CI workflow.
- **Python:** Application and unit tests.
- **Gitleaks:** Secret scanning.
- **Semgrep:** Source-code security scanning.
- **Docker:** Container image building.
- **Trivy:** Container vulnerability scanning.
- **Kubernetes and Minikube:** Local container orchestration.

## Planned Tools

- **Terraform:** Infrastructure as code.
- **AWS:** Cloud infrastructure.
- **Amazon ECR:** Container image registry.
- **Prometheus:** Metrics collection.
- **Grafana:** Monitoring dashboards.

## Important Notes

The solid lines show the implemented development and local deployment components. The dashed lines represent planned cloud infrastructure and monitoring work.

The CI workflow runs automated checks, but it does not currently deploy the application automatically to AWS or Minikube.

The Mermaid diagram is rendered by supported Markdown viewers, including GitHub. It is not an automatically updating infrastructure monitoring dashboard.
