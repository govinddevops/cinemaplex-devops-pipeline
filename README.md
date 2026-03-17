<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a0a0a,100:2d0a0a&height=200&section=header&text=Cinemaplex%20DevOps%20Pipeline&fontSize=32&fontColor=e50914&animation=fadeIn&fontAlignY=38&desc=Production-grade%20Netflix-style%20Video%20Streaming%20Infrastructure&descAlignY=58&descSize=14&descColor=aaaaaa" width="100%"/>

![CI/CD Pipeline](https://github.com/govinddevops/cinemaplex-devops-pipeline/actions/workflows/ci-cd.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS_S3-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=flat-square&logo=ffmpeg&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)

</div>

---

## 🎬 Overview

> **Production-grade Netflix-style video streaming platform** built as a microservices architecture. Features automated video processing pipeline using FFmpeg, AWS S3 storage, Kubernetes orchestration with HPA, full CI/CD with Jenkins and GitHub Actions, Trivy security scanning, and Prometheus + Grafana observability.
```yaml
Author      : Govind
Company     : Ezdat Technology Pvt Ltd
Stack       : React + Node.js + Python + FFmpeg + Docker + K8s
Storage     : AWS S3 + CloudFront CDN
CI/CD       : Jenkins + GitHub Actions
Security    : Trivy + SonarQube
Monitoring  : Prometheus + Grafana + Loki
Duration    : 1 Month (Production-grade implementation)
```

---

## 🏗️ Architecture
```
                        USER
                          |
              +-----------+-----------+
              |   Nginx Ingress       |
              |   (Load Balancer)     |
              +-----------+-----------+
                          |
          +---------------+---------------+
          |               |               |
    +----------+   +----------+   +-------------+
    | Frontend |   | Backend  |   |   Video     |
    |  React   |   | Node.js  |   | Processor   |
    | Netflix  |   |   API    |   |   FFmpeg    |
    |    UI    |   |          |   |             |
    +----------+   +----+-----+   +------+------+
                        |                |
               +--------+----+    +------+------+
               |   Redis     |    |   AWS S3    |
               |   Cache     |    | 480p/720p/  |
               |             |    |   1080p     |
               +--------+----+    +-------------+
                        |
               +--------+----+
               |   MongoDB   |
               | Video Meta  |
               +-------------+
                        |
          +-------------+-------------+
          |       OBSERVABILITY       |
          |  Prometheus + Grafana     |
          |  Loki + Alertmanager      |
          +-------------+-------------+
                        |
          +-------------+-------------+
          |          CI/CD            |
          |  GitHub Actions + Jenkins |
          |  Trivy + SonarQube        |
          +---------------------------+
```

---

## 🧰 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | React 18 + Tailwind | Netflix-style UI |
| Backend | Node.js + Express | REST API |
| Video Processing | Python + FFmpeg | Multi-resolution pipeline |
| Storage | AWS S3 + CloudFront | Video delivery CDN |
| Cache | Redis | Fast metadata cache |
| Database | MongoDB | Video metadata |
| Container | Docker Multi-stage | Optimized images |
| Orchestration | Kubernetes + HPA | Auto-scaling |
| CI Pipeline | GitHub Actions | Test + Build + Push |
| CD Pipeline | Jenkins | Deploy to K8s |
| Security | Trivy + SonarQube | Image + code scanning |
| Monitoring | Prometheus + Grafana | Dashboards + alerts |
| Logs | Loki | Log aggregation |
| Ingress | Nginx | Load balancing |

---

## 📁 Project Structure
```
cinemaplex-devops-pipeline/
├── services/
│   ├── frontend/           <- React Netflix UI
│   │   ├── src/
│   │   │   ├── pages/      <- Home, Player, Upload
│   │   │   └── components/ <- Navbar
│   │   ├── Dockerfile      <- Multi-stage build
│   │   └── nginx.conf      <- Production config
│   ├── backend-api/        <- Node.js REST API
│   │   ├── src/server.js   <- Express server
│   │   └── Dockerfile      <- Multi-stage build
│   └── video-processor/    <- FFmpeg pipeline
│       ├── processor.py    <- Multi-resolution processing
│       └── Dockerfile      <- FFmpeg optimized
├── k8s/
│   ├── base/               <- K8s manifests
│   │   ├── frontend/       <- Frontend deployment
│   │   ├── backend/        <- Backend deployment
│   │   ├── ingress.yaml    <- Nginx ingress
│   │   ├── hpa.yaml        <- Auto-scaling
│   │   ├── configmap.yaml  <- App config
│   │   └── secrets.yaml    <- Sensitive data
│   └── overlays/
│       ├── dev/            <- Dev environment
│       └── prod/           <- Prod environment
├── monitoring/
│   ├── prometheus/         <- Metrics + alerts
│   └── grafana/            <- Dashboards
├── jenkins/
│   └── Jenkinsfile         <- Full CD pipeline
├── .github/workflows/
│   └── ci-cd.yml           <- Full CI pipeline
└── docker-compose.yml      <- Local development
```

---

## ⚙️ Video Processing Pipeline
```
User uploads video
       |
       v
AWS S3 (raw upload)
       |
       v
FFmpeg Processing Service
       |
   +---+---+---+
   |   |   |   |
  480p 720p 1080p  + Thumbnail
   |   |   |   |
   +---+---+---+
       |
       v
AWS S3 (processed videos)
       |
       v
CloudFront CDN
       |
       v
Redis Cache (metadata)
       |
       v
User streams video
```

---

## 🚀 Quick Start
```bash
# Clone the repo
git clone https://github.com/govinddevops/cinemaplex-devops-pipeline.git
cd cinemaplex-devops-pipeline

# Set environment variables
cp .env.example .env
# Edit .env with your AWS credentials

# Run locally with Docker Compose
docker-compose up -d

# Access the app
http://localhost:3000        <- Netflix UI
http://localhost:3001/health <- Backend API
http://localhost:9090        <- Prometheus
http://localhost:3002        <- Grafana
```

---

## ☸️ Deploy to Kubernetes
```bash
# Apply all manifests
kubectl apply -f k8s/base/configmap.yaml
kubectl apply -f k8s/base/secrets.yaml
kubectl apply -f k8s/base/frontend/deployment.yaml
kubectl apply -f k8s/base/backend/deployment.yaml
kubectl apply -f k8s/base/ingress.yaml
kubectl apply -f k8s/base/hpa.yaml

# Check status
kubectl get pods -A
kubectl get svc -A
```

---

## 🔐 Security
```bash
# Trivy image scan
trivy image govinddevopsdocker/cinemaplex-frontend:latest

# Trivy filesystem scan
trivy fs --severity HIGH,CRITICAL .
```

---

## 📊 Monitoring
```
Grafana Dashboard: http://localhost:3002
Username: admin
Password: cinemaplex123

Key Metrics:
- Active video streams
- Bandwidth usage per second
- CPU/Memory per pod
- Video processing success rate
- API response times
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2d0a0a,50:1a0a0a,100:0d1117&height=100&section=footer&animation=fadeIn" width="100%"/>

**Built with passion by Govind | Junior DevOps Engineer**

⭐ Star this repo if it helped you!

</div>
trigger
