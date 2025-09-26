import streamlit as st
from components.government_header import show_government_header
from components.government_footer import show_government_footer

def main():
    # Set page config
    st.set_page_config(
        page_title="Policy Feedback Analysis Portal | Government of India",
        page_icon="🇮🇳",
        layout="wide"
    )
    
    # Load custom CSS
    with open("dashboard/assets/government_theme.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # Show government header
    show_government_header()
    
    # Main content
    st.markdown("""
    <div class="main-content">
        <div class="govt-card">
            <h2>Policy Feedback Analysis Portal</h2>
            <p>Welcome to the official Policy Feedback Analysis Portal of the Government of India. 
            This platform allows citizens to provide feedback on government policies and initiatives.</p>
        </div>
        
        <div class="govt-card">
            <h2>Upload Feedback</h2>
            <p>Upload your feedback documents in various formats including PDF, DOCX, or plain text.</p>
            <button class="govt-btn">Upload Document</button>
        </div>
        
        <div class="govt-card">
            <h2>View Analysis</h2>
            <p>Access comprehensive analysis of public feedback on various government policies.</p>
            <button class="govt-btn">View Reports</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Show government footer
    show_government_footer()

if __name__ == "__main__":
    main()
