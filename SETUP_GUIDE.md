# Sentiment Analysis Platform - Setup Guide

## Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account (or local MongoDB instance)
- Git (optional, for version control)

## Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd Sentiment
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   .\install_requirements.bat
   ```
   This will install all required Python packages and create necessary directories.

## Database Setup

1. **Configure MongoDB**:
   - Make sure your MongoDB Atlas connection string is set in the `.env` file
   - The connection string should look like:
     ```
     MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-address>/<database>?retryWrites=true&w=majority
     MONGODB_DB=sentiment_analysis
     ```

2. **Initialize the database**:
   ```bash
   .\init_database.bat
   ```
   This will create the necessary collections and insert sample data.

## Running the Application

1. **Start the backend API** (in a terminal):
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`
   - API documentation: `http://localhost:8000/docs`
   - Health check: `http://localhost:8000/health`

2. **Start the Streamlit dashboard** (in a new terminal):
   ```bash
   cd dashboard
   streamlit run main.py
   ```
   The dashboard will open in your default browser at `http://localhost:8501`

## Default Credentials

A default admin user is created during database initialization:
- **Email**: admin@example.com
- **Password**: secret

## Security Notes

1. **Change the default admin password** after first login
2. **Never commit sensitive data** (passwords, API keys) to version control
3. **Use environment variables** for all sensitive configuration

## Troubleshooting

1. **Connection issues**:
   - Verify your MongoDB Atlas IP whitelist includes your current IP
   - Check that the connection string in `.env` is correct

2. **Python package issues**:
   - Make sure you're using the correct Python version
   - Try recreating the virtual environment

3. **Port conflicts**:
   - The backend runs on port 8000 by default
   - The frontend runs on port 8501 by default
   
   If these ports are in use, you can change them in the respective configuration files.

## Support

For additional help, please contact [Your Support Email] or open an issue in the repository.
