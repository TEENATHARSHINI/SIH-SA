"""
E-Consultation Insight Engine - Clean Version
Original functionality with default Streamlit styling
"""

import streamlit as st
import sys
import os

# Add the parent directory to path to import the main module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the original dashboard components
from dashboard.main import (
    main as original_main,
    initialize_session_state,
    configure_page
)

def main():
    """Main application function with clean styling"""
    # Configure page with default Streamlit settings
    configure_page()
    
    # Initialize session state if not already done
    if 'initialized' not in st.session_state:
        initialize_session_state()
        st.session_state.initialized = True
    
    # Render the original dashboard content without any theme overrides
    original_main()

if __name__ == "__main__":
    main()
