"""
Test script to verify that all services are working correctly.
"""

import requests
import time

def test_backend_api():
    """Test the backend API endpoints."""
    base_url = "http://127.0.0.1:8000"
    
    print("Testing backend API...")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/api/v1/health")
        if response.status_code == 200:
            print("✅ Health check: PASSED")
        else:
            print(f"❌ Health check: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Health check: FAILED ({str(e)})")
    
    # Test analyze-text endpoint
    try:
        payload = {"text": "This is a test sentence for sentiment analysis."}
        response = requests.post(f"{base_url}/api/v1/analyze-text", json=payload)
        if response.status_code == 200:
            print("✅ Sentiment analysis: PASSED")
        else:
            print(f"❌ Sentiment analysis: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Sentiment analysis: FAILED ({str(e)})")
    
    # Test summarize-text endpoint
    try:
        payload = {"text": "This is a test sentence for summarization. This is another sentence. And this is a third sentence."}
        response = requests.post(f"{base_url}/api/v1/summarize-text", json=payload)
        if response.status_code == 200:
            print("✅ Text summarization: PASSED")
        else:
            print(f"❌ Text summarization: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Text summarization: FAILED ({str(e)})")

def test_frontend_access():
    """Test if frontend can access backend."""
    print("\nTesting frontend access to backend...")
    
    # This would typically be done from the frontend, but we can simulate it
    try:
        # Test if we can access the API from the frontend perspective
        response = requests.get("http://127.0.0.1:8000")
        if response.status_code == 200:
            print("✅ Frontend can access backend: PASSED")
        else:
            print(f"❌ Frontend can access backend: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Frontend can access backend: FAILED ({str(e)})")

if __name__ == "__main__":
    print("Running service tests...\n")
    
    test_backend_api()
    test_frontend_access()
    
    print("\nTest completed. Please check the results above.")