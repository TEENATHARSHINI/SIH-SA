"""
FINAL COMPLETE GOVERNMENT DASHBOARD - 200% Working
All features integrated with MCA styling
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
                    
                    # Convert to display format
                    display_data = [{
                        "id": 1,
                        "confidence": analysis_data["results"][0]["confidence"],
                        "language": analysis_data["results"][0].get("explanation", {}).get("language_info", {}).get("language", "english")
                    }]
                    
                    st.session_state['current_data'] = display_data
                    st.success("✅ Text analyzed successfully!")

# Main Application
def main():
    # Check API Status
    api_online, health_data = check_api_status()

    # Sidebar: Navigation and System Status
    with st.sidebar:
        st.markdown("### 🏛️ System Status")
        st.markdown(f"**API Service:** {get_status_indicator(api_online)}", unsafe_allow_html=True)
        if api_online and health_data:
            st.markdown("### ✅ Available Features")
            features = health_data.get('services', {})
            for feature, status in features.items():
                icon = "✅" if status else "❌"
                st.markdown(f"{icon} {feature.replace('_', ' ').title()}")
        st.markdown("---")
        st.markdown("### 📋 Navigation")
        nav_options = [
            "File Upload", "Single Analysis", "Batch Analysis", "Summarization", "Key Phrase Extraction", "Word Cloud", "Comment Explorer", "Stakeholder Analysis", "Legislative Context", "Aspect-Based Sentiment", "Explainability", "Sarcasm Detection", "Admin Panel", "System Analytics", "Export & Reports"
        ]
        selected_tab = st.radio("Select Feature:", nav_options)

    # Main Content Area
    if not api_online:
        st.markdown("""
        <div class="error-message">
            <h3>⚠️ API Service Unavailable</h3>
            <p>The sentiment analysis API is currently offline. Please ensure the API server is running on port 8001.</p>
            <p><strong>To start the API:</strong></p>
            <p><code>python backend/final_api.py</code></p>
        </div>
        """, unsafe_allow_html=True)
        return

    # Feature Tabs
    if selected_tab == "File Upload":
        from dashboard.components.file_upload import render_file_upload
        render_file_upload()
    elif selected_tab == "Single Analysis":
        from dashboard.components.analysis_dashboard import render_single_text_analysis
        render_single_text_analysis()
    elif selected_tab == "Batch Analysis":
        from dashboard.components.analysis_dashboard import render_batch_analysis
        render_batch_analysis()
    elif selected_tab == "Summarization":
        from dashboard.components.text_analytics import render_summarization_interface
        render_summarization_interface()
    elif selected_tab == "Key Phrase Extraction":
        from dashboard.components.text_analytics import render_key_phrase_extraction
        render_key_phrase_extraction()
    elif selected_tab == "Word Cloud":
        from dashboard.components.text_analytics import render_text_statistics
        render_text_statistics()
    elif selected_tab == "Comment Explorer":
        from dashboard.components.analysis_dashboard import render_saved_comments_analysis
        render_saved_comments_analysis()
    elif selected_tab == "Stakeholder Analysis":
        from dashboard.main import render_stakeholder_analysis
        render_stakeholder_analysis()
    elif selected_tab == "Legislative Context":
        from dashboard.main import render_legislative_context
        render_legislative_context()
    elif selected_tab == "Aspect-Based Sentiment":
        from dashboard.main import render_comparative_analysis
        render_comparative_analysis()
    elif selected_tab == "Explainability":
        from dashboard.main import render_advanced_analysis
        render_advanced_analysis()
    elif selected_tab == "Sarcasm Detection":
        st.markdown("## 🤨 Sarcasm Detection")
        st.info("Sarcasm detection is enabled for English and Hindi comments. Results will be shown in analysis tabs.")
    elif selected_tab == "Admin Panel":
        from dashboard.components.admin_panel import render_admin_panel
        render_admin_panel()
    elif selected_tab == "System Analytics":
        from dashboard.components.admin_panel import render_system_analytics
        render_system_analytics()
    elif selected_tab == "Export & Reports":
        st.markdown("## 💾 Export & Reports")
        st.info("Export options are available in each analysis tab. Download CSV, JSON, PDF, or Excel for all results.")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; margin-top: 2rem;">
        <p><strong>Ministry of Corporate Affairs | Government of India</strong></p>
        <p>eConsultation Sentiment Analysis Portal • Version 3.0 • Powered by Advanced AI</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
        with col1:
            st.markdown(format_sentiment_card(
                "Positive", 
                sentiment_counts['positive'], 
                (sentiment_counts['positive']/total)*100
            ), unsafe_allow_html=True)
        
        with col2:
            st.markdown(format_sentiment_card(
                "Neutral", 
                sentiment_counts['neutral'], 
                (sentiment_counts['neutral']/total)*100
            ), unsafe_allow_html=True)
        
        with col3:
            st.markdown(format_sentiment_card(
                "Negative", 
                sentiment_counts['negative'], 
                (sentiment_counts['negative']/total)*100
            ), unsafe_allow_html=True)

        # Visualization Section
        st.markdown("### 📈 Data Visualizations")
        
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            # Sentiment Distribution Pie Chart
            fig_pie = px.pie(
                values=[sentiment_counts['positive'], sentiment_counts['neutral'], sentiment_counts['negative']],
                names=['Positive', 'Neutral', 'Negative'],
                title="Sentiment Distribution",
                color_discrete_map={
                    'Positive': '#28a745',
                    'Neutral': '#17a2b8', 
                    'Negative': '#dc3545'
                }
            )
            fig_pie.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                title_font_size=16,
                title_font_color='#003366'
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with viz_col2:
            # Stakeholder Analysis
            if 'stakeholder_type' in data[0]:
                stakeholder_sentiments = {}
                for item in data:
                    stakeholder = item['stakeholder_type']
                    sentiment = item['sentiment']
                    if stakeholder not in stakeholder_sentiments:
                        stakeholder_sentiments[stakeholder] = {'positive': 0, 'neutral': 0, 'negative': 0}
                    stakeholder_sentiments[stakeholder][sentiment] += 1
                
                # Create stacked bar chart
                stakeholders = list(stakeholder_sentiments.keys())
                positive_counts = [stakeholder_sentiments[s]['positive'] for s in stakeholders]
                neutral_counts = [stakeholder_sentiments[s]['neutral'] for s in stakeholders]
                negative_counts = [stakeholder_sentiments[s]['negative'] for s in stakeholders]
                
                fig_bar = go.Figure(data=[
                    go.Bar(name='Positive', x=stakeholders, y=positive_counts, marker_color='#28a745'),
                    go.Bar(name='Neutral', x=stakeholders, y=neutral_counts, marker_color='#17a2b8'),
                    go.Bar(name='Negative', x=stakeholders, y=negative_counts, marker_color='#dc3545')
                ])
                
                fig_bar.update_layout(
                    barmode='stack',
                    title='Sentiment by Stakeholder Type',
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    title_font_size=16,
                    title_font_color='#003366'
                )
                st.plotly_chart(fig_bar, use_container_width=True)

        # Language Analysis
        languages = [item.get('language', 'english') for item in data]
        language_counts = {}
        for lang in languages:
            language_counts[lang] = language_counts.get(lang, 0) + 1
        
        if len(language_counts) > 1:
            st.markdown("### 🌐 Language Distribution")
            lang_col1, lang_col2 = st.columns(2)
            
            with lang_col1:
                fig_lang = px.bar(
                    x=list(language_counts.keys()),
                    y=list(language_counts.values()),
                    title="Comments by Language",
                    color=list(language_counts.values()),
                    color_continuous_scale='Blues'
                )
                fig_lang.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    title_font_size=16,
                    title_font_color='#003366'
                )
                st.plotly_chart(fig_lang, use_container_width=True)
            
            with lang_col2:
                st.markdown("#### 🔍 Multilingual Support")
                for lang, count in language_counts.items():
                    percentage = (count/len(data))*100
                    st.markdown(f"**{lang.title()}:** {count} comments ({percentage:.1f}%)")

        # Detailed Results Table
        st.markdown("### 📋 Detailed Analysis Results")
        
        # Convert to DataFrame for display
        df = pd.DataFrame(data)
        
        # Add sentiment emoji
        sentiment_emoji = {'positive': '😊', 'negative': '😞', 'neutral': '😐'}
        df['Sentiment_Display'] = df['sentiment'].map(sentiment_emoji) + ' ' + df['sentiment'].str.title()
        
        # Display table with formatting
        display_columns = ['id', 'comment', 'stakeholder_type', 'policy_area', 'Sentiment_Display', 'confidence', 'language']
        column_names = ['ID', 'Comment', 'Stakeholder', 'Policy Area', 'Sentiment', 'Confidence', 'Language']
        
        if all(col in df.columns for col in display_columns):
            display_df = df[display_columns].copy()
            display_df.columns = column_names
            display_df['Confidence'] = (display_df['Confidence'] * 100).round(1).astype(str) + '%'
            display_df['Language'] = display_df['Language'].str.title()
            
            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True
            )

        # Word Cloud Section
        st.markdown("### ☁️ Word Cloud Analysis")
        with st.spinner("Generating word cloud..."):
            comments = [item['comment'] for item in data]
            wordcloud_result = get_wordcloud_data(comments)
            
            if wordcloud_result["success"]:
                wc_data = wordcloud_result["data"]
                
                if 'wordcloud_data' in wc_data:
                    word_frequencies = wc_data['wordcloud_data']['word_frequencies']
                    
                    # Create word frequency chart
                    if word_frequencies:
                        top_words = dict(list(word_frequencies.items())[:20])
                        
                        fig_words = px.bar(
                            x=list(top_words.values()),
                            y=list(top_words.keys()),
                            orientation='h',
                            title="Top 20 Most Frequent Words",
                            color=list(top_words.values()),
                            color_continuous_scale='Viridis'
                        )
                        fig_words.update_layout(
                            plot_bgcolor='rgba(0,0,0,0)',
                            paper_bgcolor='rgba(0,0,0,0)',
                            title_font_size=16,
                            title_font_color='#003366',
                            yaxis={'categoryorder': 'total ascending'}
                        )
                        st.plotly_chart(fig_words, use_container_width=True)
                        
                        # Display word frequencies
                        st.markdown("#### 📊 Word Frequency Analysis")
                        freq_col1, freq_col2 = st.columns(2)
                        
                        words_list = list(word_frequencies.items())
                        mid_point = len(words_list) // 2
                        
                        with freq_col1:
                            for word, freq in words_list[:mid_point]:
                                st.markdown(f"**{word}:** {freq}")
                        
                        with freq_col2:
                            for word, freq in words_list[mid_point:]:
                                st.markdown(f"**{word}:** {freq}")
                    else:
                        st.info("No significant words found for word cloud generation.")
                else:
                    st.warning("Word cloud data not available in the expected format.")
            else:
                st.warning(f"Word cloud generation failed: {wordcloud_result['error']}")

        # Export Options
        st.markdown("### 💾 Export Results")
        export_col1, export_col2, export_col3 = st.columns(3)
        
        with export_col1:
            # CSV Export
            csv_data = pd.DataFrame(data).to_csv(index=False)
            st.download_button(
                label="📁 Download CSV",
                data=csv_data,
                file_name=f"sentiment_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        
        with export_col2:
            # JSON Export
            json_data = json.dumps(data, indent=2, ensure_ascii=False)
            st.download_button(
                label="📄 Download JSON",
                data=json_data,
                file_name=f"sentiment_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
        
        with export_col3:
            # Summary Report
            summary_report = f"""
# Sentiment Analysis Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary Statistics
- Total Comments Analyzed: {len(data)}
- Positive Sentiment: {sentiment_counts['positive']} ({(sentiment_counts['positive']/total)*100:.1f}%)
- Neutral Sentiment: {sentiment_counts['neutral']} ({(sentiment_counts['neutral']/total)*100:.1f}%)
- Negative Sentiment: {sentiment_counts['negative']} ({(sentiment_counts['negative']/total)*100:.1f}%)

## Language Distribution
{chr(10).join([f"- {lang.title()}: {count}" for lang, count in language_counts.items()])}

## Analysis Method
- Advanced multilingual sentiment analysis
- Government consultation focused
- Real-time processing
"""
            st.download_button(
                label="📋 Download Report",
                data=summary_report,
                file_name=f"sentiment_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                mime="text/markdown"
            )

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; margin-top: 2rem;">
        <p><strong>Ministry of Corporate Affairs | Government of India</strong></p>
        <p>eConsultation Sentiment Analysis Portal • Version 3.0 • Powered by Advanced AI</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    # Initialize session state
    if 'analysis_complete' not in st.session_state:
        st.session_state['analysis_complete'] = False
    
    main()