"""
Government-Styled E-Consultation Insight Engine
Enhanced UI with professional government theme
"""

import streamlit as st
import base64
import os
import sys
from pathlib import Path

# Add the parent directory to path to import the main module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the original dashboard but don't run it directly
from dashboard.main import main as original_main
from dashboard.main import initialize_session_state

# Set page config with government theme
st.set_page_config(
    page_title="E-Consultation Insight Engine | Government of India",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def add_government_theme():
    """Add professional government website theme CSS"""
    st.markdown("""
    <style>
    /* Root variables - Government Theme */
    :root {
        /* Official Government of India Colors */
        --primary-color: #003366;      /* Dark Blue */
        --primary-light: #1a4d80;      /* Lighter Blue */
        --primary-dark: #001a33;       /* Darker Blue */
        --secondary-color: #FF9933;    /* Saffron */
        --secondary-light: #ffad4d;    /* Lighter Saffron */
        --accent-color: #138808;       /* Green */
        --accent-light: #2ba01f;      /* Lighter Green */
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
    .stApp .stBlock {
        background: var(--white);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: var(--box-shadow);
        border: 1px solid var(--medium-gray);
        transition: var(--transition);
        position: relative;
        overflow: hidden;
        border-left: 4px solid var(--primary-color);
    }
    
    .stApp .stBlock:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
    
    .stApp h1, .stApp h2, .stApp h3 {
        color: var(--primary-color);
        font-family: var(--font-heading);
    }
    
    /* Buttons */
    .stButton > button {
        background-color: var(--primary-color);
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
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
    
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary-color) 100%);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Secondary Button */
    .stButton > button.secondary {
        background: var(--white);
        color: var(--primary-color);
        border: 1px solid var(--primary-color);
    }
    
    .stButton > button.secondary:hover {
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
    
    .footer::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color), var(--accent-color));
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
        margin-bottom: 0.5rem;
    }
    
    .footer-links a {
        color: rgba(255, 255, 255, 0.8);
        text-decoration: none;
        transition: var(--transition);
    }
    
    .footer-links a:hover {
        color: var(--white);
        padding-left: 5px;
    }
    
    .footer-bottom {
        text-align: center;
        padding: 1.5rem 0;
        margin-top: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.7);
    }
    
    /* Form elements */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > div,
    .stNumberInput > div > div > input {
        border-radius: var(--border-radius) !important;
        border: 1px solid var(--medium-gray) !important;
        padding: 0.5rem 0.75rem !important;
    }
    
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label,
    .stNumberInput > label {
        font-weight: 500;
        color: var(--text-dark);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.75rem 1.5rem;
        border-radius: var(--border-radius);
        background-color: var(--light-gray);
        color: var(--text-dark);
        transition: var(--transition);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: var(--medium-gray);
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--primary-color);
        color: white;
    }
    
    /* Tables */
    .stDataFrame {
        border-radius: var(--border-radius);
        overflow: hidden;
        box-shadow: var(--box-shadow);
    }
    
    /* Charts */
    .stPlotlyChart {
        border-radius: var(--border-radius);
        overflow: hidden;
        box-shadow: var(--box-shadow);
    }
    
    /* Responsive adjustments */
    @media (max-width: 992px) {
        .header-content {
            flex-direction: column;
            text-align: center;
            gap: 1rem;
        }
        
        .main-navigation {
            margin: 1rem 0 0;
            flex-wrap: wrap;
            justify-content: center;
        }
        
        .footer-content {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    
    @media (max-width: 576px) {
        .footer-content {
            grid-template-columns: 1fr;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 0.5rem 1rem;
            font-size: 0.9rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def render_government_header():
    """Render government website header"""
    st.markdown(
        """
        <div class="header-content">
            <div class="logo-container">
                <div class="site-title">
                    <h1>E-Consultation Insight Engine</h1>
                    <p>Government of India | Ministry of Corporate Affairs</p>
                </div>
            </div>
            <nav class="main-navigation">
                <a href="#" class="nav-link">Home</a>
                <a href="#analysis" class="nav-link">Analysis</a>
                <a href="#reports" class="nav-link">Reports</a>
                <a href="#about" class="nav-link">About</a>
                <a href="#contact" class="nav-link">Contact</a>
            </nav>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_government_footer():
    """Render government website footer"""
    st.markdown(
        """
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>About Us</h3>
                    <p>Empowering public consultation through advanced sentiment analysis and insights.</p>
                </div>
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <ul class="footer-links">
                        <li><a href="#">Home</a></li>
                        <li><a href="#analysis">Analysis</a></li>
                        <li><a href="#reports">Reports</a></li>
                        <li><a href="#about">About</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Resources</h3>
                    <ul class="footer-links">
                        <li><a href="#">Documentation</a></li>
                        <li><a href="#">API</a></li>
                        <li><a href="#">Help Center</a></li>
                        <li><a href="#">Tutorials</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Contact</h3>
                    <ul class="footer-links">
                        <li>Email: support@mca.gov.in</li>
                        <li>Phone: 1800-123-1234</li>
                        <li>Address: New Delhi, India</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Ministry of Corporate Affairs, Government of India. All Rights Reserved.</p>
            </div>
        </footer>
        """,
        unsafe_allow_html=True
    )

def main():
    """Main application function"""
    # Add government theme
    add_government_theme()
    
    # Render government header
    render_government_header()
    
    # Initialize session state if not already done
    if 'initialized' not in st.session_state:
        initialize_session_state()
        st.session_state.initialized = True
    
    # Render the original dashboard content
    original_main()
    
    # Add some spacing before footer
    st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)
    
    # Render government footer
    render_government_footer()

if __name__ == "__main__":
    main()
