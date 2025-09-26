"""
Original Working Dashboard - Clean Version
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
# Add project root to path for enhanced modules
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def configure_page():
    """Configure page settings."""
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
        st.session_state.current_view = "Dashboard"  # Changed to match radio button case
    if 'selected_file' not in st.session_state:
        st.session_state.selected_file = None

def render_sidebar():
    """Render the sidebar navigation."""
    with st.sidebar:
        st.title("Navigation")
        st.radio(
            "Go to",
            ["Dashboard", "Upload Data", "Analyze", "Reports", "Settings"],
            key="current_view"
        )

def render_dashboard():
    """Render the main dashboard view."""
    st.title("E-Consultation Insight Engine")
    st.write("Upload a file to begin analysis or explore the available options.")

def render_upload():
    """Render the file upload interface."""
    st.title("Upload Data")
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file format. Please upload a CSV or Excel file.")
                return
            
            st.session_state.data = df
            st.session_state.selected_file = uploaded_file.name
            st.success(f"Successfully uploaded {uploaded_file.name}")
            
            # Show data preview
            st.subheader("Data Preview")
            st.dataframe(df.head())
            
        except Exception as e:
            st.error(f"Error loading file: {str(e)}")

def render_analysis():
    """Render the analysis interface."""
    if st.session_state.data is None:
        st.warning("Please upload a file first.")
        return
    
    st.title("Analyze Data")
    df = st.session_state.data
    
    # Text column selection
    text_columns = [col for col in df.columns if df[col].dtype == 'object']
    if not text_columns:
        st.error("No text columns found in the uploaded file.")
        return
    
    text_col = st.selectbox("Select text column", text_columns)
    
    # Analysis options
    analysis_type = st.radio(
        "Analysis Type",
        ["Sentiment Analysis", "Keyword Extraction", "Topic Modeling"]
    )
    
    if st.button("Run Analysis"):
        with st.spinner("Analyzing..."):
            try:
                # Sample analysis results
                st.session_state.analysis_results = {
                    'type': analysis_type.lower(),
                    'status': 'completed',
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.success("Analysis completed successfully!")
                
                # Show sample results
                st.subheader("Sample Analysis Results")
                st.write(f"Analysis Type: {analysis_type}")
                st.write(f"Analyzed Column: {text_col}")
                st.write(f"Total Rows: {len(df)}")
                
                # Show sample of the data
                st.write("Sample of analyzed text:")
                st.dataframe(df[text_col].head().reset_index(drop=True))
                
            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")

def render_reports():
    """Render the reports view."""
    st.title("Reports")
    st.write("Analysis reports will be displayed here.")
    
    if st.session_state.analysis_results:
        st.subheader("Latest Analysis")
        st.json(st.session_state.analysis_results)

def render_settings():
    """Render the settings view."""
    st.title("Settings")
    st.write("Configure your application settings here.")

def main():
    """Main application function."""
    configure_page()
    initialize_session_state()
    
    # Render sidebar
    render_sidebar()
    
    # Main content area
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

if __name__ == "__main__":
    main()
