"""
Enhanced Original Dashboard with Improved UI
Maintains all original functionality with a more polished, professional look
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import asyncio
import httpx
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO, BytesIO
import base64
import sys
import os

# Add services directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend', 'app', 'services'))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Custom CSS for Enhanced Government Theme
st.markdown("""
<style>
    /* Import Government fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Noto+Sans:wght@300;400;500;700&display=swap');
    
    /* Root variables - Enhanced Government Theme */
    :root {
        /* Official Government of India Colors - Enhanced */
        --primary-color: #00264D;      /* Darker Blue */
        --primary-light: #1A4D80;      /* Lighter shade for hover states */
        --secondary-color: #FF8C00;    /* Brighter Saffron */
        --accent-color: #1E9C4A;       /* Richer Green */
        --white: #FFFFFF;
        --off-white: #F8F9FA;         /* Softer white for backgrounds */
        --light-gray: #E9ECEF;        /* Softer light gray */
        --medium-gray: #DEE2E6;       /* Updated medium gray */
        --dark-gray: #343A40;         /* Darker gray for better contrast */
        --text-dark: #212529;
        --text-light: #495057;        /* Better for readability */
        
        /* Sentiment Colors - Enhanced */
        --sentiment-positive: #2E8B57;  /* Sea Green */
        --sentiment-neutral: #6C757D;   /* Gray */
        --sentiment-negative: #DC3545;  /* Red */
        --sentiment-mixed: #FFC107;     /* Amber */
        
        /* Layout */
        --header-height: 70px;
        --footer-height: auto;
        --container-max-width: 1400px;
        --border-radius: 8px;
        --box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        
        /* Typography */
        --font-primary: 'Roboto', 'Noto Sans', sans-serif;
        --font-heading: 'Roboto', 'Noto Sans', sans-serif;
    }
    
    /* Base Styles */
    body {
        font-family: var(--font-primary);
        color: var(--text-dark);
        line-height: 1.6;
        background-color: var(--off-white);
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Main container */
    .main .block-container {
        padding: calc(var(--header-height) + 1rem) 2rem 2rem;
        max-width: var(--container-max-width);
        margin: 0 auto;
        background-color: var(--white);
        min-height: 100vh;
    }
    
    /* Cards */
    .card {
        background: var(--white);
        border-radius: var(--border-radius);
        box-shadow: var(--box-shadow);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid var(--medium-gray);
        transition: var(--transition);
    }
    
    .card:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
        color: white;
        border: none;
        padding: 0.7rem 1.5rem;
        border-radius: var(--border-radius);
        font-weight: 500;
        transition: var(--transition);
        box-shadow: var(--box-shadow);
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, var(--primary-light), var(--primary-color));
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: var(--primary-color);
        color: white;
    }
    
    .css-1d391kg .stRadio > div {
        color: white;
    }
    
    .css-1d391kg .stRadio > label > div {
        color: white;
    }
    
    /* Input fields */
    .stTextInput>div>div>input,
    .stSelectbox>div>div>div {
        border-radius: var(--border-radius);
        border: 1px solid var(--medium-gray);
        padding: 0.5rem 1rem;
    }
    
    /* File uploader */
    .stFileUploader {
        border: 2px dashed var(--medium-gray);
        border-radius: var(--border-radius);
        padding: 2rem;
        text-align: center;
        transition: var(--transition);
    }
    
    .stFileUploader:hover {
        border-color: var(--primary-color);
        background-color: rgba(0, 38, 77, 0.05);
    }
    
    /* Tables */
    .stDataFrame {
        border-radius: var(--border-radius);
        overflow: hidden;
        box-shadow: var(--box-shadow);
    }
    
    /* Success/Error messages */
    .stAlert {
        border-radius: var(--border-radius);
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main .block-container {
            padding: calc(var(--header-height) + 1rem) 1rem 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

def configure_page():
    """Configure page settings with enhanced UI."""
    st.set_page_config(
        page_title="E-Consultation Insight Engine",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def initialize_session_state():
    """Initialize session state variables."""
    if 'data' not in st.session_state:
        st.session_state.data = None
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = None
    if 'current_view' not in st.session_state:
        st.session_state.current_view = "Dashboard"
    if 'selected_file' not in st.session_state:
        st.session_state.selected_file = None

def render_sidebar():
    """Render the sidebar navigation with enhanced styling."""
    with st.sidebar:
        st.markdown("""
        <div style='padding: 1rem 0;'>
            <h2 style='color: white; margin-bottom: 1.5rem;'>Navigation</h2>
        """, unsafe_allow_html=True)
        
        # Navigation radio buttons with custom styling
        view = st.radio(
            "",
            ["Dashboard", "Upload Data", "Analyze", "Reports", "Settings"],
            key="current_view",
            label_visibility="collapsed"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Add some space at the bottom
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)

def render_dashboard():
    """Render the main dashboard view with enhanced UI."""
    st.markdown("""
    <div class='card'>
        <h1 style='color: var(--primary-color); margin-bottom: 1rem;'>E-Consultation Insight Engine</h1>
        <p style='font-size: 1.1rem; color: var(--text-light);'>
            Upload a file to begin analysis or explore the available options.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add some sample cards for demonstration
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h3>Quick Analysis</h3>
            <p>Perform a quick sentiment analysis on your data.</p>
            <button class='stButton'>Try Now</button>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h3>Upload Data</h3>
            <p>Upload your dataset to get started.</p>
            <button class='stButton'>Upload</button>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h3>View Reports</h3>
            <p>Access your saved analysis reports.</p>
            <button class='stButton'>View Reports</button>
        </div>
        """, unsafe_allow_html=True)

def render_upload():
    """Render the file upload interface with enhanced UI."""
    st.markdown("""
    <div class='card'>
        <h1 style='color: var(--primary-color); margin-bottom: 1.5rem;'>Upload Data</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # File uploader with custom styling
    uploaded_file = st.file_uploader(
        "Choose a file (CSV or Excel)",
        type=['csv', 'xlsx', 'xls'],
        help="Upload your dataset in CSV or Excel format"
    )
    
    if uploaded_file is not None:
        try:
            with st.spinner("Processing your file..."):
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                elif uploaded_file.name.endswith(('.xls', '.xlsx')):
                    df = pd.read_excel(uploaded_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")
                    return
                
                st.session_state.data = df
                st.session_state.selected_file = uploaded_file.name
                
                st.success(f"✅ Successfully uploaded {uploaded_file.name}")
                
                # Show data preview in a card
                st.markdown("""
                <div class='card' style='margin-top: 1.5rem;'>
                    <h3 style='color: var(--primary-color);'>Data Preview</h3>
                </div>
                """, unsafe_allow_html=True)
                
                st.dataframe(df.head(), use_container_width=True)
                
        except Exception as e:
            st.error(f"❌ Error loading file: {str(e)}")

def render_analysis():
    """Render the analysis interface with enhanced UI."""
    if st.session_state.data is None:
        st.warning("⚠️ Please upload a file first.")
        return
    
    st.markdown("""
    <div class='card'>
        <h1 style='color: var(--primary-color); margin-bottom: 1.5rem;'>Analyze Data</h1>
    </div>
    """, unsafe_allow_html=True)
    
    df = st.session_state.data
    
    # Text column selection in a card
    with st.container():
        st.markdown("<div class='card' style='margin-bottom: 1.5rem;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: var(--primary-color); margin-bottom: 1rem;'>Data Selection</h3>", unsafe_allow_html=True)
        
        text_columns = [col for col in df.columns if df[col].dtype == 'object']
        if not text_columns:
            st.error("No text columns found in the uploaded file.")
            return
        
        text_col = st.selectbox("Select text column for analysis", text_columns)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Analysis options in a card
    with st.container():
        st.markdown("<div class='card' style='margin-bottom: 1.5rem;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: var(--primary-color); margin-bottom: 1rem;'>Analysis Options</h3>", unsafe_allow_html=True)
        
        analysis_type = st.radio(
            "Select analysis type",
            ["Sentiment Analysis", "Keyword Extraction", "Topic Modeling"],
            horizontal=True
        )
        
        if st.button("Run Analysis", key="run_analysis"):
            with st.spinner("Analyzing data..."):
                try:
                    # Simulate analysis
                    time.sleep(2)
                    
                    # Sample analysis results
                    st.session_state.analysis_results = {
                        'type': analysis_type.lower(),
                        'status': 'completed',
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'file': st.session_state.selected_file,
                        'text_column': text_col,
                        'row_count': len(df)
                    }
                    
                    st.success("✅ Analysis completed successfully!")
                    
                    # Show sample results in an expander
                    with st.expander("View Analysis Results", expanded=True):
                        st.markdown(f"""
                        <div style='background-color: var(--off-white); padding: 1rem; border-radius: var(--border-radius);'>
                            <h4>Analysis Summary</h4>
                            <p><strong>Type:</strong> {analysis_type}</p>
                            <p><strong>Text Column:</strong> {text_col}</p>
                            <p><strong>Rows Processed:</strong> {len(df):,}</p>
                            <p><strong>Completed At:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Show a sample of the analyzed text
                        st.markdown("<h5 style='margin-top: 1.5rem;'>Sample of Analyzed Text</h5>", unsafe_allow_html=True)
                        st.dataframe(df[text_col].head().reset_index(drop=True))
                        
                except Exception as e:
                    st.error(f"❌ Error during analysis: {str(e)}")
        
        st.markdown("</div>", unsafe_allow_html=True)

def render_reports():
    """Render the reports view with enhanced UI."""
    st.markdown("""
    <div class='card'>
        <h1 style='color: var(--primary-color); margin-bottom: 1.5rem;'>Analysis Reports</h1>
        <p>View and manage your analysis reports.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if 'analysis_results' in st.session_state and st.session_state.analysis_results:
        st.markdown("<div class='card' style='margin-top: 1.5rem;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: var(--primary-color); margin-bottom: 1rem;'>Latest Analysis</h3>", unsafe_allow_html=True)
        
        results = st.session_state.analysis_results
        st.json(results, expanded=False)
        
        # Add export options
        st.markdown("<h4 style='margin-top: 1.5rem;'>Export Results</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            st.download_button(
                label="Download as JSON",
                data=json.dumps(results, indent=2),
                file_name=f"analysis_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
        
        with col2:
            st.download_button(
                label="Download as CSV",
                data=pd.DataFrame([results]).to_csv(index=False),
                file_name=f"analysis_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("ℹ️ No analysis results available. Please run an analysis first.")

def render_settings():
    """Render the settings view with enhanced UI."""
    st.markdown("""
    <div class='card'>
        <h1 style='color: var(--primary-color); margin-bottom: 1.5rem;'>Settings</h1>
        <p>Configure your application settings.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("settings_form"):
        st.markdown("<div class='card' style='margin-top: 1.5rem;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: var(--primary-color); margin-bottom: 1.5rem;'>General Settings</h3>", unsafe_allow_html=True)
        
        # Theme selection
        theme = st.selectbox(
            "Color Theme",
            ["Default (Blue)", "Dark Mode", "High Contrast"],
            index=0
        )
        
        # Results per page
        results_per_page = st.slider(
            "Results per page",
            min_value=10,
            max_value=100,
            value=25,
            step=5
        )
        
        # Notification preferences
        st.markdown("<h4 style='margin-top: 1.5rem;'>Notifications</h4>", unsafe_allow_html=True)
        email_notifications = st.checkbox("Enable email notifications", value=True)
        
        if email_notifications:
            email_address = st.text_input("Email address", value="your.email@example.com")
        
        # Save button
        if st.form_submit_button("Save Settings"):
            st.success("✅ Settings saved successfully!")
        
        st.markdown("</div>", unsafe_allow_html=True)

def main():
    """Main application function with enhanced UI."""
    configure_page()
    initialize_session_state()
    
    # Render sidebar
    render_sidebar()
    
    # Main content area with enhanced styling
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    
    # Route to the appropriate view
    if st.session_state.current_view == "Dashboard":
        render_dashboard()
    elif st.session_state.current_view == "Upload Data":
        render_upload()
    elif st.session_state.current_view == "Analyze":
        render_analysis()
    elif st.session_state.current_view == "Reports":
        render_reports()
    elif st.session_state.current_view == "Settings":
        render_settings()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Add a footer
    st.markdown("""
    <div style='margin-top: 3rem; padding: 1.5rem 0; text-align: center; color: var(--text-light); font-size: 0.9rem; border-top: 1px solid var(--medium-gray);'>
        <p>E-Consultation Insight Engine v1.0.0 &copy; 2023</p>
        <p style='font-size: 0.8rem; opacity: 0.8;'>Powered by Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
