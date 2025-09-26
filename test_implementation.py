#!/usr/bin/env python3
"""
Quick test script to validate the enhanced sentiment analysis and summarization features.
"""

import asyncio
import sys
import os

# Add the backend path to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

async def test_sentiment_service():
    """Test the enhanced sentiment service."""
    try:
        from backend.app.services.sentiment_service import SentimentAnalyzer, AnalysisMethod

        print("🔍 Testing Sentiment Service...")
        analyzer = SentimentAnalyzer()

        # Test text
        test_text = "I strongly support the new policy but have concerns about its implementation timeline."

        # Test comprehensive analysis
        result = await analyzer.comprehensive_analysis(test_text)

        print(f"✅ Overall sentiment: {result.overall_sentiment}")
        print(f"✅ Confidence: {result.overall_confidence:.2f}")
        print(f"✅ Processing time: {result.processing_time_ms}ms")
        print(f"✅ Aspect sentiments: {len(result.aspect_sentiments)}")
        print(f"✅ Emotions detected: {len(result.emotion_result.detected_emotions) if result.emotion_result else 0}")

        return True
    except Exception as e:
        print(f"❌ Sentiment service test failed: {e}")
        return False

async def test_summarization_service():
    """Test the enhanced summarization service."""
    try:
        from backend.app.services.summarization_service import SummarizationService

        print("\n📝 Testing Summarization Service...")
        summarizer = SummarizationService()

        # Test text
        test_text = "The government has proposed a new environmental policy that aims to reduce carbon emissions by 30% over the next decade. This policy includes incentives for renewable energy adoption and stricter regulations on industrial pollution. Many stakeholders have expressed both support and concerns about the implementation details."

        # Test topic-based summarization
        topics = ["environmental policy", "carbon emissions", "renewable energy"]
        result = await summarizer.topic_based_summarization(
            text=test_text,
            topics=topics,
            max_length=100,
            min_length=30
        )

        print(f"✅ Topic-based summary generated: {len(result.summary_text)} characters")
        print(f"✅ Method used: {result.method}")
        print(f"✅ Confidence: {result.confidence_score:.2f}")
        print(f"✅ Topics focused: {result.metadata.get('topics_focused', [])}")

        return True
    except Exception as e:
        print(f"❌ Summarization service test failed: {e}")
        return False

async def test_visualization_service():
    """Test the enhanced visualization service."""
    try:
        from backend.app.services.visualization_service import VisualizationService

        print("\n🎨 Testing Visualization Service...")
        vis_service = VisualizationService()

        # Test data
        texts = [
            "This policy is excellent and will help the community.",
            "I disagree with this approach completely.",
            "The implementation seems reasonable but needs more details."
        ]

        analysis_results = [
            {"sentiment_label": "positive", "sentiment_score": 0.8, "confidence_score": 0.9},
            {"sentiment_label": "negative", "sentiment_score": -0.6, "confidence_score": 0.8},
            {"sentiment_label": "neutral", "sentiment_score": 0.1, "confidence_score": 0.7}
        ]

        # Test sentiment-tagged word cloud
        image_bytes, word_data = await vis_service.create_sentiment_tagged_wordcloud(
            texts=texts,
            analysis_results=analysis_results,
            max_words=50
        )

        print(f"✅ Sentiment-tagged word cloud generated: {len(image_bytes)} bytes")
        print(f"✅ Words processed: {len(word_data)}")

        # Check if we have sentiment data
        if word_data:
            sample_word = list(word_data.keys())[0] if word_data else None
            if sample_word:
                data = word_data[sample_word]
                print(f"✅ Sample word '{sample_word}': sentiment={data.sentiment_label}, confidence={data.confidence:.2f}")

        return True
    except Exception as e:
        print(f"❌ Visualization service test failed: {e}")
        return False

async def main():
    """Run all tests."""
    print("🚀 Starting implementation validation tests...\n")

    results = []
    results.append(await test_sentiment_service())
    results.append(await test_summarization_service())
    results.append(await test_visualization_service())

    print("\n📊 Test Results Summary:")
    print(f"✅ Passed: {sum(results)}/{len(results)}")

    if all(results):
        print("🎉 All tests passed! Implementation is ready.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)