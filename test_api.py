import requests
import json

# Test the working API
data = {
    'texts': ['This policy is excellent and will benefit all citizens.', 'The framework lacks clarity in several areas.'],
    'include_explanation': False
}

try:
    response = requests.post('http://127.0.0.1:8002/api/analyze', json=data, timeout=10)
    print(f'Status: {response.status_code}')
    if response.status_code == 200:
        result = response.json()
        print(f'API is working! Got {len(result["results"])} results')
        for i, res in enumerate(result['results']):
            print(f'Text {i+1}: {res["sentiment"]} confidence={res["confidence"]:.1%}')
            print(f'  Justification: {", ".join(res["justification_words"])}')
    else:
        print(f'Error: {response.text}')
except Exception as e:
    print(f'Request failed: {e}')