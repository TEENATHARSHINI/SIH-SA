"""
Unit tests for the summarization service.
"""

import pytest
import asyncio
from backend.app.services.summarization_service import (
    SummarizationService, SummarizationType, SummarizationMethod,
    TextRankSummarizer, SummaryResult
)


class TestTextRankSummarizer:
    """Test cases for custom TextRank implementation."""
    
    @pytest.fixture
    def textrank_summarizer(self):
        """Create TextRank summarizer instance."""
        return TextRankSummarizer()
    
    def test_sentence_similarity(self, textrank_summarizer):
        """Test sentence similarity calculation."""
        sent1 = "The new regulation will improve data protection."
        sent2 = "Data protection will be enhanced by the new regulation."
        sent3 = "The weather is nice today."
        
        # Similar sentences should have high similarity
        similarity_high = textrank_summarizer.sentence_similarity(sent1, sent2)
        assert similarity_high > 0.3
        
        # Different sentences should have low similarity
        similarity_low = textrank_summarizer.sentence_similarity(sent1, sent3)
        assert similarity_low < 0.2
    
    def test_summarize_short_text(self, textrank_summarizer):
        """Test summarization of short text."""
        text = "This is a short text. It has only two sentences."
        summary, key_sentences, confidence = textrank_summarizer.summarize(text, num_sentences=3)
        
        # Should return original text for short inputs
        assert summary == text
        assert len(key_sentences) == 2
        assert confidence == 1.0
    
    def test_summarize_long_text(self, textrank_summarizer):
        """Test summarization of longer text."""
        text = """
        The proposed data protection regulation aims to enhance privacy rights for citizens.
        This regulation includes provisions for data collection transparency.
        Companies will be required to implement stronger security measures.
        Penalties for non-compliance will be significantly increased.
        The regulation also addresses cross-border data transfers.
        Implementation timeline spans two years from enactment.
        Stakeholder feedback has been overwhelmingly positive.
        Privacy advocates support the stronger enforcement mechanisms.
        """
        
        summary, key_sentences, confidence = textrank_summarizer.summarize(text, num_sentences=3)
        
        # Should produce a meaningful summary
        assert len(key_sentences) == 3
        assert len(summary) < len(text)
        assert confidence > 0
        assert all(sentence.strip().endswith('.') for sentence in key_sentences)


class TestSummarizationService:
    """Test cases for the summarization service."""
    
    @pytest.fixture
    def summarization_service(self):
        """Create summarization service instance."""
        return SummarizationService()
    
    @pytest.fixture
    def sample_text(self):
        """Sample text for testing."""
        return """
        The proposed legislation introduces significant changes to data privacy regulations.
        These changes aim to strengthen individual privacy rights and enhance data protection.
        Organizations will need to implement new compliance measures within eighteen months.
        The regulation includes provisions for automatic data deletion and consent management.
        Penalties for non-compliance have been increased substantially to ensure effectiveness.
        Cross-border data transfer mechanisms will be subject to stricter oversight.
        The legislation has received broad support from privacy advocacy groups.
        Industry representatives have raised concerns about implementation costs.
        Government officials emphasize the importance of protecting citizen privacy.
        The new framework aligns with international best practices in data protection.
        """
    
    @pytest.fixture
    def sample_comments(self):
        """Sample comments for testing."""
        return [
            "I strongly support this regulation as it protects our privacy rights effectively.",
            "The implementation timeline seems too aggressive for small businesses to comply.",
            "Excellent initiative! This will finally give us control over our personal data.",
            "Concerned about the compliance costs for startups and small companies.",
            "The penalties are appropriate and necessary to ensure organizations take this seriously.",
            "This regulation is long overdue and addresses critical privacy concerns."
        ]
    
    @pytest.mark.asyncio
    async def test_extractive_summarization_textrank(self, summarization_service, sample_text):
        """Test extractive summarization using TextRank."""
        result = await summarization_service.extractive_summarization(
            text=sample_text,
            method=SummarizationMethod.CUSTOM_TEXTRANK,
            num_sentences=3
        )
        
        assert isinstance(result, SummaryResult)
        assert result.method == SummarizationMethod.CUSTOM_TEXTRANK.value
        assert result.summary_type == SummarizationType.EXTRACTIVE
        assert len(result.key_sentences) <= 3
        assert result.compression_ratio < 1.0
        assert result.confidence_score > 0
        assert result.processing_time_ms >= 0
    
    @pytest.mark.asyncio
    async def test_extractive_summarization_sumy(self, summarization_service, sample_text):
        """Test extractive summarization using Sumy TextRank."""
        result = await summarization_service.extractive_summarization(
            text=sample_text,
            method=SummarizationMethod.TEXTRANK,
            num_sentences=2
        )
        
        assert isinstance(result, SummaryResult)
        assert result.method == SummarizationMethod.TEXTRANK.value
        assert result.summary_type == SummarizationType.EXTRACTIVE
        assert len(result.summary_text.strip()) > 0
        assert result.original_length > result.summary_length
    
    @pytest.mark.asyncio
    async def test_abstractive_summarization(self, summarization_service, sample_text):
        """Test abstractive summarization (may fallback if transformers unavailable)."""
        result = await summarization_service.abstractive_summarization(
            text=sample_text,
            method=SummarizationMethod.T5,
            max_length=100,
            min_length=30
        )
        
        assert isinstance(result, SummaryResult)
        assert result.summary_type == SummarizationType.ABSTRACTIVE or "fallback" in result.method
        assert len(result.summary_text.strip()) > 0
        assert result.processing_time_ms >= 0
    
    @pytest.mark.asyncio
    async def test_hybrid_summarization(self, summarization_service, sample_text):
        """Test hybrid summarization."""
        result = await summarization_service.hybrid_summarization(
            text=sample_text,
            extractive_sentences=4,
            abstractive_max_length=80
        )
        
        assert isinstance(result, SummaryResult)
        assert result.summary_type == SummarizationType.HYBRID
        assert len(result.summary_text.strip()) > 0
        assert result.processing_time_ms >= 0
        assert "hybrid" in result.method.lower() or "fallback" in result.method.lower()
    
    @pytest.mark.asyncio
    async def test_summarize_comments(self, summarization_service, sample_comments):
        """Test comment summarization."""
        result = await summarization_service.summarize_comments(
            comments=sample_comments,
            method=SummarizationMethod.CUSTOM_TEXTRANK,
            summary_type=SummarizationType.EXTRACTIVE
        )
        
        assert isinstance(result, SummaryResult)
        assert len(result.summary_text.strip()) > 0
        assert result.metadata["source_type"] == "multiple_comments"
        assert result.metadata["comment_count"] == len(sample_comments)
        assert result.metadata["average_comment_length"] > 0
    
    @pytest.mark.asyncio
    async def test_aggregate_summarization(self, summarization_service):
        """Test aggregate summarization by section."""
        comments_by_section = {
            "Section 1": [
                "This section is well-drafted and addresses key concerns.",
                "I support the provisions in this section.",
                "The requirements seem reasonable and fair."
            ],
            "Section 2": [
                "This section needs clarification on implementation.",
                "Concerned about the timeline specified here.",
                "The penalties in this section are too harsh."
            ],
            "Section 3": [
                "Excellent approach to data protection in this section.",
                "This section aligns with international standards.",
                "Strong support for these privacy measures."
            ]
        }
        
        sentiments_by_section = {
            "Section 1": ["positive", "positive", "positive"],
            "Section 2": ["negative", "negative", "negative"],
            "Section 3": ["positive", "positive", "positive"]
        }
        
        result = await summarization_service.aggregate_summarization(
            comments_by_section=comments_by_section,
            sentiments_by_section=sentiments_by_section
        )
        
        assert len(result.section_summaries) == 3
        assert "Section 1" in result.section_summaries
        assert "Section 2" in result.section_summaries
        assert "Section 3" in result.section_summaries
        
        assert len(result.overall_summary.summary_text) > 0
        assert result.total_comments == 9
        assert "positive" in result.sentiment_distribution
        assert "negative" in result.sentiment_distribution
        assert len(result.key_themes) > 0
        assert result.processing_statistics["sections_processed"] == 3
    
    @pytest.mark.asyncio
    async def test_batch_summarization(self, summarization_service):
        """Test batch summarization."""
        texts = [
            "This is the first document about data privacy regulations and their implications.",
            "The second document discusses implementation challenges for organizations.",
            "Third document covers stakeholder feedback and public consultation results."
        ]
        
        results = await summarization_service.batch_summarization(
            texts=texts,
            method=SummarizationMethod.CUSTOM_TEXTRANK,
            summary_type=SummarizationType.EXTRACTIVE
        )
        
        assert len(results) == len(texts)
        assert all(isinstance(result, SummaryResult) for result in results)
        assert all(len(result.summary_text.strip()) > 0 for result in results)
    
    def test_extract_key_themes_with_spacy(self, summarization_service):
        """Test key theme extraction when spaCy is available."""
        comments = [
            "Data protection is crucial for privacy rights.",
            "Privacy regulations should protect personal information.",
            "Data security measures need improvement.",
            "Personal data protection requires better oversight."
        ]
        
        themes = summarization_service._extract_key_themes(comments, max_themes=5)
        
        assert isinstance(themes, list)
        assert len(themes) > 0
        # Should identify privacy/data-related themes
        theme_text = ' '.join(themes).lower()
        assert any(keyword in theme_text for keyword in ['data', 'privacy', 'protection'])
    
    def test_extract_key_themes_empty_input(self, summarization_service):
        """Test key theme extraction with empty input."""
        themes = summarization_service._extract_key_themes([])
        assert themes == []
    
    @pytest.mark.asyncio
    async def test_error_handling_empty_text(self, summarization_service):
        """Test error handling for empty text."""
        result = await summarization_service.extractive_summarization(
            text="",
            method=SummarizationMethod.CUSTOM_TEXTRANK
        )
        
        # Should handle gracefully with fallback
        assert isinstance(result, SummaryResult)
        assert "fallback" in result.method or result.confidence_score < 1.0
    
    @pytest.mark.asyncio
    async def test_error_handling_very_short_text(self, summarization_service):
        """Test handling of very short text."""
        short_text = "Short."
        result = await summarization_service.extractive_summarization(
            text=short_text,
            method=SummarizationMethod.CUSTOM_TEXTRANK,
            num_sentences=2
        )
        
        assert isinstance(result, SummaryResult)
        assert len(result.summary_text) > 0


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])