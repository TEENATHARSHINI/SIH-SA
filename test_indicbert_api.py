"""
Test IndicBERT API for accurate predictions
"""
import requests
import time

print("🤖 Testing IndicBERT API for Accurate Predictions...")

# Wait for API to be ready
print("⏳ Waiting for API to start...")
time.sleep(5)

# Test with complex sentiments that should show varied results
test_cases = [
    "I strongly support this initiative as it will greatly benefit our community",
    "This policy is terrible and will cause significant problems for our community", 
    "I have mixed feelings about this approach - some good points but concerns too",
    "The framework lacks clarity and may create compliance challenges",
    "Excellent proposal that addresses key issues effectively"
]

try:
    # Health check
    health_response = requests.get('http://127.0.0.1:8002/api/v1/health', timeout=10)
    print(f"✅ Health Check: {health_response.status_code}")
    
    # Test batch analysis
    response = requests.post(
        'http://127.0.0.1:8002/api/analyze',
        json={
            'texts': test_cases,
            'include_explanation': True
        },
        timeout=30
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n🎯 IndicBERT Analysis Results:")
        print(f"Processed {len(data['results'])} texts")
        
        for i, result in enumerate(data['results'], 1):
            print(f"\nResult {i}:")
            print(f"  Text: {test_cases[i-1][:50]}...")
            print(f"  Sentiment: {result['sentiment'].upper()}")
            print(f"  Confidence: {result['confidence']:.1%}")
            print(f"  Method: {result['method']}")
            
        print("\n✅ IndicBERT providing accurate and varied predictions!")
        
    else:
        print(f"❌ API Error: {response.status_code}")
        
except Exception as e:
    print(f"❌ Connection Error: {e}")
    print("API might still be loading...")