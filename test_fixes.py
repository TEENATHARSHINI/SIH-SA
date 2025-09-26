"""
Test script to verify the word cloud and sentiment analysis fixes
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from final_api import analyze_sentiment_advanced, create_word_frequencies, detect_language

def test_sentiment_analysis():
    """Test sentiment analysis with various inputs"""
    print("=== Testing Sentiment Analysis ===")
    
    test_cases = [
        "This policy is excellent and will help citizens",
        "यह नीति बहुत अच्छी है",
        "The implementation needs improvement", 
        "I support this initiative completely",
        "This is terrible and will cause problems",
        "மிகவும் நல்லது"
    ]
    
    for i, text in enumerate(test_cases, 1):
        print(f"\nTest {i}: {text}")
        try:
            result = analyze_sentiment_advanced(text)
            print(f"  Sentiment: {result['sentiment']}")
            print(f"  Confidence: {result['confidence']:.2f}")
            print(f"  Language: {result['language_info']['language']}")
            print(f"  Key indicators: {result['key_indicators']}")
        except Exception as e:
            print(f"  ERROR: {e}")

def test_word_cloud():
    """Test word cloud generation"""
    print("\n=== Testing Word Cloud Generation ===")
    
    comments = [
        "This policy is excellent and will help citizens",
        "यह नीति बहुत अच्छी है",
        "The implementation needs improvement",
        "I support this initiative completely",
        "This is terrible and will cause problems"
    ]
    
    print(f"Analyzing {len(comments)} comments:")
    for comment in comments:
        print(f"  - {comment}")
    
    try:
        word_frequencies = create_word_frequencies(comments)
        print(f"\nWord frequencies generated: {len(word_frequencies)} words")
        print("Top 10 words:")
        for word, freq in list(word_frequencies.items())[:10]:
            print(f"  {word}: {freq}")
    except Exception as e:
        print(f"ERROR: {e}")

def test_language_detection():
    """Test language detection"""
    print("\n=== Testing Language Detection ===")
    
    test_texts = [
        "This is English text",
        "यह हिंदी टेक्स्ट है",
        "இது தமிழ் உரை",
        "ఇది తెలుగు వచనం",
        "এটি বাংলা পাঠ্য"
    ]
    
    for text in test_texts:
        try:
            lang_info = detect_language(text)
            print(f"{text} -> {lang_info['language']} (confidence: {lang_info['confidence']:.2f})")
        except Exception as e:
            print(f"{text} -> ERROR: {e}")

if __name__ == "__main__":
    print("Testing Complete MCA Sentiment Analysis System")
    print("=" * 50)
    
    test_sentiment_analysis()
    test_word_cloud()
    test_language_detection()
    
    print("\n" + "=" * 50)
    print("Testing completed!")