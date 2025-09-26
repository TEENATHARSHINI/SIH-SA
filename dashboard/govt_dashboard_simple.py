"""
Simplified Government Dashboard with National Emblem
"""

import streamlit as st

# Set page config
st.set_page_config(
    page_title="E-Consultation Dashboard | Government of India",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for government theme
st.markdown("""
<style>
/* Government Theme */
:root {
    --primary: #003366;
    --secondary: #0F4D92;
    --accent: #FFA500;
    --light: #F5F5F5;
    --dark: #333333;
}

/* Header */
.govt-header {
    background: linear-gradient(135deg, #003366 0%, #0F4D92 100%);
    padding: 1rem 2rem;
    margin: -1rem -1rem 1.5rem -1rem;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.govt-title h1 {
    margin: 0;
    font-size: 1.8rem;
}

.govt-title p {
    margin: 0.25rem 0 0 0;
    opacity: 0.9;
}

/* Main container */
.main .block-container {
    max-width: 1200px;
    padding: 1rem 2rem;
}

/* Buttons */
.stButton>button {
    background-color: var(--primary);
    color: white;
    border-radius: 4px;
    padding: 0.5rem 1.5rem;
    border: none;
}

.stButton>button:hover {
    background-color: var(--secondary);
    color: white;
}

/* Cards */
.stCard {
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    border: 1px solid #dee2e6;
    color: #000000 !important;
}

/* Ensure text in all containers is visible */
.stContainer, .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
    color: #000000 !important;
}

/* Override any Streamlit text colors */
[data-testid="stMarkdownContainer"] {
    color: #000000 !important;
}

/* Footer */
.govt-footer {
    margin-top: 3rem;
    padding: 1.5rem 0;
    border-top: 1px solid #dee2e6;
    text-align: center;
    color: #6c757d;
    font-size: 0.875rem;
}
</style>
""", unsafe_allow_html=True)

def render_header():
    """Render government header with emblem"""
    st.markdown("""
    <div class="govt-header">
        <div class="govt-title">
            <h1>Government of India</h1>
            <p>E-Consultation Insight Engine</p>
        </div>
        <div>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Emblem_of_India.svg/1200px-Emblem_of_India.svg.png" 
                 alt="National Emblem" 
                 style="height: 60px;">
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Render government footer"""
    st.markdown("""
    <div class="govt-footer">
        <p>© 2023 Government of India. All Rights Reserved.</p>
    </div>
    """, unsafe_allow_html=True)

def create_metric_card(title, value, change=None, icon="📊"):
    """Helper function to create metric cards"""
    change_html = f"<span style='color: #28a745; font-size: 0.9rem;'>{change}% ↑</span>" if change else ""
    return f"""
    <div class='metric-card'>
        <div class='metric-icon'>{icon}</div>
        <div class='metric-content'>
            <div class='metric-title'>{title}</div>
            <div class='metric-value'>{value}</div>
            {change_html}
        </div>
    </div>
    """

def main():
    # Render header
    render_header()
    
    # Add custom CSS for metrics and layout
    st.markdown("""
    <style>
        /* Metrics grid */
        .metric-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .metric-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .metric-icon {
            font-size: 2rem;
            color: #0F4D92;
        }
        
        .metric-title {
            color: #6c757d;
            font-size: 0.9rem;
            margin-bottom: 0.25rem;
        }
        
        .metric-value {
            font-size: 1.5rem;
            font-weight: 600;
            color: #212529;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: #f8f9fa;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            color: #495057;
            font-weight: 500;
        }
        
        .stTabs [aria-selected="true"] {
            background: #003366;
            color: white;
        }
        
        /* Data tables */
        .stDataFrame {
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Main content
    st.title("Policy Feedback Analytics Dashboard")
    
    # Metrics row
    st.markdown('<div class="metric-grid">' + 
                create_metric_card("Total Feedback", "1,248", 12, "📝") +
                create_metric_card("Positive Sentiment", "68%", 5, "😊") +
                create_metric_card("Avg. Response Time", "2.4 days", -3, "⏱️") +
                create_metric_card("Active Policies", "24", 2, "📋") + 
                '</div>', unsafe_allow_html=True)
    
    # Main content area with tabs
    tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Analysis", "⚙️ Settings"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Sentiment Trend")
            # Sample data for chart
            chart_data = {
                'Date': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                'Positive': [45, 52, 48, 62, 55, 68],
                'Negative': [25, 20, 22, 18, 20, 15],
                'Neutral': [30, 28, 30, 20, 25, 17]
            }
            st.bar_chart(
                data=chart_data,
                x='Date',
                y=['Positive', 'Neutral', 'Negative'],
                color=["#28a745", "#ffc107", "#dc3545"]
            )
            
        with col2:
            st.subheader("Top Categories")
            # Sample data for pie chart
            categories = {
                'Education': 35,
                'Healthcare': 25,
                'Infrastructure': 20,
                'Agriculture': 15,
                'Others': 5
            }
            st.bar_chart(categories)
    
    with tab2:
        st.subheader("Detailed Analysis")
        # Sample data table
        import pandas as pd
        data = {
            'Policy': ['Education Reform', 'Healthcare Access', 'Infrastructure', 'Farmers Support', 'Digital India'],
            'Feedback Count': [245, 198, 176, 154, 132],
            'Avg. Sentiment': [0.72, 0.68, 0.61, 0.55, 0.78],
            'Response Rate': '92% 85% 88% 79% 95%'.split()
        }
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Add some sample insights
        st.markdown("""
        ### Key Insights
        - Education policies received the highest engagement with 245 feedback entries
        - Digital India initiative has the highest positive sentiment at 78%
        - Farmers Support policies show room for improvement in public perception
        """)
    
    with tab3:
        st.subheader("Dashboard Settings")
        st.checkbox("Show real-time updates", value=True)
        st.checkbox("Enable email notifications", value=True)
        st.selectbox("Update frequency", ["Daily", "Weekly", "Monthly"])
        st.button("Save Settings")
    
    # Add some sample interactive elements
    with st.sidebar:
        st.header("Filters")
        st.selectbox("Select Department", ["All", "Education", "Healthcare", "Infrastructure"])
        st.date_input("Date Range", [])
        st.slider("Minimum Feedback Count", 0, 1000, 100)
        st.multiselect("Sentiment", ["Positive", "Neutral", "Negative"], ["Positive", "Neutral"])
    
    # Render footer
    render_footer()

if __name__ == "__main__":
    main()
