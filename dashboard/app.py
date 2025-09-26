"""
E-Consultation Insight Engine - Main Application
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
import os
import sys

# Add services directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend', 'app', 'services'))

# Page Configuration
st.set_page_config(
    page_title="E-Consultation Insight Engine",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = None
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None
if 'current_view' not in st.session_state:
    st.session_state.current_view = "Dashboard"
if 'selected_file' not in st.session_state:
    st.session_state.selected_file = None

# Sidebar Navigation
with st.sidebar:
    st.title("Navigation")
    st.radio(
        "Go to",
        ["Dashboard", "Upload Data", "Analyze", "Reports", "Settings"],
        key="current_view"
    )

# Main Content Area
if st.session_state.current_view == "Dashboard":
    st.title("E-Consultation Insight Engine")
    st.write("Welcome to the E-Consultation Insight Engine. Upload a file to begin analysis or explore the available options.")
    
    # Add some sample visualizations or instructions
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Getting Started")
        st.markdown("""
        1. Go to **Upload Data** to upload your dataset
        2. Navigate to **Analyze** to perform analysis
        3. View results in the **Reports** section
        """)
    
    with col2:
        st.subheader("Supported File Types")
        st.markdown("""
        - CSV files (.csv)
        - Excel files (.xls, .xlsx)
        """)

elif st.session_state.current_view == "Upload Data":
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
                st.stop()
            
            st.session_state.data = df
            st.session_state.selected_file = uploaded_file.name
            st.success(f"Successfully uploaded {uploaded_file.name}")
            
            # Show data preview
            st.subheader("Data Preview")
            st.dataframe(df.head())
            
        except Exception as e:
            st.error(f"Error loading file: {str(e)}")

elif st.session_state.current_view == "Analyze":
    st.title("Analyze Data")
    
    if st.session_state.data is None:
        st.warning("Please upload a file first.")
    else:
        df = st.session_state.data
        
        # Text column selection
        text_columns = [col for col in df.columns if df[col].dtype == 'object']
        if not text_columns:
            st.error("No text columns found in the uploaded file.")
        else:
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
                            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            'column_analyzed': text_col,
                            'total_rows': len(df)
                        }
                        st.success("Analysis completed successfully!")
                        
                        # Show sample results
                        st.subheader("Analysis Results")
                        st.json(st.session_state.analysis_results)
                        
                    except Exception as e:
                        st.error(f"Error during analysis: {str(e)}")

elif st.session_state.current_view == "Reports":
    st.title("Reports")
    
    if st.session_state.analysis_results:
        st.subheader("Latest Analysis Report")
        st.json(st.session_state.analysis_results)
        
        # Add some sample visualizations
        if st.session_state.data is not None:
            st.subheader("Data Distribution")
            df = st.session_state.data
            
            # Show basic statistics
            st.write("### Basic Statistics")
            st.write(df.describe())
            
            # Show column distribution
            st.write("### Column Distribution")
            col = st.selectbox("Select column to visualize", df.columns)
            
            if df[col].dtype in ['int64', 'float64']:
                fig = px.histogram(df, x=col, title=f"Distribution of {col}")
                st.plotly_chart(fig, use_container_width=True)
            else:
                value_counts = df[col].value_counts().nlargest(10)
                fig = px.bar(
                    x=value_counts.index.astype(str),
                    y=value_counts.values,
                    title=f"Top 10 values in {col}"
                )
                st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No analysis results available. Please run an analysis first.")

elif st.session_state.current_view == "Settings":
    st.title("Settings")
    st.write("Configure your application settings here.")
    
    # Add some sample settings
    st.subheader("Appearance")
    theme = st.selectbox("Theme", ["Light", "Dark", "System Default"])
    
    st.subheader("Data")
    if st.button("Clear All Data"):
        st.session_state.data = None
        st.session_state.analysis_results = None
        st.session_state.selected_file = None
        st.rerun()

# Add footer
st.sidebar.markdown("---")
st.sidebar.info(
    "E-Consultation Insight Engine v1.0\n\n"
    "For support, contact your system administrator."
)
