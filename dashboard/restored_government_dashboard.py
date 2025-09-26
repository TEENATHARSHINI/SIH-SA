"""
MCA eConsultation Sentiment Analysis Dashboard
Government-style UI with MCA21 portal aesthetic
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json
from datetime import datetime, timedelta
import base64
from io import BytesIO
import time
import numpy as np
from collections import Counter
import re

# Page configuration
st.set_page_config(
    page_title="MCA Sentiment Analysis Dashboard",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Government aesthetic
st.markdown("""
<style>
    /* Import Government fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Noto+Sans:wght@300;400;500;700&display=swap');
    
    /* Root variables - Enhanced Government Theme */
    :root {
        /* Official Government of India Colors - Enhanced */
        --primary-color: #00264D;      /* Darker Blue for better contrast */
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
        
        /* New Variables */
        --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        --transition: all 0.3s ease;
        --border-radius: 8px;
        --card-padding: 1.5rem;
    }
    
    /* Global Styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Roboto', 'Noto Sans', sans-serif;
    }
    
    body {
        background-color: var(--light-gray);
        color: var(--text-dark);
        line-height: 1.6;
    }
    
    /* Header Styles - Enhanced */
    .header {
        background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
        color: white;
        padding: 0.8rem 0;
        box-shadow: var(--box-shadow);
        border-bottom: 4px solid var(--secondary-color);
        position: sticky;
        top: 0;
        z-index: 1000;
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
    }
    
    .header-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .logo {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .logo img {
        height: 50px;
    }
    
    .logo-text h1 {
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0;
        line-height: 1.2;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        letter-spacing: 0.5px;
    }
    
    .logo-text p {
        font-size: 0.9rem;
        opacity: 0.9;
        margin: 0;
    }
    
    /* Navigation */
    .main-nav {
        background-color: var(--primary-color);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    
    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    .nav-menu {
        display: flex;
        list-style: none;
        margin: 0;
        padding: 0;
    }
    
    .nav-menu li {
        position: relative;
    }
    
    .nav-menu a {
        display: block;
        color: white;
        text-decoration: none;
        padding: 0.8rem 1.2rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .nav-menu a:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    .nav-menu a.active {
        background-color: var(--secondary-color);
        color: var(--primary-color);
        font-weight: 600;
    }
    
    /* Main Content */
    .main-container {
        max-width: 1200px;
        margin: 2rem auto;
        padding: 0 1rem;
    }
    
    /* Cards - Enhanced */
    .card {
        background: var(--white);
        border-radius: var(--border-radius);
        box-shadow: var(--box-shadow);
        margin-bottom: 1.5rem;
        overflow: hidden;
        border: 1px solid var(--medium-gray);
        transition: var(--transition);
    }
    
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .card-header {
        background: var(--primary-color);
        color: white;
        padding: 0.8rem 1.2rem;
        font-weight: 500;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .card-body {
        padding: 1.2rem;
    }
    
    /* Buttons */
    /* Buttons - Enhanced */
    .btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: 500;
        text-align: center;
        white-space: nowrap;
        vertical-align: middle;
        user-select: none;
        border: 2px solid transparent;
        padding: 0.6rem 1.2rem;
        font-size: 0.9rem;
        line-height: 1.5;
        border-radius: 6px;
        transition: var(--transition);
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        gap: 0.5rem;
    }
    
    .btn i {
        font-size: 1.1em;
    }
    
    .btn-primary {
        background-color: var(--primary-color);
        color: white;
        border-color: var(--primary-light);
    }
    
    .btn-primary:hover {
        background-color: var(--primary-light);
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .btn-primary:hover {
        background-color: #00274d;
        color: white;
    }
    
    .btn-secondary {
        background-color: var(--secondary-color);
        color: var(--primary-color);
        border-color: #e07e00;
    }
    
    .btn-secondary:hover {
        background-color: #e07e00;
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .btn-secondary:hover {
        background-color: #e68a00;
        color: white;
    }
    
    /* Table Styles */
    /* Table Styles - Enhanced */
    .data-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 1.5rem 0;
        border-radius: var(--border-radius);
        overflow: hidden;
        box-shadow: 0 0 0 1px var(--medium-gray);
    }
    
    .data-table thead {
        background: var(--primary-color);
        color: white;
    }
    
    .data-table th:first-child {
        border-top-left-radius: var(--border-radius);
    }
    
    .data-table th:last-child {
        border-top-right-radius: var(--border-radius);
    }
    
    .data-table tr:last-child td:first-child {
        border-bottom-left-radius: var(--border-radius);
    }
    
    .data-table tr:last-child td:last-child {
        border-bottom-right-radius: var(--border-radius);
    }
    
    .data-table th,
    .data-table td {
        padding: 1rem;
        text-align: left;
        border-bottom: 1px solid var(--medium-gray);
        transition: var(--transition);
    }
    
    .data-table th {
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.8rem;
        letter-spacing: 0.5px;
        padding: 1rem 1.25rem;
    }
    
    .data-table tbody tr:last-child td {
        border-bottom: none;
    }
    
    .data-table th {
        background-color: var(--light-gray);
        font-weight: 600;
    }
    
    .data-table tbody tr {
        transition: var(--transition);
    }
    
    .data-table tbody tr:hover {
        background-color: rgba(0, 51, 102, 0.03);
        transform: translateX(2px);
    }
    
    .data-table tbody tr:nth-child(even) {
        background-color: var(--off-white);
    }
    
    .data-table tbody tr:nth-child(even):hover {
        background-color: rgba(0, 51, 102, 0.05);
    }
    
    /* Sentiment Badges */
    /* Sentiment Badges - Enhanced */
    .sentiment-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.35rem 0.8rem;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: capitalize;
        letter-spacing: 0.3px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: var(--transition);
    }
    
    .sentiment-badge i {
        margin-right: 0.3rem;
        font-size: 0.9em;
    }
    
    .sentiment-positive {
        background-color: var(--sentiment-positive);
        color: white;
        border-left: 4px solid darken(#2E8B57, 10%);
    }
    
    .sentiment-positive:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(46, 139, 87, 0.2);
    }
    
    .sentiment-neutral {
        background-color: var(--sentiment-neutral);
        color: white;
        border-left: 4px solid darken(#6C757D, 10%);
    }
    
    .sentiment-neutral:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(108, 117, 125, 0.2);
    }
    
    .sentiment-negative {
        background-color: var(--sentiment-negative);
        color: white;
        border-left: 4px solid darken(#DC3545, 10%);
    }
    
    .sentiment-negative:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(220, 53, 69, 0.2);
    }
    
    .sentiment-mixed {
        background-color: var(--sentiment-mixed);
        color: var(--text-dark);
        border-left: 4px solid darken(#FFC107, 15%);
    }
    
    .sentiment-mixed:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(255, 193, 7, 0.2);
    }
    
    /* Footer - Enhanced */
    .footer {
        background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
        color: white;
        padding: 3rem 0 1.5rem;
        margin-top: 4rem;
        border-top: 4px solid var(--secondary-color);
        position: relative;
        overflow: hidden;
    }
    
    .footer::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--secondary-color), var(--accent-color), var(--secondary-color));
    }
    
    .footer-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
    }
    
    .footer-section h3 {
        color: var(--secondary-color);
        margin-bottom: 1.5rem;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid rgba(255, 255, 255, 0.1);
        position: relative;
        font-size: 1.1rem;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    .footer-section h3::after {
        content: '';
        position: absolute;
        left: 0;
        bottom: -2px;
        width: 50px;
        height: 2px;
        background-color: var(--accent-color);
    }
    
    .footer-section ul {
        list-style: none;
        padding: 0;
    }
    
    .footer-section li {
        margin-bottom: 0.5rem;
    }
    
    .footer-section a {
        color: rgba(255, 255, 255, 0.8);
        text-decoration: none;
        transition: var(--transition);
        display: inline-block;
        padding: 0.25rem 0;
        position: relative;
    }
    
    .footer-section a::after {
        content: '';
        position: absolute;
        width: 0;
        height: 2px;
        bottom: 0;
        left: 0;
        background-color: var(--secondary-color);
        transition: var(--transition);
    }
    
    .footer-section a:hover::after {
        width: 100%;
    }
    
    .footer-section a:hover {
        color: white;
        transform: translateX(5px);
    }
    
    .copyright {
        text-align: center;
        padding-top: 2rem;
        margin-top: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        font-size: 0.85rem;
        color: rgba(255, 255, 255, 0.6);
        line-height: 1.6;
    }
    
    .copyright a {
        color: var(--secondary-color);
        text-decoration: none;
        font-weight: 500;
        transition: var(--transition);
    }
    
    .copyright a:hover {
        color: white;
        text-decoration: underline;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .header-container {
            flex-direction: column;
            text-align: center;
            gap: 1rem;
        }
        
        .nav-menu {
            flex-direction: column;
        }
        
        .footer-container {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# API Configuration
API_BASE_URL = "http://localhost:8001"

# Initialize session state
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None
if 'df' not in st.session_state:
    st.session_state.df = None

def check_api_status():
    """Check if the API is available"""
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        return response.status_code == 200
    except:
        return False

def load_sample_data():
    """Load sample data for demonstration"""
    data = {
        'comment': [
            "This is a great initiative by the government.",
            "The implementation could be better.",
            "I'm neutral about this proposal.",
            "Excellent work by the authorities!",
            "There are several issues that need to be addressed."
        ],
        'date': [
            '2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19'
        ]
    }
    return pd.DataFrame(data)

def analyze_comments(comments, use_advanced=False):
    """Analyze comments and return sentiment analysis results"""
    # This is a mock function - replace with actual API call
    sentiments = ['positive', 'negative', 'neutral', 'positive', 'negative']
    scores = [0.9, -0.7, 0.1, 0.8, -0.6]
    
    results = []
    for i, comment in enumerate(comments):
        results.append({
            'comment': comment,
            'sentiment': sentiments[i % len(sentiments)],
            'score': scores[i % len(scores)],
            'keywords': ['government', 'initiative'] if i % 2 == 0 else ['implementation', 'issues']
        })
    
    return {
        'status': 'success',
        'timestamp': datetime.now().isoformat(),
        'analysis_type': 'advanced' if use_advanced else 'basic',
        'results': results,
        'summary': {
            'total_comments': len(comments),
            'positive': len([r for r in results if r['sentiment'] == 'positive']),
            'negative': len([r for r in results if r['sentiment'] == 'negative']),
            'neutral': len([r for r in results if r['sentiment'] == 'neutral']),
            'average_score': sum(r['score'] for r in results) / len(results) if results else 0
        }
    }

def render_government_header():
    """Render the government-style header"""
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <div class="header">
        <div class="header-container">
            <div class="logo">
                <img src="https://www.mca.gov.in/content/dam/mca/Images/emblem.png" alt="Government Logo" style="height: 55px;">
                <div class="logo-text">
                    <h1>Ministry of Corporate Affairs</h1>
                    <p>Government of India</p>
                </div>
            </div>
            <div class="header-actions">
                <a href="#" class="btn btn-secondary"><i class="fas fa-sign-in-alt"></i> Login</a>
            </div>
        </div>
    </div>
    <div class="main-nav">
        <div class="nav-container">
            <ul class="nav-menu">
                <li><a href="#" class="active"><i class="fas fa-tachometer-alt"></i> Dashboard</a></li>
                <li><a href="#"><i class="fas fa-chart-bar"></i> Analysis</a></li>
                <li><a href="#"><i class="fas fa-file-alt"></i> Reports</a></li>
                <li><a href="#"><i class="fas fa-info-circle"></i> About</a></li>
                <li><a href="#"><i class="fas fa-question-circle"></i> Help</a></li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_dashboard():
    """Render the main dashboard"""
    st.title("E-Consultation Sentiment Analysis Dashboard")
    
    # File upload section
    st.subheader("Upload Consultation Data")
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx'])
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
                
            st.session_state.df = df
            
            # Show data preview
            st.subheader("Data Preview")
            st.dataframe(df.head())
            
            # Analyze button
            if st.button("Analyze Sentiment", key="analyze_btn"):
                with st.spinner("Analyzing comments..."):
                    comments = df['comment'].tolist() if 'comment' in df.columns else []
                    if comments:
                        st.session_state.analysis_results = analyze_comments(comments)
                        st.success("Analysis completed successfully!")
                    else:
                        st.error("No comments found in the uploaded file.")
            
            # Show analysis results if available
            if st.session_state.analysis_results:
                render_analysis_results(st.session_state.analysis_results)
                
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
    else:
        st.info("Please upload a file to begin analysis.")

def render_analysis_results(analysis_results):
    """Render the analysis results"""
    st.subheader("Analysis Results")
    
    # Summary cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Comments", analysis_results['summary']['total_comments'])
    
    with col2:
        st.metric("Positive", analysis_results['summary']['positive'])
    
    with col3:
        st.metric("Negative", analysis_results['summary']['negative'])
    
    with col4:
        st.metric("Neutral", analysis_results['summary']['neutral'])
    
    # Sentiment distribution chart
    st.subheader("Sentiment Distribution")
    sentiment_data = {
        'Sentiment': ['Positive', 'Negative', 'Neutral'],
        'Count': [
            analysis_results['summary']['positive'],
            analysis_results['summary']['negative'],
            analysis_results['summary']['neutral']
        ]
    }
    
    fig = px.pie(
        sentiment_data,
        names='Sentiment',
        values='Count',
        color='Sentiment',
        color_discrete_map={
            'Positive': '#28a745',
            'Negative': '#dc3545',
            'Neutral': '#6c757d'
        }
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Comments table
    st.subheader("Detailed Analysis")
    
    if 'results' in analysis_results and analysis_results['results']:
        results_df = pd.DataFrame(analysis_results['results'])
        
        # Add sentiment badges
        icons = {
            'positive': 'fa-smile',
            'neutral': 'fa-meh',
            'negative': 'fa-frown',
            'mixed': 'fa-meh-rolling-eyes'
        }
        def get_sentiment_badge(sentiment):
            icon = icons.get(sentiment.lower(), 'fa-circle')
            return f'<span class="sentiment-badge sentiment-{sentiment.lower()}"><i class="far {icon}"></i> {sentiment.capitalize()}</span>'
        
        results_df['Sentiment'] = results_df['sentiment'].apply(
            lambda x: get_sentiment_badge(x.capitalize())
        )
        
        # Display table
        st.markdown(
            results_df[['comment', 'Sentiment', 'score']].to_html(escape=False, index=False),
            unsafe_allow_html=True
        )
    else:
        st.info("No analysis results available.")

def render_footer():
    """Render the government-style footer"""
    current_year = datetime.now().year
    st.markdown(f"""
    <div class="footer">
        <div class="footer-container">
            <div class="footer-section">
                <h3><i class="fas fa-link"></i> Quick Links</h3>
                <ul>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Home</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> About Us</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Contact</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Help & Support</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Sitemap</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3><i class="fas fa-external-link-alt"></i> Related Sites</h3>
                <ul>
                    <li><a href="https://www.mca.gov.in" target="_blank"><i class="fas fa-external-link-alt"></i> MCA Portal</a></li>
                    <li><a href="https://www.india.gov.in" target="_blank"><i class="fas fa-external-link-alt"></i> National Portal of India</a></li>
                    <li><a href="https://www.mygov.in" target="_blank"><i class="fas fa-external-link-alt"></i> MyGov</a></li>
                    <li><a href="https://www.digitalindia.gov.in" target="_blank"><i class="fas fa-external-link-alt"></i> Digital India</a></li>
                    <li><a href="https://data.gov.in" target="_blank"><i class="fas fa-external-link-alt"></i> Open Government Data</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3><i class="fas fa-address-card"></i> Contact Us</h3>
                <p><i class="fas fa-building"></i> Ministry of Corporate Affairs</p>
                <p><i class="fas fa-map-marker-alt"></i> 5th Floor, A Wing, Shastri Bhawan</p>
                <p><i class="fas fa-road"></i> Dr. Rajendra Prasad Road, New Delhi - 110001</p>
                <p><i class="fas fa-phone"></i> <a href="tel:+911123456789">+91 11 2345 6789</a></p>
                <p><i class="fas fa-envelope"></i> <a href="mailto:support@mca.gov.in">support@mca.gov.in</a></p>
                <div class="social-links" style="margin-top: 1rem;">
                    <a href="#" style="margin-right: 10px; color: white; font-size: 1.2rem;"><i class="fab fa-twitter"></i></a>
                    <a href="#" style="margin-right: 10px; color: white; font-size: 1.2rem;"><i class="fab fa-facebook"></i></a>
                    <a href="#" style="margin-right: 10px; color: white; font-size: 1.2rem;"><i class="fab fa-youtube"></i></a>
                    <a href="#" style="color: white; font-size: 1.2rem;"><i class="fab fa-linkedin"></i></a>
                </div>
            </div>
        </div>
        <div class="copyright">
            <p>&copy; {current_year} Ministry of Corporate Affairs, Government of India. All Rights Reserved. | 
            <a href="#">Privacy Policy</a> | <a href="#">Terms of Use</a> | <a href="#">Accessibility Statement</a> | 
            <a href="#">Disclaimer</a> | <a href="#">Help</a></p>
            <p style="margin-top: 0.5rem; font-size: 0.8rem; opacity: 0.7;">
                Best viewed with latest versions of Chrome, Firefox, Safari and Internet Explorer 11+
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main application function"""
    # Render the government header
    render_government_header()
    
    # Render the main content
    with st.container():
        render_dashboard()
    
    # Render the footer
    render_footer()

if __name__ == "__main__":
    main()
