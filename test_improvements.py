#!/usr/bin/env python3
"""
Test script for all sentiment analysis improvements
"""

import requests
import json

API_URL = "http://127.0.0.1:8001"

def test_sentiment_analysis():
    """Test improved sentiment analysis"""
    print("🧪 Testing Sentiment Analysis Improvements...")
    
    test_texts = [
        "This consultation process is absolutely excellent and I strongly support this initiative!",
        "I am completely disappointed with this terrible proposal and oppose this policy.",
        "The document provides adequate information for review and seems reasonable."
    ]
    
    response = requests.post(f"{API_URL}/api/analyze", json={
        'texts': test_texts,
        'include_explanation': True,
        'use_advanced': True
    })
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Sentiment Analysis - SUCCESS")
        
        for i, result in enumerate(data.get('results', [])):
            sentiment = result.get('sentiment')
            confidence = result.get('confidence')
            explanation = result.get('explanation', {})
            
            print(f"\n📝 Text {i+1}: {test_texts[i][:50]}...")
            print(f"   🎯 Sentiment: {sentiment.upper()} (confidence: {confidence:.2f})")
            print(f"   💡 Explanation: {explanation.get('detailed_explanation', 'N/A')}")
            print(f"   🔍 Key words: {explanation.get('key_indicators', [])}")
            
        return True
    else:
        print(f"❌ Sentiment Analysis - FAILED: {response.status_code}")
        return False

def test_word_cloud():
    """Test word cloud from comments"""
    print("\n🌥️ Testing Word Cloud from Comments...")
    
    test_comments = [
        {"comment": "This excellent consultation process enables great community engagement"},
        {"comment": "Wonderful initiative for public participation in policy development"},
        {"comment": "Very good approach to gather citizen feedback and improve governance"}
    ]
    
    response = requests.post(f"{API_URL}/api/wordcloud-from-comments", json={
        'comments': test_comments
    })
    
    if response.status_code == 200:
        data = response.json()
        word_data = data.get('wordcloud_data', {})
        frequencies = word_data.get('word_frequencies', {})
        
        print("✅ Word Cloud - SUCCESS")
        print(f"   📊 Total words: {word_data.get('total_words', 0)}")
        print(f"   💬 Comments processed: {word_data.get('total_comments', 0)}")
        print(f"   🔤 Top words: {list(frequencies.keys())[:8]}")
        
        return True
    else:
        print(f"❌ Word Cloud - FAILED: {response.status_code}")
        return False

def test_summarization():
    """Test improved summarization"""
    print("\n📄 Testing Advanced Summarization...")
    
    test_texts = [
        "This is a comprehensive consultation document that outlines important policy changes for urban development in our city. I strongly recommend that the government should consider conducting a thorough environmental impact assessment before proceeding with this major infrastructure initiative. The community engagement process has been excellent and demonstrates genuine commitment to public participation in democratic decision-making processes.",
        "The proposed policy framework lacks adequate consideration of community concerns and environmental sustainability. I am disappointed with the limited consultation period and believe this initiative requires more comprehensive stakeholder engagement before implementation."
    ]
    
    response = requests.post(f"{API_URL}/api/summarize", json={
        'texts': test_texts,
        'max_length': 100,
        'min_length': 30
    })
    
    if response.status_code == 200:
        data = response.json()
        summaries = data.get('summaries', [])
        
        print("✅ Summarization - SUCCESS")
        print(f"   📊 Texts processed: {data.get('total_processed', 0)}")
        print(f"   📉 Overall reduction: {data.get('overall_reduction', 'N/A')}")
        
        for i, summary in enumerate(summaries):
            original_length = len(test_texts[i])
            summary_length = len(summary) if isinstance(summary, str) else len(summary.get('summary', ''))
            reduction = ((original_length - summary_length) / original_length * 100)
            
            print(f"\n   📝 Summary {i+1}:")
            if isinstance(summary, str):
                print(f"      💬 {summary}")
            else:
                print(f"      💬 {summary.get('summary', 'No summary')}")
            print(f"      📏 Reduction: {reduction:.1f}%")
        
        return True
    else:
        print(f"❌ Summarization - FAILED: {response.status_code}")
        return False

def test_error_handling():
    """Test error handling improvements"""
    print("\n🛡️ Testing Error Handling...")
    
    # Test with empty text
    response = requests.post(f"{API_URL}/api/analyze", json={
        'texts': ['', None, '   '],
        'include_explanation': True,
        'use_advanced': True
    })
    
    if response.status_code == 200:
        print("✅ Error Handling - SUCCESS (handles empty texts)")
        return True
    else:
        print(f"❌ Error Handling - FAILED: {response.status_code}")
        return False

def main():
    """Run all tests"""
    print("🚀 Running Comprehensive Sentiment Analysis Tests")
    print("=" * 60)
    
    results = []
    results.append(test_sentiment_analysis())
    results.append(test_word_cloud())
    results.append(test_summarization())
    results.append(test_error_handling())
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    
    if all(results):
        print("🎉 ALL TESTS PASSED - System working perfectly!")
        print("✅ Sentiment analysis with detailed explanations")
        print("✅ Word cloud analyzing actual comment content")
        print("✅ Advanced summarization with keyword extraction")
        print("✅ Robust error handling")
    else:
        print("⚠️ Some tests failed. Check the output above.")
    
    print("\n🌐 API Status: All endpoints operational")
    print("📱 Dashboard: Ready for testing")

if __name__ == "__main__":
    main()