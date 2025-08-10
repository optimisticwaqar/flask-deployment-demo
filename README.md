# Flask Deployment Demo

![Build and Deploy](https://github.com/optimisticwaqar/flask-deployment-demo/workflows/Build%20and%20Deploy/badge.svg)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)

A demonstration of automated Docker deployment with GitHub Actions, environments, and approval workflows.

## Features

- 🚀 **Automated Deployment**: Push to main triggers staging deployment
- 🔒 **Environment Protection**: Production requires manual approval
- 🐳 **Docker**: Containerized application with multi-platform builds
- 🔄 **Rollback**: Manual rollback workflow for quick recovery
- 📊 **Monitoring**: Health checks and deployment status
- 🌍 **Multi-Environment**: Staging and Production environments

## Environments

- **Staging**: Auto-deployed on main branch push
- **Production**: Requires manual approval after staging success

## Docker Repository

- **DockerHub**: [waqar8593/flask-deployment-demo](https://hub.docker.com/r/YOUR_DOCKERHUB_USERNAME/flask-deployment-demo)

## Manual Deployment

To deploy manually:
1. Go to **Actions** tab
2. Select **Build and Deploy** workflow
3. Click **Run workflow**
4. Choose environment and options
5. Click **Run workflow**

## Rollback

To rollback a deployment:
1. Go to **Actions** tab
2. Select **Rollback Deployment** workflow
3. Click **Run workflow**
4. Choose environment and previous version
5. Click **Run workflow**

## Local Development

```bash
# Run locally
pip install -r requirements.txt
python app.py

# Run with Docker
docker build -t flask-demo .
docker run -p 8080:5000 flask-demo