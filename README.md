# 🚀 Enterprise CI/CD Pipeline

## Project Overview

This project implements an **Enterprise CI/CD Pipeline** using:

* GitHub Actions
* SonarQube
* Pytest
* Docker
* Trivy
* AWS ECR
* Amazon EKS
* Helm

The pipeline automatically builds, tests, scans, containerizes, and deploys a Python Flask application to Kubernetes whenever code is pushed to GitHub.

---

# Architecture

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
│    Application      │
└─────────────────────┘
```

---

# Technologies Used

| Tool           | Purpose                    |
| -------------- | -------------------------- |
| Python Flask   | Application Development    |
| GitHub         | Source Control             |
| GitHub Actions | CI/CD Automation           |
| SonarQube      | Code Quality Analysis      |
| Pytest         | Unit Testing               |
| Docker         | Containerization           |
| Trivy          | Security Scanning          |
| AWS ECR        | Image Registry             |
| Amazon EKS     | Kubernetes Platform        |
| Helm           | Kubernetes Package Manager |

---

# Project Structure

```text
enterprise-cicd-pipeline
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

# CI/CD Pipeline Flow

## 1. Code Commit

Developer pushes code to GitHub.

```bash
git add .
git commit -m "Updated application"
git push origin main
```

---

## 2. Unit Testing

GitHub Actions executes:

```bash
pytest app/test_app.py
```

Validates application functionality before deployment.

---

## 3. SonarQube Scan

Performs:

* Code Quality Analysis
* Security Analysis
* Code Smell Detection

---

## 4. Docker Build

Creates Docker image:

```bash
docker build -t enterprise-cicd-app .
```

---

## 5. Trivy Security Scan

Scans Docker image for:

* Critical Vulnerabilities
* High Vulnerabilities
* Dependency Issues

---

## 6. Push Image to ECR

Pushes image to Amazon ECR.

Example:

```text
449499558261.dkr.ecr.us-east-1.amazonaws.com/enterprise-cicd-app
```

---

## 7. Deploy to Amazon EKS

Helm deploys the application:

```bash
helm upgrade --install myapp ./helm/myapp
```

Creates:

* Deployment
* Pods
* Service

---

## 8. Load Balancer Access

Application becomes available through AWS Load Balancer.

```bash
kubectl get svc
```

---

# Helm Components

## Chart.yaml

Defines Helm chart metadata.

## values.yaml

Stores configurable values:

```yaml
replicaCount: 2

image:
  repository: enterprise-cicd-app
  tag: latest

containerPort: 5000
```

## deployment.yaml

Creates Kubernetes Deployment.

Responsible for:

* Pods
* Replicas
* Rolling Updates

## service.yaml

Creates Kubernetes Service.

```yaml
type: LoadBalancer
```

Provides external access to the application.

---

# Rollback Capability

View deployment history:

```bash
helm history myapp
```

Rollback to a previous release:

```bash
helm rollback myapp 1
```

---

# Environment Configuration

Environment values are passed during deployment.

Example:

```text
ENVIRONMENT=Production
APP_VERSION=1.0.0
DEPLOY_TIME=2026-06-12
```

Displayed on the application UI.

---

# Verification Commands

### Check Pods

```bash
kubectl get pods
```

### Check Services

```bash
kubectl get svc
```

### Check Deployment

```bash
kubectl get deployment
```

### Check Helm Releases

```bash
helm list
```

---

# Project Deliverables

* ✅ GitHub Actions CI/CD Pipeline
* ✅ SonarQube Integration
* ✅ Trivy Security Scan
* ✅ Docker Image Creation
* ✅ AWS ECR Integration
* ✅ Amazon EKS Deployment
* ✅ Helm-Based Deployment
* ✅ Environment-Specific Configuration
* ✅ Rollback Capability
* ✅ Automated Smoke Test

---

# Author

Enterprise CI/CD Pipeline using GitHub Actions, Docker, SonarQube, Trivy, AWS ECR, Amazon EKS, and Helm.
