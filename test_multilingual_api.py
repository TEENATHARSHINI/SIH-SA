"""
Test script for the multilingual sentiment analysis API
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:8001"

def test_health_check():
    """Test health check endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    if response.status_code == 200:
        data = response.json()
        print("✅ Health Check:")
        print(f"   Status: {data['status']}")
        print(f"   Basic explainer: {data['basic_explainer_available']}")
        print(f"   Advanced analyzer: {data['advanced_analyzer_available']}")
        print(f"   Wordcloud: {data['wordcloud_available']}")
        return True
    else:
        print("❌ Health check failed")
        return False

def test_basic_sentiment():
    """Test basic sentiment analysis"""
    test_texts = [
        "I love this product! It's amazing!",
        "This is terrible, worst experience ever.",
        "The product is okay, nothing special.",
        "यह बहुत अच्छा है",  # Hindi: This is very good
        "এটি খুব খারাপ",  # Bengali: This is very bad
        "நல்ல சேவை"  # Tamil: Good service
    ]
    
    payload = {
        "texts": test_texts,
        "include_explanation": True,
        "use_advanced": False
    }
    
    response = requests.post(f"{BASE_URL}/api/analyze", json=payload)
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Basic Sentiment Analysis:")
        for result in data['results']:
            print(f"   Text: {result['text'][:50]}...")
            print(f"   Sentiment: {result['sentiment']} (confidence: {result['confidence']:.2f})")
        
        print(f"\n   Summary: {data['summary']['sentiment_distribution']}")
        return True
    else:
        print("❌ Basic sentiment analysis failed")
        print(f"Error: {response.text}")
        return False

def test_advanced_sentiment():
    """Test advanced multilingual sentiment analysis"""
    test_texts = [
        "मुझे यह बहुत पसंद है! यह शानदार है!",  # Hindi: I love this! It's wonderful!
        "This mixed language text करना चाहिए work fine",  # Mixed Hindi-English
        "தமிழ் மொழி மிகவும் அழகான மொழி",  # Tamil: Tamil is a very beautiful language
        "আমি এই পণ্যটি পছন্দ করি না"  # Bengali: I don't like this product
    ]
    
    payload = {
        "texts": test_texts,
        "include_explanation": True,
        "use_advanced": True
    }
    
    response = requests.post(f"{BASE_URL}/api/analyze", json=payload)
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Advanced Multilingual Sentiment Analysis:")
        for result in data['results']:
            print(f"   Text: {result['text'][:50]}...")
            print(f"   Sentiment: {result['sentiment']} (confidence: {result['confidence']:.2f})")
            if result.get('explanation') and 'language_info' in result['explanation']:
                lang_info = result['explanation']['language_info']
                print(f"   Language: {lang_info}")
        return True
    else:
        print("❌ Advanced sentiment analysis failed")
        print(f"Error: {response.text}")
        return False

def test_wordcloud():
    """Test wordcloud generation"""
    test_texts = [
        "Machine learning artificial intelligence technology innovation",
        "मशीन लर्निंग कृत्रिम बुद्धिमत्ता तकनीक नवाचार",  # Hindi
        "தொழில்நுட்பம் புதுமை செயற்கை நுண்ணறிவு",  # Tamil
    ]
    
    payload = {
        "texts": test_texts,
        "width": 800,
        "height": 400,
        "max_words": 50
    }
    
    response = requests.post(f"{BASE_URL}/api/wordcloud", json=payload)
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Wordcloud Generation:")
        print(f"   Status: {data['status']}")
        if 'languages_detected' in data:
            print(f"   Languages detected: {data['languages_detected']}")
        if 'scripts_detected' in data:
            print(f"   Scripts detected: {data['scripts_detected']}")
        return True
    else:
        print("❌ Wordcloud generation failed")
        print(f"Error: {response.text}")
        return False

def test_summarization():
    """Test text summarization"""
    test_texts = [
        """
        Artificial intelligence (AI) is transforming the way we live and work. 
        Machine learning algorithms can now process vast amounts of data to identify 
        patterns and make predictions. This technology is being used in healthcare 
        to diagnose diseases, in finance to detect fraud, and in transportation 
        to develop autonomous vehicles. The potential applications of AI are limitless, 
        but we must also consider the ethical implications and ensure that these 
        technologies are developed responsibly.
        """,
        """
        कृत्रिम बुद्धिमत्ता (AI) हमारे जीवन और काम करने के तरीके को बदल रही है। 
        मशीन लर्निंग एल्गोरिदम अब बड़ी मात्रा में डेटा को संसाधित कर सकते हैं। 
        यह तकनीक स्वास्थ्य सेवा में बीमारियों का निदान करने, वित्त में धोखाधड़ी 
        का पता लगाने में उपयोग की जा रही है।
        """
    ]
    
    payload = {
        "texts": test_texts,
        "max_length": 100,
        "min_length": 30
    }
    
    response = requests.post(f"{BASE_URL}/api/summarize", json=payload)
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Text Summarization:")
        print(f"   Status: {data['status']}")
        for i, summary in enumerate(data['summaries']):
            print(f"   Summary {i+1}: {summary['summary'][:100]}...")
        return True
    else:
        print("❌ Summarization failed")
        print(f"Error: {response.text}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Multilingual Sentiment Analysis API")
    print("=" * 50)
    
    try:
        # Test health check first
        if not test_health_check():
            return
        
        # Test basic functionality
        test_basic_sentiment()
        
        # Test advanced functionality (may take time to load models)
        print("\n🔄 Testing advanced features (models may need to download)...")
        test_advanced_sentiment()
        
        # Test wordcloud
        test_wordcloud()
        
        # Test summarization
        test_summarization()
        
        print("\n🎉 All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to API. Make sure the server is running on port 8001")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")

if __name__ == "__main__":
    main()