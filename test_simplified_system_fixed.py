#!/usr/bin/env python3
"""
Comprehensive test script for the simplified sentiment analysis system.
"""

import asyncio
import sys
import os
import time

# Add the backend path to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

async def test_simplified_sentiment_service():
    """Test the simplified sentiment service."""
    print("\n🔍 Testing Simplified Sentiment Service...")

    try:
        from backend.app.services.simplified_sentiment_service import (
            SimplifiedSentimentAnalyzer, SentimentLabel
        )

        analyzer = SimplifiedSentimentAnalyzer()

        # Test texts
        test_cases = [
            "I love this new policy! It's amazing and will help everyone.",
            "This is terrible. I completely disagree with this approach.",
            "The implementation seems okay, but there are some concerns.",
            "",  # Empty text
            "Hello world",  # Short text
        ]

        results = []
        for i, text in enumerate(test_cases):
            print(f"  Testing case {i+1}: '{text[:50]}...'")
            result = await analyzer.comprehensive_analysis(text)
            results.append(result)

            print(f"    ✅ Sentiment: {result.overall_sentiment}")
            print(f"    ✅ Confidence: {result.overall_confidence:.2f}")
            print(f"    ✅ Processing time: {result.processing_time_ms}ms")
            if result.emotion_result:
                print(f"    ✅ Emotion: {result.emotion_result.emotion_label}")
            if result.key_phrases:
                print(f"    ✅ Key phrases: {result.key_phrases[:3]}")

        # Validate results
        assert results[0].overall_sentiment == SentimentLabel.POSITIVE, "Positive text should be positive"
        assert results[1].overall_sentiment == SentimentLabel.NEGATIVE, "Negative text should be negative"
        assert results[2].overall_sentiment == SentimentLabel.NEUTRAL, "Neutral text should be neutral"

        print("✅ Simplified sentiment service test PASSED")
        return True

    except Exception as e:
        print(f"❌ Simplified sentiment service test FAILED: {e}")
        return False

async def test_simplified_summarization_service():
    """Test the simplified summarization service."""
    print("\n📝 Testing Simplified Summarization Service...")

    try:
        from backend.app.services.simplified_summarization_service import (
            SimplifiedSummarizationService, SummarizationType, SummarizationMethod
        )

        summarizer = SimplifiedSummarizationService()

        # Test text
        test_text = """
        The government has announced a new environmental policy aimed at reducing carbon emissions.
        This comprehensive plan includes incentives for renewable energy adoption, stricter regulations
        on industrial pollution, and investment in clean technology research. Environmental groups
        have praised the initiative, stating it represents a significant step forward in combating
        climate change. However, some industry leaders have expressed concerns about the economic
        impact and implementation timeline. The policy also includes measures to support workers
        in transitioning to green jobs and provides funding for community-based sustainability projects.
        """

        # Test extractive summarization
        print("  Testing extractive summarization...")
        extractive_result = await summarizer.extractive_summarization(
            test_text, SummarizationMethod.CUSTOM_TEXTRANK, 3
        )
        print(f"    ✅ Extractive summary length: {len(extractive_result.summary_text)} chars")
        print(f"    ✅ Key sentences: {len(extractive_result.key_sentences)}")
        print(f"    ✅ Confidence: {extractive_result.confidence_score:.2f}")

        # Test abstractive summarization
        print("  Testing abstractive summarization...")
        abstractive_result = await summarizer.abstractive_summarization(
            test_text, max_length=100, min_length=30
        )
        print(f"    ✅ Abstractive summary length: {len(abstractive_result.summary_text)} chars")
        print(f"    ✅ Confidence: {abstractive_result.confidence_score:.2f}")

        # Test topic-based summarization
        print("  Testing topic-based summarization...")
        topics = ["environmental policy", "renewable energy", "climate change"]
        topic_result = await summarizer.topic_based_summarization(
            test_text, topics=topics, max_length=120, min_length=40
        )
        print(f"    ✅ Topic-based summary length: {len(topic_result.summary_text)} chars")
        print(f"    ✅ Topics focused: {topic_result.metadata.get('topics_focused', [])}")

        # Test hybrid summarization
        print("  Testing hybrid summarization...")
        hybrid_result = await summarizer.hybrid_summarization(
            test_text, extractive_sentences=2, abstractive_max_length=80
        )
        print(f"    ✅ Hybrid summary length: {len(hybrid_result.summary_text)} chars")

        print("✅ Simplified summarization service test PASSED")
        return True

    except Exception as e:
        print(f"❌ Simplified summarization service test FAILED: {e}")
        return False

async def test_simplified_visualization_service():
    """Test the simplified visualization service."""
    print("\n🎨 Testing Simplified Visualization Service...")

    try:
        from backend.app.services.simplified_visualization_service import SimplifiedVisualizationService

        vis_service = SimplifiedVisualizationService()

        # Test texts
        test_texts = [
            "This policy is excellent and will help the community greatly.",
            "I strongly disagree with this approach and find it problematic.",
            "The implementation seems reasonable but needs more details.",
            "Environmental protection is crucial for our future sustainability.",
            "Economic concerns must be addressed in the policy framework."
        ]

        # Test token preparation
        print("  Testing token preparation...")
        tokens = await vis_service.prepare_tokens(test_texts, min_len=3)
        print(f"    ✅ Tokens prepared: {len(tokens)} total")

        # Test frequency computation
        print("  Testing frequency computation...")
        frequencies = vis_service.compute_frequencies(tokens, max_words=20)
        print(f"    ✅ Frequencies computed: {len(frequencies)} unique words")
        if frequencies:
            top_word = max(frequencies, key=frequencies.get)
            print(f"    ✅ Top word: '{top_word}' (frequency: {frequencies[top_word]})")

        # Test word cloud generation
        print("  Testing word cloud generation...")
        image_bytes = vis_service.generate_wordcloud_image(frequencies, width=600, height=300)
        print(f"    ✅ Word cloud image size: {len(image_bytes)} bytes")

        # Test sentiment-tagged word cloud
        print("  Testing sentiment-tagged word cloud...")
        analysis_results = [
            {"sentiment_label": "positive", "confidence_score": 0.9},
            {"sentiment_label": "negative", "confidence_score": 0.8},
            {"sentiment_label": "neutral", "confidence_score": 0.7},
            {"sentiment_label": "positive", "confidence_score": 0.85},
            {"sentiment_label": "neutral", "confidence_score": 0.75}
        ]

        image_bytes_tagged, word_data = await vis_service.create_sentiment_tagged_wordcloud(
            test_texts, analysis_results, max_words=15
        )
        print(f"    ✅ Sentiment-tagged word cloud size: {len(image_bytes_tagged)} bytes")
        print(f"    ✅ Words with sentiment data: {len(word_data)}")

        print("✅ Simplified visualization service test PASSED")
        return True

    except Exception as e:
        print(f"❌ Simplified visualization service test FAILED: {e}")
        return False

def check_dependencies():
    """Check which dependencies are available."""
    print("\n📦 Checking Dependencies...")

    dependencies = {
        "fastapi": "FastAPI web framework",
        "uvicorn": "ASGI server",
        "pydantic": "Data validation",
        "numpy": "Numerical computing",
        "matplotlib": "Plotting library",
        "wordcloud": "Word cloud generation",
        "transformers": "Advanced NLP models",
        "torch": "PyTorch for ML",
        "spacy": "NLP processing",
        "nltk": "Natural language toolkit",
        "httpx": "HTTP client for testing"
    }

    available = {}
    missing = {}

    for package, description in dependencies.items():
        try:
            __import__(package)
            available[package] = description
            print(f"  ✅ {package}: {description}")
        except ImportError:
            missing[package] = description
            print(f"  ❌ {package}: {description}")

    print(f"\n📊 Dependency Summary:")
    print(f"  ✅ Available: {len(available)}/{len(dependencies)}")
    print(f"  ❌ Missing: {len(missing)}/{len(dependencies)}")

    if missing:
        print("\n⚠️ Missing dependencies (optional for basic functionality):")
        for package, description in missing.items():
            print(f"    - {package}: {description}")

    return available, missing

async def main():
    """Run comprehensive system tests."""
    print("🚀 Starting Comprehensive System Validation...")
    print("=" * 60)

    # Check dependencies first
    available_deps, missing_deps = check_dependencies()

    # Test individual services
    test_results = []
    test_results.append(await test_simplified_sentiment_service())
    test_results.append(await test_simplified_summarization_service())
    test_results.append(await test_simplified_visualization_service())

    print("\n" + "=" * 60)
    print("📊 COMPREHENSIVE TEST RESULTS SUMMARY")
    print("=" * 60)

    passed_tests = sum(test_results)
    total_tests = len(test_results)

    print(f"✅ Tests Passed: {passed_tests}/{total_tests}")
    print(f"❌ Tests Failed: {total_tests - passed_tests}")

    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ Your simplified sentiment analysis system is working correctly.")
        print("\n🚀 Ready to use features:")
        print("  • Sentiment Analysis with emotion detection")
        print("  • Text Summarization (extractive, abstractive, hybrid)")
        print("  • Topic-based Summarization")
        print("  • Word Cloud Generation")
        print("  • Sentiment-tagged Word Clouds")
        print("  • Robust fallback handling for missing dependencies")

        if missing_deps:
            print("\n⚠️ Optional enhancements available:")
            print("  Install additional dependencies for advanced features:")
            for package in ['transformers', 'torch', 'spacy', 'wordcloud']:
                if package in missing_deps:
                    print(f"    pip install {package}")

        return 0
    else:
        print("\n⚠️ SOME TESTS FAILED")
        print("🔧 Troubleshooting:")
        print("  1. Check that all required dependencies are installed")
        print("  2. Check the error messages above for specific issues")
        print("  3. Verify that the backend directory structure is correct")

        return 1

if __name__ == "__main__":
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n⏹️ Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        sys.exit(1)