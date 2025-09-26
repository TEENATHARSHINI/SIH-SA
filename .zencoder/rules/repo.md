# Repository Overview

## Project
- **Name**: E-Consultation Insight Engine (Sentiment)
- **Root**: d:\Sentiment
- **Primary stacks**:
  - **Backend**: FastAPI (Python), JWT auth, optional MongoDB
  - **Dashboard**: Streamlit
  - **NLP**: Transformers (optional fallback), VADER/TextBlob/spaCy (optional), Sumy, custom TextRank

## Key Paths
- **Backend app**: `backend/app`
  - `main.py`: FastAPI app, routers, health endpoints
  - `routers/`: API routers (auth, etc.)
  - `services/`: sentiment, summarization, preprocessing, etc.
  - `core/`: config, security, database
  - `models/`: pydantic models and enums
- **Dashboard**: `dashboard/`
- **Data**: `data/`
- **Tests**: `tests/` (unit + integration)

## Tests
- Run: `d:\Sentiment\.venv\Scripts\pytest.exe -q`
- Focus files: `tests/unit/test_authentication.py`, `tests/unit/test_sentiment_analysis.py`, `tests/unit/test_summarization.py`, `tests/test_health.py`

## Notable Config
- `.env` or `.env.example` and `backend/app/core/config.py`
- Tokens: `backend/app/core/security.py` (uses `settings.SECRET_KEY`, `ALGORITHM`)

## Tips
- If transformers/spacy unavailable, code uses fallbacks to pass tests
- Auth router is enabled in `backend/app/main.py`

## Commands
- Install deps: `d:\Sentiment\install_requirements.bat` (or `pip install -r requirements.txt`)
- Run API: `d:\Sentiment\.venv\Scripts\uvicorn.exe backend.app.main:app --host 0.0.0.0 --port 8000`
- Run tests: `d:\Sentiment\.venv\Scripts\pytest.exe -q`