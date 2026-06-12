# Complete CI/CD Pipeline Deployed on Amazon EKS

## Overview

This project demonstrates a complete end-to-end CI/CD pipeline for a Python Flask application using modern DevSecOps practices. The pipeline automates code validation, quality analysis, security scanning, containerization, image management, and Kubernetes deployment on Amazon EKS.

### Key Features

* Automated CI/CD with GitHub Actions
* Unit Testing using Pytest
* Static Code Analysis with SonarQube
* Docker Image Build and Packaging
* Container Vulnerability Scanning using Trivy
* Image Storage in Amazon ECR
* Kubernetes Deployment on Amazon EKS
* Helm-Based Release Management
* LoadBalancer Service Exposure
* Rollback and Version Management
* Environment-Specific Configuration Support

---

## Architecture

```text
┌─────────────┐
│  Developer  │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ GitHub Repository   │
└─────────┬───────────┘
          │
          ▼
┌───────────────────────────────┐
│ GitHub Actions CI/CD Pipeline │
├───────────────────────────────┤
│ • Code Checkout               │
│ • Unit Testing                │
│ • SonarQube Analysis          │
│ • Docker Build                │
│ • Trivy Security Scan         │
│ • Push Image to Amazon ECR    │
│ • Helm Deployment             │
└───────────────┬───────────────┘
                │
                ▼
┌─────────────────────┐
│     Amazon EKS      │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ LoadBalancer Service│
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Flask Application   │
└─────────────────────┘
```

---

## Technology Stack

| Category            | Technology     |
| ------------------- | -------------- |
| Source Control      | GitHub         |
| CI/CD               | GitHub Actions |
| Application         | Python Flask   |
| Testing             | Pytest         |
| Code Quality        | SonarQube      |
| Containerization    | Docker         |
| Security Scanning   | Trivy          |
| Container Registry  | Amazon ECR     |
| Kubernetes Platform | Amazon EKS     |
| Package Management  | Helm           |
| Cloud Provider      | AWS            |

---

## CI/CD Workflow

### 1. Source Code Commit

Developers push code changes to GitHub.

### 2. Automated Testing

Pytest executes unit tests to validate application functionality.

### 3. Code Quality Analysis

SonarQube performs:

* Static Code Analysis
* Security Checks
* Code Smell Detection
* Maintainability Review

### 4. Container Build

Docker creates a deployable application image.

### 5. Security Scan

Trivy scans the Docker image for:

* Critical Vulnerabilities
* High Severity Issues
* Dependency Risks

### 6. Push to Amazon ECR

The validated image is pushed to Amazon Elastic Container Registry.

### 7. Deployment to Amazon EKS

Helm deploys the latest application version to the Kubernetes cluster.

### 8. Application Exposure

A Kubernetes LoadBalancer Service exposes the application externally.

---

## Project Structure

```text
complete-cicd-pipeline-eks
│
├── .github/
│   └── workflows/
│       └── cicd.yml
│
├── app/
│   ├── app.py
│   ├── test_app.py
│   ├── requirements.txt
│   ├── templates/
│   └── static/
│
├── helm/
│   └── myapp/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           └── service.yaml
│
├── Dockerfile
├── sonar-project.properties
└── README.md
```

---

## Deployment Command

```bash
helm upgrade --install myapp ./helm/myapp
```

---

## Verification Commands

### Check Pods

```bash
kubectl get pods
```

### Check Services

```bash
kubectl get svc
```

### Check Deployments

```bash
kubectl get deployment
```

### Check Helm Releases

```bash
helm list
```

---

## Rollback Deployment

View release history:

```bash
helm history myapp
```

Rollback to a previous version:

```bash
helm rollback myapp 1
```

---

## Deliverables

* ✅ GitHub Actions CI/CD Pipeline
* ✅ Pytest Unit Testing
* ✅ SonarQube Code Analysis
* ✅ Docker Image Build
* ✅ Trivy Vulnerability Scanning
* ✅ Amazon ECR Integration
* ✅ Amazon EKS Deployment
* ✅ Helm Release Management
* ✅ LoadBalancer Exposure
* ✅ Rollback Capability
* ✅ DevSecOps Best Practices

---

## Outcome

This project demonstrates a production-style DevSecOps workflow where every code change is automatically tested, scanned, containerized, and deployed to Amazon EKS through a fully automated CI/CD pipeline.
