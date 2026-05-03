from fastapi import FastAPI
import onnxruntime as ort

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Model API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}