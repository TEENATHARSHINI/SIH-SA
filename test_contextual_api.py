"""
Test the updated API with contextual analysis
"""
import requests
import json

# Test data with complex sentiments that require contextual understanding
test_cases = [
    "I strongly support this new policy as it will improve transparency in government operations. This is exactly what we need to restore public trust.",
    "The framework lacks clarity in several key areas and may create compliance challenges for smaller organizations. However, I do appreciate the effort.",
    "This policy is terrible and will cause significant problems. But I understand the intention behind it.",
    "Although the concept has merit, I am concerned about the implementation challenges and potential unintended consequences.",
    "I have mixed feelings about this proposal. While some aspects are good, others need more work before implementation."
]

print("🧠 Testing API with Advanced Contextual Sentiment Analysis")
print("=" * 70)

# Test health endpoint
try:
    health_response = requests.get('http://127.0.0.1:8002/api/v1/health', timeout=5)
    print(f"✅ Health Check: {health_response.status_code} - {health_response.json()}")
except Exception as e:
    print(f"❌ Health check failed: {e}")
    exit()

print()

# Test single analysis
print("🔍 Testing Single Text Analysis:")
test_text = test_cases[0]
try:
    response = requests.post(
        'http://127.0.0.1:8002/api/v1/analyze',
        json={'text': test_text},
        timeout=10
    )
    
    if response.status_code == 200:
        result = response.json()['result']
        print(f"Text: {test_text}")
        print(f"Sentiment: {result['sentiment'].upper()}")
        print(f"Confidence: {result['confidence']:.1%}")
        print(f"Method: {result['method']}")
        print(f"Justification: {', '.join(result['justification_words'])}")
        print(f"Reasoning: {result['reasoning']}")
    else:
        print(f"❌ Single analysis failed: {response.status_code} - {response.text}")
        
except Exception as e:
    print(f"❌ Single analysis error: {e}")

print()

# Test batch analysis
print("📊 Testing Batch Analysis:")
try:
    response = requests.post(
        'http://127.0.0.1:8002/api/analyze',
        json={
            'texts': test_cases[:3],
            'include_explanation': True
        },
        timeout=15
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Batch analysis successful! Processed {len(data['results'])} texts")
        
        for i, result in enumerate(data['results'], 1):
            print(f"\nResult {i}:")
            print(f"  Sentiment: {result['sentiment'].upper()}")
            print(f"  Confidence: {result['confidence']:.1%}")
            print(f"  Justification: {', '.join(result['justification_words'][:2])}")
            
    else:
        print(f"❌ Batch analysis failed: {response.status_code} - {response.text}")
        
except Exception as e:
    print(f"❌ Batch analysis error: {e}")

print()
print("🎉 API testing completed with Advanced Contextual Analysis!")