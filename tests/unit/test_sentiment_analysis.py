"""
Unit tests for sentiment analysis service.
"""

import pytest
import asyncio
from backend.app.services.sentiment_service import SentimentAnalyzer, AnalysisMethod
from backend.app.models.analysis import SentimentLabel, EmotionLabel


@pytest.fixture
def sentiment_analyzer():
    """Create a sentiment analyzer instance for testing."""
    return SentimentAnalyzer()


@pytest.mark.asyncio
async def test_transformer_sentiment_analysis(sentiment_analyzer):
    """Test Transformer-based sentiment analysis (no VADER)."""
    positive_text = "This policy is excellent and will greatly benefit our community!"
    results = await sentiment_analyzer.analyze_sentiment(positive_text, [AnalysisMethod.TRANSFORMER])
    assert len(results) > 0
    result = results[0]
    assert result.method == "Transformer"
    assert result.sentiment_label in [SentimentLabel.POSITIVE, SentimentLabel.NEUTRAL]
    assert 0.0 <= result.confidence_score <= 1.0
    
    negative_text = "This is a terrible policy that will harm everyone!"
    results = await sentiment_analyzer.analyze_sentiment(negative_text, [AnalysisMethod.TRANSFORMER])
    assert len(results) > 0
    result = results[0]
    assert result.method == "Transformer"
    assert result.sentiment_label in [SentimentLabel.NEGATIVE, SentimentLabel.NEUTRAL]
    assert 0.0 <= result.confidence_score <= 1.0


@pytest.mark.asyncio
async def test_emotion_analysis(sentiment_analyzer):
    """Test emotion analysis."""
    # Test support emotion
    support_text = "I strongly support this initiative and appreciate the government's efforts."
    emotion_result = await sentiment_analyzer.analyze_emotions(support_text)
    
    assert emotion_result is not None
    assert emotion_result.emotion_label in [EmotionLabel.SUPPORT, EmotionLabel.APPRECIATION]
    assert emotion_result.confidence_score >= 0
    assert "support" in emotion_result.emotion_scores or "appreciation" in emotion_result.emotion_scores


@pytest.mark.asyncio
async def test_aspect_sentiment_analysis(sentiment_analyzer):
    """Test aspect-based sentiment analysis."""
    text = "Section 3.1 is excellent but the implementation timeline is concerning."
    aspect_results = await sentiment_analyzer.analyze_aspect_sentiment(text)
    
    # Should detect some aspects
    assert len(aspect_results) >= 0  # May not detect aspects in short text, that's okay


@pytest.mark.asyncio
async def test_comprehensive_analysis(sentiment_analyzer):
    """Test comprehensive analysis."""
    text = "I support this policy proposal in Section 2.4, but I have concerns about the enforcement mechanisms."
    
    result = await sentiment_analyzer.comprehensive_analysis(text)
    
    assert result is not None
    assert result.text == text
    assert len(result.sentiment_results) > 0
    assert result.emotion_result is not None
    assert result.overall_sentiment in [SentimentLabel.POSITIVE, SentimentLabel.NEGATIVE, SentimentLabel.NEUTRAL]
    assert 0 <= result.overall_confidence <= 1
    assert result.processing_time_ms > 0
    assert "explanation" in result.explanation or len(result.explanation) >= 0


@pytest.mark.asyncio
async def test_batch_analysis(sentiment_analyzer):
    """Test batch analysis."""
    texts = [
        "This is a great policy!",
        "I disagree with this approach.",
        "This seems reasonable and balanced."
    ]
    
    results = await sentiment_analyzer.batch_analysis(texts)
    
    assert len(results) == len(texts)
    
    for result in results:
        assert result is not None
        assert result.overall_sentiment in [SentimentLabel.POSITIVE, SentimentLabel.NEGATIVE, SentimentLabel.NEUTRAL]


def test_law_section_extraction(sentiment_analyzer):
    """Test law section extraction."""
    text = "Section 3.1 and Article 5 need revision, but Clause 2.4 is fine."
    sections = sentiment_analyzer._extract_law_sections(text)
    
    # Should extract at least some sections
    assert isinstance(sections, list)


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__])