import streamlit as st

def show_government_footer():
    """Display the government website footer"""
    st.markdown(
        """
        <footer class="govt-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Services</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Important Links</h3>
                    <ul>
                        <li><a href="https://www.india.gov.in/" target="_blank">National Portal of India</a></li>
                        <li><a href="https://meity.gov.in/" target="_blank">MeitY</a></li>
                        <li><a href="https://www.digitalindia.gov.in/" target="_blank">Digital India</a></li>
                        <li><a href="https://www.mygov.in/" target="_blank">MyGov</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Contact Us</h3>
                    <p>Ministry of Electronics & IT<br>
                    Electronics Niketan, 6 CGO Complex,<br>
                    Lodhi Road, New Delhi - 110003<br>
                    Phone: 011-24301931<br>
                    Email: feedback@meity.gov.in</p>
                </div>
            </div>
            <div class="copyright">
                <p>© 2025 Government of India. All Rights Reserved.</p>
                <p>Last Updated: September 23, 2025</p>
            </div>
        </footer>
        """,
        unsafe_allow_html=True
    )
