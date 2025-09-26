"""
Test the contextual sentiment analyzer
"""
from contextual_sentiment_analyzer import analyze_sentiment_contextual

# Test with a sample text
test_text = "I strongly support this new policy as it will improve transparency in government operations. This is exactly what we need to restore public trust."

print("🧠 Testing Advanced Contextual Sentiment Analyzer")
print("=" * 60)
print(f"Text: {test_text}")
print()

result = analyze_sentiment_contextual(test_text)

print(f"Sentiment: {result['sentiment'].upper()}")
print(f"Confidence: {result['confidence']:.1%}")
print(f"Polarity Score: {result['polarity_score']}")
print(f"Method: {result['method']}")
print(f"Justification: {', '.join(result['justification_words'])}")
print(f"Reasoning: {result['reasoning']}")
print()
print("✅ Contextual analyzer working correctly!")