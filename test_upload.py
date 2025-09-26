import requests

# Test the ingestion upload endpoint
url = "http://localhost:8000/api/v1/ingestion/upload"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0QGV4YW1wbGUuY29tIiwiZXhwIjoxNzU4ODgwODAyLCJ0eXBlIjoiYWNjZXNzIn0.1TUcrgpQ0j4Rk4I4SZoip0SEuCDS8yw6wPDAOa-t4bI"

headers = {
    "Authorization": f"Bearer {token}"
}

files = {
    "file": ("test_comments.csv", open("test_comments.csv", "rb"), "text/csv")
}

response = requests.post(url, headers=headers, files=files)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code == 200:
    print("✅ File upload successful!")
else:
    print("❌ File upload failed")