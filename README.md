🚀 Enterprise CI/CD Pipeline
Project Overview

This project implements an Enterprise CI/CD Pipeline using:

GitHub Actions
SonarQube
Pytest
Docker
Trivy
AWS ECR
Amazon EKS
Helm

The pipeline automatically builds, tests, scans, containerizes, and deploys a Python Flask application to Kubernetes whenever code is pushed to GitHub.

Architecture

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

Technologies Used
Tool	Purpose
Python Flask	Application
GitHub	Source Control
GitHub Actions	CI/CD Automation
SonarQube	Code Quality Analysis
Pytest	Unit Testing
Docker	Containerization
Trivy	Security Scanning
AWS ECR	Image Registry
Amazon EKS	Kubernetes Platform
Helm	Kubernetes Package Manager
Project Structure
enterprise-cicd-pipeline
│
├── .github/workflows/
│   └── cicd.yml
│
├── app/
│   ├── app.py
│   ├── test_app.py
│   ├── requirements.txt
│   ├── templates/
│   └── static/
│
├── helm/myapp/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       └── service.yaml
│
├── Dockerfile
├── sonar-project.properties
└── README.md
CI/CD Pipeline Flow
1. Code Commit

Developer pushes code to GitHub.

git add .
git commit -m "Updated application"
git push origin main
2. Unit Testing

GitHub Actions executes:

pytest app/test_app.py

Validates application functionality before deployment.

3. SonarQube Scan

Performs:

Code Quality Analysis
Security Analysis
Code Smell Detection
4. Docker Build

Creates Docker image:

docker build -t enterprise-cicd-app .
5. Trivy Security Scan

Scans Docker image for:

Critical Vulnerabilities
High Vulnerabilities
Dependency Issues
6. Push Image to ECR

Pushes image to Amazon ECR.

Example:

449499558261.dkr.ecr.us-east-1.amazonaws.com/enterprise-cicd-app
7. Deploy to Amazon EKS

Helm deploys application:

helm upgrade --install myapp ./helm/myapp

Creates:

Deployment
Pods
Service
8. Load Balancer Access

Application becomes available through AWS Load Balancer.

kubectl get svc
Helm Components
Chart.yaml

Defines Helm chart metadata.

values.yaml

Stores configurable values:

replicaCount: 2
containerPort: 5000
deployment.yaml

Creates Kubernetes Deployment.

Responsible for:

Pods
Replicas
Rolling Updates
service.yaml

Creates Kubernetes Service.

Type:

LoadBalancer

Provides external access.

Rollback Capability

View deployment history:

helm history myapp

Rollback:

helm rollback myapp 1
Environment Configuration

Environment values are passed during deployment.

Example:

ENVIRONMENT=Production
APP_VERSION=<Git Commit ID>
DEPLOY_TIME=<Deployment Timestamp>

Displayed on application UI.

Verification Commands

Check Pods:

kubectl get pods

Check Services:

kubectl get svc

Check Deployment:

kubectl get deployment

Check Helm Releases:

helm list
Project Deliverables

✅ GitHub Actions CI/CD Pipeline

✅ SonarQube Integration

✅ Trivy Security Scan

✅ Docker Image Creation

✅ AWS ECR Integration

✅ Amazon EKS Deployment

✅ Helm-Based Deployment

✅ Environment-Specific Configuration

✅ Rollback Capability

✅ Automated Smoke Test