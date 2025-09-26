"""
E-Consultation Insight Engine - Restored Version
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
        st.session_state.current_view = "Dashboard"
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
    st.write("Welcome to the E-Consultation platform. Use the sidebar to navigate.")
    
    if st.session_state.data is not None:
        st.success(f"File loaded: {st.session_state.selected_file}")
        st.dataframe(st.session_state.data.head())

def render_upload():
    """Render the file upload interface."""
    st.title("Upload Data")
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:  # Excel file
                df = pd.read_excel(uploaded_file)
                
            st.session_state.data = df
            st.session_state.selected_file = uploaded_file.name
            st.success("File uploaded successfully!")
            
            # Show data preview
            st.subheader("Data Preview")
            st.dataframe(df.head())
            
        except Exception as e:
            st.error(f"Error loading file: {str(e)}")

def render_analysis():
    """Render the analysis interface."""
    if st.session_state.data is None:
        st.warning("Please upload a file first from the 'Upload Data' section.")
        return
    
    st.title("Analyze Data")
    df = st.session_state.data
    
    # Show basic stats
    st.subheader("Data Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", len(df))
    col2.metric("Total Columns", len(df.columns))
    
    # Column selection for analysis
    text_columns = [col for col in df.columns if df[col].dtype == 'object']
    if not text_columns:
        st.warning("No text columns found for analysis.")
        return
    
    selected_column = st.selectbox("Select text column for analysis", text_columns)
    
    if st.button("Run Basic Analysis"):
        with st.spinner("Analyzing..."):
            try:
                # Sample analysis (you can replace this with your actual analysis)
                word_counts = df[selected_column].str.split().str.len()
                char_counts = df[selected_column].str.len()
                
                # Show basic stats
                st.subheader("Text Analysis Results")
                st.write(f"Analyzing column: **{selected_column}**")
                
                # Create columns for metrics
                col1, col2, col3 = st.columns(3)
                col1.metric("Average Word Count", f"{word_counts.mean():.1f}")
                col2.metric("Average Character Count", f"{char_counts.mean():.1f}")
                col3.metric("Unique Values", df[selected_column].nunique())
                
                # Show sample of the data
                st.subheader("Sample Data")
                st.dataframe(df[[selected_column]].head())
                
                # Save results to session state
                st.session_state.analysis_results = {
                    'column_analyzed': selected_column,
                    'avg_word_count': word_counts.mean(),
                    'avg_char_count': char_counts.mean(),
                    'unique_values': df[selected_column].nunique(),
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")

def render_reports():
    """Render the reports view."""
    st.title("Analysis Reports")
    
    if 'analysis_results' not in st.session_state or st.session_state.analysis_results is None:
        st.info("No analysis results available. Please run an analysis first.")
        return
    
    st.subheader("Latest Analysis Results")
    results = st.session_state.analysis_results
    
    # Display results in a nice format
    st.json(results)
    
    # Option to download results
    if st.button("Download Results as JSON"):
        json_str = json.dumps(results, indent=4)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name=f"analysis_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )

def render_settings():
    """Render the settings view."""
    st.title("Settings")
    
    # Theme selection
    st.subheader("Appearance")
    theme = st.selectbox("Theme", ["Light", "Dark", "System Default"])
    
    # Data management
    st.subheader("Data Management")
    if st.button("Clear All Data"):
        st.session_state.clear()
        st.rerun()
    
    st.info("Note: Clearing data will remove all uploaded files and analysis results.")

def main():
    """Main application function."""
    # Configure page
    configure_page()
    
    # Initialize session state
    if 'initialized' not in st.session_state:
        initialize_session_state()
        st.session_state.initialized = True
    
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
