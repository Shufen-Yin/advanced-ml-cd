# Advanced ML Continuous Deployment (Assignment 3)

## Project Overview
This project demonstrates a CI/CD pipeline for a sentiment analysis model using FastAPI and GitHub Actions.

## Files
- `app.py`: FastAPI application script.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Containerization configuration.
- `sentiment_model.onnx`: Trained machine learning model.

## How to Run
1. Build the docker image: `docker build -t sentiment-app .`
2. Run the container: `docker run -p 8000:8000 sentiment-app`
