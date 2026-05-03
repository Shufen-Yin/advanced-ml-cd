# Advanced ML Continuous Deployment - Assignment 3

## Project Description
This repository contains a containerized sentiment analysis API using FastAPI and an ONNX model. It features a fully automated CI/CD pipeline via GitHub Actions.

## Prerequisites
- Docker installed locally
- Python 3.10
- GitHub account for Actions

## Installation & Setup
1. Clone the repository:
   `git clone https://github.com/Shufen-Yin/advanced-ml-cd.git`
2. Install dependencies:
   `pip install -r requirements.txt`

## How to Run with Docker
1. Build the image:
   `docker build -t sentiment-app .`
2. Run the container:
   `docker run -p 8000:8000 sentiment-app`

## CI/CD Pipeline
This project uses **GitHub Actions** to:
- Lint the code.
- Run unit tests and integration tests using `pytest`.
- Assess model robustness with edge-case inputs (Empty strings, invalid types).
