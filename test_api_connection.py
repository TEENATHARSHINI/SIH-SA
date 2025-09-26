"""
Quick test to verify API connection and sentiment analysis accuracy
"""
import requests
import json

def test_api_connection():
    """Test our advanced API server connection and accuracy."""
    
    # Test data including Row 7 
    test_cases = [
        {
            "text": "This is an excellent policy framework that will benefit everyone.",
            "expected": "positive"
        },
        {
            "text": "The framework lacks clarity in several key areas and may create compliance challenges for smaller organizations",
            "expected": "negative"  # This is Row 7 - should be NEGATIVE
        },
        {
            "text": "The policy is okay but could be improved.",
            "expected": "neutral"
        }
    ]
    
    print("🚀 Testing Advanced Sentiment Analysis API...")
    print("=" * 50)
    
    for i, case in enumerate(test_cases, 1):
        try:
            # Test with our advanced API
            payload = {
                "text": case["text"],
                "use_advanced": True
            }
            
            response = requests.post(
                "http://localhost:8002/api/explain",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                sentiment = result.get("sentiment", "unknown")
                confidence = result.get("confidence", 0) * 100
                
                # Check if result matches expected
                is_correct = sentiment.lower() == case["expected"].lower()
                status = "✅ CORRECT" if is_correct else "❌ WRONG"
                
                print(f"\nTest {i}: {status}")
                print(f"Text: {case['text'][:60]}...")
                print(f"Expected: {case['expected'].upper()}")
                print(f"Got: {sentiment.upper()} ({confidence:.1f}% confidence)")
                
                if i == 2:  # Row 7 test
                    print(f"🎯 ROW 7 RESULT: {sentiment.upper()} - {'PERFECT!' if is_correct else 'NEEDS FIX!'}")
                    
            else:
                print(f"\n❌ Test {i} failed: HTTP {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"\n🔌 Test {i}: API server not running on port 8002")
        except Exception as e:
            print(f"\n❌ Test {i} error: {e}")
    
    print("\n" + "=" * 50)
    print("Testing complete!")

if __name__ == "__main__":
    test_api_connection()