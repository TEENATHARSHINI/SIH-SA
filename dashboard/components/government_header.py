import streamlit as st

def show_government_header():
    """Display the government website header"""
    st.markdown(
        """
        <style>
            header {visibility: hidden;}
            .main .block-container {padding-top: 1rem;}
        </style>
        
        <header>
            <div class="govt-header">
                <div class="govt-logo">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Emblem_of_India.svg/1200px-Emblem_of_India.svg.png" alt="Government Logo">
                    <div class="govt-title">
                        <h1>भारत सरकार | Government of India</h1>
                        <p>Ministry of Electronics & Information Technology</p>
                    </div>
                </div>
            </div>
            <nav class="govt-nav">
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Services</a></li>
                    <li><a href="#">Documents</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>
        </header>
        """,
        unsafe_allow_html=True
    )
