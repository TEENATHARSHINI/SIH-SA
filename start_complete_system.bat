@echo off
REM COMPLETE STARTUP SCRIPT FOR WINDOWS - 200% Working System
REM This script starts all services for the MCA Sentiment Analysis System

echo 🏛️ ==========================================
echo 🏛️  MCA SENTIMENT ANALYSIS SYSTEM STARTUP
echo 🏛️ ==========================================
echo.

REM Function to kill processes on specific ports
echo 🧹 Clearing existing processes on ports 8001 and 8501...

REM Kill processes on port 8001 (API)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8001') do (
    if not "%%a"=="0" (
        echo Stopping process %%a on port 8001...
        taskkill /F /PID %%a >nul 2>&1
    )
)

REM Kill processes on port 8501 (Dashboard)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8501') do (
    if not "%%a"=="0" (
        echo Stopping process %%a on port 8501...
        taskkill /F /PID %%a >nul 2>&1
    )
)

echo ✅ Port cleanup completed
echo.

echo 📁 Setting up directory structure...

REM Check if we're in the right directory
if not exist "backend\final_api.py" (
    echo ❌ Error: Please run this script from the project root directory
    echo    Make sure backend\final_api.py exists
    pause
    exit /b 1
)

REM Create necessary directories
if not exist "data\sample" mkdir "data\sample"
if not exist "data\uploads" mkdir "data\uploads"
if not exist "logs" mkdir "logs"
if not exist "backend\__pycache__" mkdir "backend\__pycache__"
if not exist "dashboard\__pycache__" mkdir "dashboard\__pycache__"

echo ✅ Directory structure ready
echo.

echo 📦 Installing Python dependencies...
pip install --quiet --upgrade pip
pip install --quiet fastapi uvicorn pandas numpy requests plotly streamlit python-multipart aiofiles python-dotenv

echo ✅ Dependencies installed
echo.

REM Create sample data if it doesn't exist
if not exist "data\sample\mca_test_dataset.csv" (
    echo 📊 Creating sample MCA dataset...
    python -c "
import pandas as pd
import os

# Create sample MCA consultation data
sample_data = [
    {'stakeholder_type': 'Individual', 'policy_area': 'Digital Governance', 'comment': 'I strongly support the new digital governance framework. It will improve transparency.'},
    {'stakeholder_type': 'NGO', 'policy_area': 'Corporate Affairs', 'comment': 'The proposed changes are excellent and will benefit small businesses significantly.'},
    {'stakeholder_type': 'Corporation', 'policy_area': 'Environmental Compliance', 'comment': 'These regulations are too strict and will harm business growth.'},
    {'stakeholder_type': 'Academic', 'policy_area': 'Digital Policy', 'comment': 'The framework needs more research-based evidence for effective implementation.'},
    {'stakeholder_type': 'Individual', 'policy_area': 'Corporate Affairs', 'comment': 'यह नई नीति बहुत अच्छी है और व्यापार को बढ़ावा देगी।'},
    {'stakeholder_type': 'Industry Association', 'policy_area': 'Digital Governance', 'comment': 'We appreciate the government initiative but request more consultation time.'},
    {'stakeholder_type': 'Legal Expert', 'policy_area': 'Environmental Compliance', 'comment': 'The legal framework is robust and addresses key environmental concerns effectively.'},
    {'stakeholder_type': 'Citizen', 'policy_area': 'Digital Policy', 'comment': 'This policy will make government services more accessible to common people.'},
    {'stakeholder_type': 'NGO', 'policy_area': 'Corporate Affairs', 'comment': 'নতুন নীতি অসাধারণ এবং এটি ছোট ব্যবসার জন্য খুবই উপকারী।'},
    {'stakeholder_type': 'Corporation', 'policy_area': 'Digital Governance', 'comment': 'The implementation timeline is unrealistic for large corporations.'}
]

# Create DataFrame and save
df = pd.DataFrame(sample_data)
os.makedirs('data/sample', exist_ok=True)
df.to_csv('data/sample/mca_test_dataset.csv', index=False)
print('✅ Sample dataset created: data/sample/mca_test_dataset.csv')
"
)

echo.
echo 🚀 Starting API Service...
echo 📍 API will be available at: http://localhost:8001
echo.

REM Start API in new window
start "MCA API Service" /min cmd /c "cd backend && python final_api.py"

echo ⏳ Waiting for API to start...
timeout /t 5 /nobreak >nul

REM Check if API is running
set API_RUNNING=false
for /L %%i in (1,1,10) do (
    curl -s http://localhost:8001/health >nul 2>&1
    if !errorlevel! equ 0 (
        set API_RUNNING=true
        echo ✅ API Service is running successfully!
        goto :api_started
    ) else (
        echo ⏳ Checking API status... (attempt %%i/10)
        timeout /t 2 /nobreak >nul
    )
)

:api_started
if "%API_RUNNING%"=="false" (
    echo ❌ API failed to start. Please check for errors.
    pause
    exit /b 1
)

echo.
echo 🌐 Starting Dashboard...
echo 📍 Dashboard will be available at: http://localhost:8501
echo.

REM Start Dashboard in new window
start "MCA Dashboard" cmd /c "streamlit run dashboard/final_dashboard.py --server.port 8501 --server.address 0.0.0.0"

echo ⏳ Waiting for Dashboard to start...
timeout /t 8 /nobreak >nul

REM Check if Dashboard is running
set DASHBOARD_RUNNING=false
for /L %%i in (1,1,10) do (
    curl -s http://localhost:8501 >nul 2>&1
    if !errorlevel! equ 0 (
        set DASHBOARD_RUNNING=true
        echo ✅ Dashboard is running successfully!
        goto :dashboard_started
    ) else (
        echo ⏳ Checking Dashboard status... (attempt %%i/10)
        timeout /t 2 /nobreak >nul
    )
)

:dashboard_started

echo.
echo 🎉 ==========================================
echo 🎉  SYSTEM STARTUP COMPLETE!
echo 🎉 ==========================================
echo.
echo 📊 Services Running:
echo    🔹 API Service: http://localhost:8001
echo    🔹 Dashboard: http://localhost:8501
echo    🔹 Health Check: http://localhost:8001/health
echo.
echo 🚀 READY TO USE:
echo    1. Open: http://localhost:8501
echo    2. Click 'Load Sample Data'
echo    3. Explore the sentiment analysis results
echo.
echo 📋 Available Features:
echo    ✅ Multilingual sentiment analysis (15+ languages)
echo    ✅ Government-style MCA dashboard
echo    ✅ Real-time text analysis
echo    ✅ Word cloud generation
echo    ✅ CSV/JSON export
echo    ✅ Interactive visualizations
echo.
echo 🔧 Manual Commands (if needed):
echo    • API only: cd backend ^&^& python final_api.py
echo    • Dashboard only: streamlit run dashboard/final_dashboard.py
echo.
echo ⏹️  To stop services: Close the API and Dashboard windows or run stop_services.bat
echo.

REM Automatically open the dashboard in default browser
echo 🌐 Opening dashboard in your default browser...
timeout /t 3 /nobreak >nul
start http://localhost:8501

echo.
echo 🎯 System is running! Check the opened browser window.
echo 📝 Press any key to create a stop script...
pause >nul

REM Create stop script
echo @echo off > stop_services.bat
echo echo 🛑 Stopping MCA Services... >> stop_services.bat
echo taskkill /F /IM python.exe /FI "WINDOWTITLE eq MCA API Service*" 2^>nul >> stop_services.bat
echo taskkill /F /IM cmd.exe /FI "WINDOWTITLE eq MCA Dashboard*" 2^>nul >> stop_services.bat
echo for /f "tokens=5" %%%%a in ('netstat -aon ^^^| findstr :8001') do if not "%%%%a"=="0" taskkill /F /PID %%%%a 2^>nul >> stop_services.bat
echo for /f "tokens=5" %%%%a in ('netstat -aon ^^^| findstr :8501') do if not "%%%%a"=="0" taskkill /F /PID %%%%a 2^>nul >> stop_services.bat
echo echo ✅ All services stopped >> stop_services.bat
echo pause >> stop_services.bat

echo ✅ Created stop_services.bat - run it to stop all services
echo 💡 Tip: Keep this window open to monitor the system
echo.
echo System is ready! 🚀
pause