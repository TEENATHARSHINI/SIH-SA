# Simplified Sentiment Analysis Engine

A robust, lightweight sentiment analysis system with comprehensive fallback handling and simplified dependencies.

## 🚀 Features

### Core Functionality
- **Sentiment Analysis**: Rule-based sentiment analysis with emotion detection
- **Text Summarization**: Extractive, abstractive, and hybrid summarization
- **Topic-Based Summarization**: Focus on specific topics in text
- **Word Cloud Generation**: Visual representation of text content
- **Sentiment-Tagged Word Clouds**: Words colored by sentiment

### Key Advantages
- ✅ **No Heavy Dependencies**: Works with minimal Python packages
- ✅ **Robust Fallbacks**: Graceful degradation when libraries are missing
- ✅ **Fast Processing**: Lightweight algorithms for quick analysis
- ✅ **Comprehensive API**: RESTful endpoints for all features
- ✅ **Error Handling**: Detailed error messages and status reporting

## 📦 Installation

### Basic Setup (Recommended)
```bash
# Clone or navigate to your project directory
cd /path/to/your/project

# Install basic dependencies
pip install fastapi uvicorn pydantic python-dotenv

# Optional: Install visualization dependencies
pip install matplotlib wordcloud

# Optional: Install advanced NLP dependencies
pip install transformers torch spacy nltk
```

### Full Setup (All Features)
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Quick Start

### 1. Start the Simplified API Server
```bash
# Run the simplified server
python -m backend.app.main_simplified

# Or with custom settings
HOST=0.0.0.0 PORT=8000 DEBUG=true python -m backend.app.main_simplified
```

### 2. Test the System
```bash
# Run comprehensive tests
python test_simplified_system.py
```

### 3. API Usage Examples

#### Sentiment Analysis
```python
import requests

response = requests.post("http://localhost:8000/api/v1/analyze-text", json={
    "text": "I love this new policy! It's amazing and will help everyone."
})

result = response.json()
print(f"Sentiment: {result['overall_sentiment']}")
print(f"Confidence: {result['overall_confidence']}")
```

#### Text Summarization
```python
response = requests.post("http://localhost:8000/api/v1/summarize-text", json={
    "text": "Your long text here...",
    "summary_type": "extractive",
    "num_sentences": 3
})

result = response.json()
print(f"Summary: {result['summary_text']}")
```

#### Topic-Based Summarization
```python
response = requests.post("http://localhost:8000/api/v1/summarize-topic", json={
    "text": "Your long text here...",
    "topics": ["environment", "policy", "economy"],
    "max_length": 150
})

result = response.json()
print(f"Topic Summary: {result['summary_text']}")
```

#### Word Cloud Generation
```python
response = requests.post("http://localhost:8000/api/v1/wordcloud", json={
    "texts": ["Text 1", "Text 2", "Text 3"],
    "max_words": 50
})

result = response.json()
# Save base64 image
with open("wordcloud.png", "wb") as f:
    f.write(base64.b64decode(result['image_base64']))
```

## 📊 API Endpoints

### Core Endpoints
- `GET /api/v1/health` - Health check and service status
- `POST /api/v1/analyze-text` - Sentiment analysis
- `POST /api/v1/summarize-text` - Text summarization
- `POST /api/v1/summarize-topic` - Topic-based summarization
- `POST /api/v1/wordcloud` - Basic word cloud
- `POST /api/v1/sentiment-wordcloud` - Sentiment-tagged word cloud

### Request/Response Examples

#### Health Check
```bash
curl http://localhost:8000/api/v1/health
```
Response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00Z",
  "version": "1.0.0",
  "services": {
    "sentiment": true,
    "summarization": true,
    "visualization": true
  }
}
```

## 🧪 Testing

### Automated Testing
```bash
# Run comprehensive system tests
python test_simplified_system.py
```

### Manual Testing
```bash
# Test individual components
python -c "
import asyncio
from backend.app.services.simplified_sentiment_service import SimplifiedSentimentAnalyzer

async def test():
    analyzer = SimplifiedSentimentAnalyzer()
    result = await analyzer.comprehensive_analysis('This is amazing!')
    print(f'Sentiment: {result.overall_sentiment}')
    print(f'Confidence: {result.overall_confidence}')

asyncio.run(test())
"
```

## 🏗️ Architecture

### Service Layer
```
backend/app/services/
├── simplified_sentiment_service.py     # Rule-based sentiment analysis
├── simplified_summarization_service.py  # TextRank + rule-based summarization
└── simplified_visualization_service.py  # Word clouds with fallbacks
```

### API Layer
```
backend/app/
├── main_simplified.py                  # Simplified FastAPI application
└── routers/                            # Optional: Additional route handlers
```

### Key Design Principles
1. **Graceful Degradation**: Services work even when dependencies are missing
2. **Lightweight Algorithms**: Fast processing without heavy ML models
3. **Comprehensive Logging**: Detailed error reporting and debugging
4. **Modular Design**: Easy to extend and customize
5. **Fallback Strategies**: Multiple approaches for each feature

## 🔧 Configuration

### Environment Variables
```bash
# Server configuration
HOST=0.0.0.0
PORT=8000
DEBUG=true

# Optional: Language detection
DEFAULT_LANGUAGE=en
```

### Service Configuration
Each service can be configured independently:
- **Sentiment Service**: Customizable positive/negative word lists
- **Summarization Service**: Adjustable similarity thresholds
- **Visualization Service**: Configurable image sizes and colors

## 🚀 Performance

### Benchmarks (Approximate)
- **Sentiment Analysis**: ~1-5ms per text
- **Text Summarization**: ~10-50ms per document
- **Word Cloud Generation**: ~50-200ms per request
- **Memory Usage**: ~50-100MB baseline

### Scaling Considerations
- **Concurrent Requests**: Handles 100+ concurrent connections
- **Text Length**: Optimized for texts up to 10,000 characters
- **Batch Processing**: Efficient for multiple texts per request

## 🛠️ Troubleshooting

### Common Issues

#### 1. Import Errors
```
Error: ModuleNotFoundError
```
**Solution**: Install missing dependencies
```bash
pip install fastapi uvicorn pydantic
```

#### 2. Service Unavailable
```
HTTP 503: Service Unavailable
```
**Solution**: Check service initialization
```bash
# Check service status
curl http://localhost:8000/api/v1/health
```

#### 3. Word Cloud Generation Fails
**Cause**: Missing matplotlib or wordcloud
**Solution**: Install optional dependencies or use text fallback
```bash
pip install matplotlib wordcloud
```

#### 4. Slow Performance
**Cause**: Large texts or many concurrent requests
**Solution**: Reduce text length or implement request queuing

### Debug Mode
Enable detailed logging:
```bash
DEBUG=true python -m backend.app.main_simplified
```

## 🔄 Migration from Advanced Version

### What Changes
1. **Simplified Algorithms**: Rule-based instead of ML models
2. **Reduced Dependencies**: Minimal package requirements
3. **Better Error Handling**: Graceful fallbacks for missing libraries
4. **Faster Startup**: Quick initialization without model loading

### Compatibility
- ✅ **API Compatible**: Same endpoints and request formats
- ✅ **Response Format**: Identical JSON response structure
- ⚠️ **Accuracy**: May be slightly lower for complex texts
- ✅ **Performance**: Generally faster for basic tasks

### When to Use Advanced Version
- High-volume processing (>1000 texts/day)
- Complex multilingual content
- Maximum accuracy requirements
- Advanced NLP features needed

## 📈 Future Enhancements

### Planned Features
- [ ] Caching layer for repeated requests
- [ ] Batch processing optimization
- [ ] Advanced emotion detection
- [ ] Custom model training support
- [ ] Real-time streaming analysis
- [ ] Integration with external APIs

### Contributing
1. Fork the repository
2. Create a feature branch
3. Add comprehensive tests
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Support

For issues and questions:
1. Check the troubleshooting section above
2. Run the test suite: `python test_simplified_system.py`
3. Review the API documentation at `/docs`
4. Check the logs for detailed error messages

---

**🎯 Ready to get started?**
```bash
# Quick start
pip install fastapi uvicorn pydantic
python -m backend.app.main_simplified

# Visit http://localhost:8000/docs for API documentation
```