# E-Consultation Insight Engine

A comprehensive sentiment analysis and visualization suite for analyzing stakeholder comments on draft legislation and policy consultations.

![Python](https://img.shields.io/badge/python-v3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.112.0-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.49.1-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

### 🔍 **Advanced Sentiment Analysis**
- **Multi-Algorithm Analysis**: VADER, TextBlob, and Ensemble methods
- **Emotion Classification**: Support, concern, suggestion, anger, appreciation, confusion
- **Aspect-Based Analysis**: Sentiment analysis for specific law sections and topics
- **Confidence Scoring**: Reliability metrics for all analysis results

### 📝 **Text Summarization**
- **Extractive Summarization**: Custom TextRank implementation
- **Abstractive Summarization**: Transformer-based text generation (T5, BART)
- **Hybrid Approach**: Combined extractive and abstractive methods
- **Multi-Document Summarization**: Aggregate summaries across multiple comments

### 🌍 **Multilingual Support**
- **English**: Full NLP pipeline with advanced processing
- **Hindi**: Basic support with language detection
- **Auto-Detection**: Automatic language identification
- **Text Normalization**: Consistent text preprocessing

### 📊 **Interactive Visualizations**
- **Real-time Charts**: Sentiment distribution, emotion analysis
- **Word Clouds**: Visual representation of key terms
- **Time-series Analysis**: Sentiment trends over time
- **Geographic Mapping**: Comment distribution by region (if available)

### 🔐 **Security & Access Control**
- **JWT Authentication**: Secure token-based authentication
- **Role-Based Access**: Admin, Staff, and Guest user roles
- **Data Privacy**: Anonymization and secure data handling
- **Audit Logging**: Comprehensive activity tracking

### 📁 **Data Processing**
- **Multiple Formats**: CSV, Excel, JSON, and plain text files
- **Batch Processing**: Handle thousands of comments efficiently
- **Data Validation**: Quality checks and error handling
- **Deduplication**: Automatic duplicate comment detection

## 🏗️ Architecture

```
E-Consultation Insight Engine/
│
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── core/              # Configuration, database, security
│   │   ├── models/            # SQLAlchemy data models
│   │   ├── routers/           # API endpoints
│   │   ├── services/          # Business logic
│   │   └── utils/             # Utility functions
│   └── main.py                # Application entry point
│
├── dashboard/                  # Streamlit Frontend
│   ├── components/            # UI components
│   └── main.py                # Dashboard entry point
│
├── tests/                     # Test suites
│   ├── unit/                  # Unit tests
│   └── integration/           # Integration tests
│
├── data/                      # Data storage
│   ├── sample/                # Sample datasets
│   ├── uploads/               # User uploads
│   └── processed/             # Processed data
│
└── docs/                      # Documentation
    ├── api/                   # API documentation
    └── user/                  # User guides
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.12+**
- **pip** (Python package manager)
- **Git** (for cloning the repository)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-org/e-consultation-insight-engine.git
cd e-consultation-insight-engine
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download NLP models**
```bash
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running the Application

1. **Start the Backend API**
```bash
cd backend
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

2. **Start the Dashboard** (in a new terminal)
```bash
streamlit run dashboard/main.py --server.port 8501
```

3. **Access the applications**
- **API Documentation**: http://localhost:8000/docs
- **Interactive Dashboard**: http://localhost:8501

## 📖 Usage Guide

### 1. **User Registration & Login**
- Register a new account or use demo credentials
- Role-based access determines available features
- JWT tokens provide secure session management

### 2. **Data Upload**
- Support for CSV, Excel, JSON, and text files
- Automatic file validation and preview
- Batch processing for large datasets

### 3. **Running Analysis**
- Single text analysis for individual comments
- Batch analysis for multiple documents
- Configurable analysis parameters

### 4. **Viewing Results**
- Interactive charts and visualizations
- Detailed sentiment breakdowns
- Export options for further analysis

### 5. **Advanced Features**
- Text summarization with multiple methods
- Key phrase extraction and analysis
- Administrative tools and system monitoring

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Application Settings
APP_NAME="E-Consultation Insight Engine"
DEBUG=false
HOST=127.0.0.1
PORT=8000

# Security
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database
DATABASE_URL=sqlite:///./sentiment_engine.db

# File Upload
MAX_UPLOAD_SIZE=52428800  # 50MB
UPLOAD_DIR=data/uploads

# NLP Settings
SPACY_MODEL=en_core_web_sm
SUPPORTED_LANGUAGES=["en", "hi"]
```

### Database Configuration

The application uses SQLite by default but can be configured for PostgreSQL:

```env
# PostgreSQL (production)
DATABASE_URL=postgresql://user:password@localhost/sentiment_engine
```

## 📊 API Documentation

### Authentication Endpoints

- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/me` - Get current user info
- `POST /api/v1/auth/refresh` - Refresh access token

### Analysis Endpoints

- `POST /api/v1/analysis/analyze` - Single text analysis
- `POST /api/v1/analysis/batch` - Batch text analysis
- `POST /api/v1/analysis/comprehensive` - Complete analysis suite

### Summarization Endpoints

- `POST /api/v1/summarization/text` - Text summarization
- `POST /api/v1/summarization/comments` - Comment summarization
- `POST /api/v1/summarization/aggregate` - Multi-document summarization

### Data Endpoints

- `POST /api/v1/ingestion/upload` - File upload
- `GET /api/v1/health` - System health check

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=backend/app tests/

# Run specific test file
pytest tests/unit/test_sentiment_analysis.py -v
```

### Test Categories

- **Unit Tests**: Individual component testing
- **Integration Tests**: API endpoint testing
- **Performance Tests**: Load and stress testing

## 🔍 Analysis Methods

### Sentiment Analysis Algorithms

1. **VADER (Valence Aware Dictionary and sEntiment Reasoner)**
   - Rule-based sentiment analysis
   - Optimized for social media text
   - Handles emojis, slang, and intensifiers

2. **TextBlob**
   - Pattern-based sentiment analysis
   - Provides polarity and subjectivity scores
   - Good for formal text analysis

3. **Ensemble Method**
   - Combines multiple algorithms
   - Weighted average approach
   - Improved accuracy and robustness

### Emotion Classification

- **Support**: Expressions of agreement and endorsement
- **Concern**: Worries, doubts, and reservations
- **Suggestion**: Recommendations and proposals
- **Anger**: Strong negative emotions and objections
- **Appreciation**: Gratitude and positive acknowledgment
- **Confusion**: Requests for clarification

### Summarization Techniques

1. **Extractive Summarization**
   - Selects important sentences from original text
   - Custom TextRank implementation
   - Preserves original meaning and context

2. **Abstractive Summarization**
   - Generates new summary text
   - Uses transformer models (T5, BART)
   - More natural and concise summaries

## 🛠️ Development

### Setting up Development Environment

1. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install development dependencies**
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

3. **Set up pre-commit hooks**
```bash
pre-commit install
```

### Code Style

- **Python**: PEP 8 compliance with Black formatter
- **Import Sorting**: isort for consistent import organization
- **Linting**: flake8 for code quality checks
- **Type Hints**: mypy for static type checking

### Contributing Guidelines

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Ensure all tests pass
5. Submit a pull request

## 🔧 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Install missing dependencies
pip install -r requirements.txt

# Download NLP models
python -m spacy download en_core_web_sm
```

**2. Database Connection Issues**
```bash
# Reset database
rm sentiment_engine.db
python -c "from backend.app.core.database import create_tables; create_tables()"
```

**3. Port Already in Use**
```bash
# Kill existing processes
lsof -ti:8000 | xargs kill -9  # Backend
lsof -ti:8501 | xargs kill -9  # Dashboard
```

**4. Memory Issues with Large Files**
- Increase batch size settings
- Use streaming for very large datasets
- Monitor system resources

### Performance Optimization

- **Database**: Use PostgreSQL for production
- **Caching**: Enable Redis for better performance
- **Batch Processing**: Optimize batch sizes for your hardware
- **Load Balancing**: Use multiple worker processes

## 📚 Resources

### Documentation Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [spaCy Documentation](https://spacy.io/usage)
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)

### Academic References

- Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.
- Mihalcea, R. & Tarau, P. (2004). TextRank: Bringing Order into Texts.
- Liu, B. (2012). Sentiment Analysis and Opinion Mining.

## 🤝 Support

### Getting Help

- **Documentation**: Check the `/docs` directory
- **Issues**: GitHub Issues for bug reports
- **Discussions**: GitHub Discussions for questions
- **Email**: support@econsultation.gov

### Commercial Support

For enterprise deployments and custom features:
- **Email**: enterprise@econsultation.gov
- **Phone**: +1-800-CONSULT

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- VADER Sentiment Analysis team
- spaCy NLP library contributors
- Streamlit community
- FastAPI framework developers
- All open-source contributors

---

## 📈 Roadmap

### Version 1.1 (Planned)
- [ ] Multi-language sentiment models
- [ ] Advanced visualization options
- [ ] Real-time analysis streaming
- [ ] Mobile-responsive dashboard

### Version 1.2 (Future)
- [ ] Machine learning model training
- [ ] Advanced analytics and insights
- [ ] Integration with external systems
- [ ] Enterprise security features

---

**Built with ❤️ for transparent governance and citizen engagement**

## Advanced Features

### Emotion Detection

- Identify specific emotions in text (joy, sadness, anger, fear, surprise, disgust)
- Emotion intensity scoring
- Emotion distribution visualization

### Aspect-based Analysis

- Extract key aspects from text
- Analyze sentiment for each aspect
- Visualize aspect relationships

### Sarcasm Detection

- Identify sarcastic or ironic statements
- Helps prevent misinterpretation of sentiment

### Real-time Analytics

- Interactive dashboards with live updates
- Real-time sentiment analysis and visualization

### Custom Model Training

- Fine-tune models on your specific domain
- Improve accuracy and robustness

## Using Advanced Features

### Emotion Detection

1. Navigate to the dashboard
2. Enter your text or upload a file
3. Click on "Emotion Detection" in the sidebar
4. View emotion intensity scores and distribution

### Aspect-based Analysis

1. Navigate to the dashboard
2. Enter your text or upload a file
3. Click on "Aspect-based Analysis" in the sidebar
4. View sentiment analysis for each aspect

### Sarcasm Detection

1. Navigate to the dashboard
2. Enter your text or upload a file
3. Click on "Sarcasm Detection" in the sidebar
4. View identified sarcastic or ironic statements

### Real-time Analytics

1. Navigate to the dashboard
2. Enter your text or upload a file
3. Click on "Real-time Analytics" in the sidebar
4. View live updates and sentiment analysis

### Custom Model Training

1. Navigate to the dashboard
2. Click on "Custom Model Training" in the sidebar
3. Upload your dataset and configure training parameters
4. Train and deploy your custom model