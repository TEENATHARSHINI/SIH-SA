"""
Government-Styled E-Consultation Insight Engine
Enhanced UI with all original functionality maintained
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64

# Import the original dashboard but don't run it directly
from main import main as original_main
from main import initialize_session_state

# Set page config with government theme
st.set_page_config(
    page_title="E-Consultation Insight Engine | MCA",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def add_government_theme():
    """Add government website theme CSS"""
    st.markdown("""
    <style>
    /* Root variables - Government Theme */
    :root {
        /* Official Government of India Colors */
        --primary-color: #003366;      /* Dark Blue */
        --secondary-color: #FF9933;    /* Saffron */
        --accent-color: #138808;       /* Green */
        --white: #FFFFFF;
        --light-gray: #F5F5F5;
        --medium-gray: #E0E0E0;
        --dark-gray: #333333;
        --text-dark: #212529;
        --text-light: #6C757D;
        
        /* Layout */
        --header-height: 80px;
        --footer-height: auto;
        --container-max-width: 1400px;
        --border-radius: 4px;
        --box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        
        /* Typography */
        --font-primary: 'Roboto', 'Noto Sans', sans-serif;
        --font-heading: 'Roboto', 'Noto Sans', sans-serif;
    }
    
    /* Base styles */
    body {
        margin: 0;
        padding: 0;
        font-family: var(--font-primary);
        color: var(--text-dark);
        background-color: #f8f9fa;
        line-height: 1.6;
    }
    
    /* Main container */
    .main .block-container {
        padding: calc(var(--header-height) + 1rem) 1rem 1rem;
        max-width: var(--container-max-width);
        margin: 0 auto;
    }
    
    /* Header */
    .stApp > header {
        background-color: var(--primary-color);
        background: linear-gradient(135deg, #003366 0%, #002244 100%);
        color: var(--white);
        padding: 0.5rem 2rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        height: var(--header-height);
        display: flex;
        align-items: center;
        border-bottom: 4px solid var(--secondary-color);
    }
    
    /* Logo and Title */
    .header-content {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        max-width: var(--container-max-width);
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    .logo-container {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .site-title {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .site-title h1 {
        font-size: 1.5rem;
        margin: 0;
        color: white;
        font-weight: 600;
        line-height: 1.2;
        font-family: var(--font-heading);
    }
    
    .site-title p {
        font-size: 0.9rem;
        margin: 0.2rem 0 0 0;
        opacity: 0.9;
        font-weight: 400;
    }
    
    /* Navigation */
    .main-navigation {
        display: flex;
        gap: 1.5rem;
        margin-left: 2rem;
    }
    
    .nav-link {
        color: rgba(255, 255, 255, 0.9);
        text-decoration: none;
        font-weight: 500;
        padding: 0.5rem 0;
        position: relative;
        transition: var(--transition);
    }
    
    .nav-link:hover {
        color: var(--white);
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 2px;
        background-color: var(--secondary-color);
        transition: var(--transition);
    }
    
    .nav-link:hover::after {
        width: 100%;
    }
    
    /* Cards */
    .card {
        background: var(--white);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: var(--box-shadow);
        border: 1px solid var(--medium-gray);
        transition: var(--transition);
        position: relative;
        overflow: hidden;
        border-top: 4px solid var(--primary-color);
    }
    
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
    
    .card-title {
        color: var(--primary-color);
        font-weight: 600;
        margin-bottom: 1rem;
        font-family: var(--font-heading);
        font-size: 1.25rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .card-title i {
        color: var(--secondary-color);
    }
    
    /* Buttons */
    .stButton>button {
        background-color: var(--primary-color);
        background: linear-gradient(135deg, var(--primary-color) 0%, #002244 100%);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        padding: 0.6rem 1.5rem;
        font-weight: 500;
        font-family: var(--font-primary);
        text-transform: uppercase;
        font-size: 0.85rem;
        letter-spacing: 0.5px;
        transition: var(--transition);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #002244 0%, #001122 100%);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Secondary Button */
    .stButton>button.secondary {
        background: var(--white);
        color: var(--primary-color);
        border: 1px solid var(--primary-color);
    }
    
    .stButton>button.secondary:hover {
        background: var(--light-gray);
        color: var(--primary-color);
    }
    
    /* Footer */
    .footer {
        width: 100%;
        background: linear-gradient(135deg, #002244 0%, #003366 100%);
        color: var(--white);
        padding: 2rem 0 0;
        margin-top: 3rem;
        position: relative;
        z-index: 100;
        font-family: var(--font-primary);
    }
    
    .footer-content {
        max-width: var(--container-max-width);
        margin: 0 auto;
        padding: 0 1rem;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
    }
    
    .footer-section h3 {
        color: var(--white);
        font-size: 1.1rem;
        margin-bottom: 1.2rem;
        position: relative;
        padding-bottom: 0.5rem;
    }
    
    .footer-section h3::after {
        content: '';
        position: absolute;
        left: 0;
        bottom: 0;
        width: 40px;
        height: 2px;
        background-color: var(--secondary-color);
    }
    
    .footer-links {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .footer-links li {
        margin-bottom: 0.6rem;
    }
    
    .footer-links a {
        color: rgba(255, 255, 255, 0.8);
        text-decoration: none;
        transition: var(--transition);
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .footer-links a:hover {
        color: var(--white);
        padding-left: 5px;
    }
    
    .footer-links i {
        font-size: 0.8em;
    }
    
    .social-links {
        display: flex;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .social-links a {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background-color: rgba(255, 255, 255, 0.1);
        color: var(--white);
        transition: var(--transition);
    }
    
    .social-links a:hover {
        background-color: var(--secondary-color);
        transform: translateY(-3px);
    }
    
    .footer-bottom {
        text-align: center;
        padding: 1.5rem 0;
        margin-top: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.7);
    }
    
    /* Responsive Design */
    @media (max-width: 992px) {
        .header-content {
            flex-direction: column;
            align-items: flex-start;
            padding: 1rem;
        }
        
        .main-navigation {
            margin: 1rem 0 0 0;
            width: 100%;
            overflow-x: auto;
            padding-bottom: 0.5rem;
        }
        
        .nav-link {
            white-space: nowrap;
        }
    }
    
    @media (max-width: 768px) {
        .footer-content {
            grid-template-columns: 1fr 1fr;
        }
    }
    
    @media (max-width: 576px) {
        .footer-content {
            grid-template-columns: 1fr;
        }
        
        .site-title h1 {
            font-size: 1.25rem;
        }
        
        .site-title p {
            font-size: 0.8rem;
        }
    }
    </style>
    
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Noto+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

def render_government_header():
    """Render the government-style header with Indian Government branding"""
    st.markdown("""
    <header class="gov-header">
        <div class="header-content">
            <div class="logo-container">
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/1200px-Flag_of_India.svg.png" 
                     alt="Indian Flag" style="height: 50px; margin-right: 15px;">
                <div class="site-title">
                    <h1>भारत सरकार | Government of India</h1>
                    <p>Ministry of Corporate Affairs</p>
                </div>
            </div>
            
            <nav class="main-navigation">
                <a href="#" class="nav-link"><i class="fas fa-home"></i> Home</a>
                <a href="#dashboard" class="nav-link"><i class="fas fa-chart-line"></i> Dashboard</a>
                <a href="#analysis" class="nav-link"><i class="fas fa-file-alt"></i> Analysis</a>
                <a href="#reports" class="nav-link"><i class="fas fa-database"></i> Reports</a>
                <a href="#about" class="nav-link"><i class="fas fa-info-circle"></i> About</a>
            </nav>
            
            <div class="header-actions">
                <div class="user-info">
                    <span class="user-name"><i class="fas fa-user-circle"></i> Welcome, Admin</span>
                </div>
            </div>
        </div>
    </header>
    """, unsafe_allow_html=True)

def render_government_footer():
    """Render the government-style footer with important links and information"""
    st.markdown("""
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul class="footer-links">
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Home</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> About MCA</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Policies</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Acts & Rules</a></li>
                </ul>
            </div>
            
            <div class="footer-section">
                <h3>Services</h3>
                <ul class="footer-links">
                    <li><a href="#"><i class="fas fa-chevron-right"></i> MCA21 Services</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Company Forms</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Public Documents</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> FAQ</a></li>
                </ul>
            </div>
            
            <div class="footer-section">
                <h3>Resources</h3>
                <ul class="footer-links">
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Publications</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Reports</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Statistics</a></li>
                    <li><a href="#"><i class="fas fa-chevron-right"></i> Tenders</a></li>
                </ul>
            </div>
            
            <div class="footer-section">
                <h3>Contact Us</h3>
                <ul class="footer-links">
                    <li><i class="fas fa-map-marker-alt"></i> Ministry of Corporate Affairs,<br>Shastri Bhawan, Dr. Rajendra Prasad Road,<br>New Delhi - 110001, India</li>
                    <li><i class="fas fa-phone"></i> +91-11-2338 1000</li>
                    <li><i class="fas fa-envelope"></i> info@mca.gov.in</li>
                </ul>
                
                <div class="social-links">
                    <a href="#" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                    <a href="#" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
                    <a href="#" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                </div>
            </div>
        </div>
        
        <div class="footer-bottom">
            <p>© 2025 Ministry of Corporate Affairs, Government of India. All Rights Reserved.</p>
            <p style="font-size: 0.85rem; opacity: 0.8; margin-top: 0.5rem;">
                <a href="#" style="color: rgba(255, 255, 255, 0.8); text-decoration: none; margin: 0 10px;">Privacy Policy</a> | 
                <a href="#" style="color: rgba(255, 255, 255, 0.8); text-decoration: none; margin: 0 10px;">Terms of Use</a> | 
                <a href="#" style="color: rgba(255, 255, 255, 0.8); text-decoration: none; margin: 0 10px;">Disclaimer</a> | 
                <a href="#" style="color: rgba(255, 255, 255, 0.8); text-decoration: none; margin: 0 10px;">Help</a>
            </p>
            <p style="font-size: 0.8rem; opacity: 0.7; margin-top: 1rem;">
                Last Updated: 23rd September 2025
            </p>
        </div>
    </footer>
    """, unsafe_allow_html=True)

def main():
    # Add government theme
    add_government_theme()
    
    # Render the government header
    render_government_header()
    
    # Add some spacing after the fixed header
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    
    # Initialize session state if not already done
    if 'initialized' not in st.session_state:
        initialize_session_state()
        st.session_state.initialized = True
    
    # Run the original dashboard content
    original_main()
    
    # Add some spacing before footer
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    
    # Render the government footer
    render_government_footer()

if __name__ == "__main__":
    main()
