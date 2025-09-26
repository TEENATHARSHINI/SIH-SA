"""
Enhanced Government Dashboard UI
Maintains all original functionality with improved government website styling
"""

import streamlit as st
import sys
import os
import importlib.util

# Import the main function from main.py
current_dir = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(current_dir, 'main.py')

# Load the module
spec = importlib.util.spec_from_file_location("main_module", main_path)
main_module = importlib.util.module_from_spec(spec)
sys.modules["main_module"] = main_module
spec.loader.exec_module(main_module)

# Get the main function
original_main = main_module.main

# ===================================
# Enhanced Government UI Configuration
# ===================================

def set_enhanced_theme():
    """Apply government website theme with improved styling"""
    st.markdown("""
    <style>
        /* Base Government Theme */
        :root {
            --primary: #003366;     /* Dark blue */
            --secondary: #0F4D92;   /* Medium blue */
            --accent: #FFA500;      /* Gold accent */
            --light: #F5F5F5;       /* Light gray */
            --dark: #333333;        /* Dark text */
            --success: #2E8B57;     /* Green */
            --warning: #FF8C00;     /* Orange */
            --danger: #8B0000;      /* Red */
        }
        
        /* Main Container */
        .main .block-container {
            max-width: 1200px;
            padding: 1rem 2rem;
        }
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            color: var(--primary);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }
        
        /* Buttons */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border-radius: 4px;
            padding: 0.5rem 1.5rem;
            font-weight: 500;
            transition: all 0.3s ease;
            border: none;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary);
            transform: translateY(-2px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Sidebar */
        .css-1d391kg {
            background-color: #f8f9fa;
            border-right: 1px solid #dee2e6;
        }
        
        /* Cards */
        .stCard {
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border: 1px solid #dee2e6;
        }
        
        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        th, td {
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #dee2e6;
        }
        
        th {
            background-color: var(--light);
            font-weight: 600;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 8px 16px;
            border-radius: 4px 4px 0 0;
            background-color: #f8f9fa;
            color: var(--dark);
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary);
            color: white;
        }
        
        /* Footer */
        footer {
            margin-top: 3rem;
            padding: 1.5rem 0;
            border-top: 1px solid #dee2e6;
            color: #6c757d;
            font-size: 0.875rem;
        }
    </style>
    """, unsafe_allow_html=True)

def render_government_header():
    """Render government-style header"""
    st.markdown("""
    <div style="background-color: #003366; color: white; padding: 1rem 0; margin: -1rem -1rem 1.5rem -1rem;">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 2rem; display: flex; align-items: center;">
            <div style="flex-grow: 1;">
                <h1 style="color: white; margin: 0; font-size: 1.8rem;">Government of India</h1>
                <p style="margin: 0.25rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">E-Consultation Insight Engine</p>
            </div>
            <div style="text-align: right;">
                <img src="https://www.india.gov.in/sites/upload_files/npi/frontend-assets/images/emblem.png" 
                     style="height: 60px;" 
                     alt="National Emblem">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_government_footer():
    """Render government-style footer"""
    st.markdown("""
    <footer style="background-color: #f8f9fa; padding: 2rem 0; margin-top: 3rem;">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 2rem;">
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 2rem;">
                <div>
                    <h4 style="color: #003366; margin-top: 0;">Quick Links</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li><a href="#" style="color: #495057; text-decoration: none;">Home</a></li>
                        <li><a href="#" style="color: #495057; text-decoration: none;">About Us</a></li>
                        <li><a href="#" style="color: #495057; text-decoration: none;">Contact</a></li>
                        <li><a href="#" style="color: #495057; text-decoration: none;">Help</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: #003366; margin-top: 0;">Related Sites</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li><a href="https://www.india.gov.in/" style="color: #495057; text-decoration: none;">National Portal of India</a></li>
                        <li><a href="https://www.mygov.in/" style="color: #495057; text-decoration: none;">MyGov</a></li>
                        <li><a href="https://www.meity.gov.in/" style="color: #495057; text-decoration: none;">Ministry of Electronics & IT</a></li>
                    </ul>
                </div>
                <div style="flex-grow: 1; max-width: 400px;">
                    <h4 style="color: #003366; margin-top: 0;">Contact Us</h4>
                    <p style="margin: 0.5rem 0; color: #495057;">
                        <i class="fas fa-map-marker-alt" style="margin-right: 0.5rem;"></i>
                        Ministry of Electronics and Information Technology<br>
                        Electronics Niketan, 6 CGO Complex, Lodhi Road,<br>
                        New Delhi - 110003, India
                    </p>
                    <p style="margin: 0.5rem 0; color: #495057;">
                        <i class="fas fa-phone" style="margin-right: 0.5rem;"></i>
                        +91-11-24301951
                    </p>
                    <p style="margin: 0.5rem 0; color: #495057;">
                        <i class="fas fa-envelope" style="margin-right: 0.5rem;"></i>
                        support@econsultation.gov.in
                    </p>
                </div>
            </div>
            <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #dee2e6; text-align: center; color: #6c757d; font-size: 0.875rem;">
                <p>© 2023 Government of India. All Rights Reserved.</p>
                <div style="margin-top: 0.5rem;">
                    <a href="#" style="color: #6c757d; margin: 0 0.5rem; text-decoration: none;">Privacy Policy</a> |
                    <a href="#" style="color: #6c757d; margin: 0 0.5rem; text-decoration: none;">Terms of Use</a> |
                    <a href="#" style="color: #6c757d; margin: 0 0.5rem; text-decoration: none;">Help</a> |
                    <a href="#" style="color: #6c757d; margin: 0 0.5rem; text-decoration: none;">Sitemap</a>
                </div>
            </div>
        </div>
    </footer>
    """, unsafe_allow_html=True)

# ===================================
# Enhanced Main Application
# ===================================

def main():
    # Set page config
    st.set_page_config(
        page_title="E-Consultation Insight Engine | Government of India",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply enhanced theme
    set_enhanced_theme()
    
    # Render government header
    render_government_header()
    
    # Call the original main function which contains all the functionality
    # This will render all your existing content with the new styling
    original_main()
    
    # Render government footer
    render_government_footer()

# Run the enhanced application
if __name__ == "__main__":
    main()
