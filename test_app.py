from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_main():
    """Test the root endpoint for API availability."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}

def test_predict_empty_input():
    """Test robustness by sending an empty string to the prediction endpoint."""
    # This demonstrates edge case handling as required by Part 2
    response = client.post("/predict", json={"text": ""})
    # If your app has validation, it should return 422 Unprocessable Entity
    assert response.status_code == 422

def test_predict_malicious_input():
    """Test robustness against invalid data types."""
    # Sending an integer instead of a string to test robustness
    response = client.post("/predict", json={"text": 12345})
    assert response.status_code == 422
