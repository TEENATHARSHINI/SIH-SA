"""
Government Theme for E-Consultation Insight Engine
"""

def apply_government_theme():
    """Apply government theme to the Streamlit app"""
    gov_theme = """
    <style>
        /* Main container */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            color: #003366 !important;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 0.3em;
        }
        
        /* Buttons */
        .stButton>button {
            background-color: #003366;
            color: white;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            border: none;
            font-weight: 500;
        }
        
        .stButton>button:hover {
            background-color: #002244;
            color: white;
            border: none;
        }
        
        /* Sidebar */
        .css-1d391kg {
            background-color: #f8f9fa;
            border-right: 1px solid #dee2e6;
        }
        
        /* Cards */
        .stDataFrame, .stAlert, .stExpander {
            border: 1px solid #dee2e6;
            border-radius: 4px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: #f8f9fa;
            border-radius: 4px 4px 0 0;
            margin-right: 2px;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #003366;
            color: white;
        }
        
        /* File uploader */
        .stFileUploader {
            border: 2px dashed #dee2e6;
            border-radius: 4px;
            padding: 2rem;
            text-align: center;
        }
        
        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        th {
            background-color: #003366;
            color: white;
            text-align: left;
            padding: 0.5rem;
        }
        
        td {
            padding: 0.5rem;
            border-bottom: 1px solid #dee2e6;
        }
        
        tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        
        /* Footer */
        footer {
            visibility: hidden;
        }
        
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #003366;
            color: white;
            text-align: center;
            padding: 0.5rem 0;
            font-size: 0.8rem;
        }
    </style>
    
    <div class="footer">
        © 2025 Government of India. All Rights Reserved.
    </div>
    """
    
    return gov_theme
