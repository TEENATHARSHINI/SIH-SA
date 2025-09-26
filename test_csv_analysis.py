"""
Test our fixed sentiment analysis on CSV data
"""
import pandas as pd
import sys
import os

# Add paths
sys.path.append('.')
sys.path.append('dashboard/components')

try:
    from dashboard.components.file_upload import apply_advanced_sentiment_analysis
    
    print("🧪 TESTING CSV SENTIMENT ANALYSIS")
    print("=" * 50)
    
    # Load test CSV
    df = pd.read_csv('test_row7_data.csv')
    print(f"✅ Loaded CSV with {len(df)} rows")
    
    # Apply sentiment analysis
    print("🔄 Applying advanced sentiment analysis...")
    df_analyzed = apply_advanced_sentiment_analysis(df)
    
    print("\n📊 SENTIMENT ANALYSIS RESULTS:")
    print("-" * 30)
    
    for i, row in df_analyzed.iterrows():
        comment = row['comment'][:60] + "..." if len(row['comment']) > 60 else row['comment']
        sentiment = row['sentiment'].upper()
        confidence = row['confidence'] * 100
        
        status = ""
        if i == 6:  # Row 7 (0-indexed as 6)
            status = " 🎯 ROW 7" + (" ✅ CORRECT" if sentiment == "NEGATIVE" else " ❌ WRONG")
        
        print(f"Row {i+1}: {sentiment} ({confidence:.1f}%){status}")
        print(f"   Text: {comment}")
        print()
    
    # Verify Row 7 specifically
    row_7 = df_analyzed.iloc[6]
    row_7_sentiment = row_7['sentiment']
    
    print("🎯 ROW 7 VALIDATION:")
    print(f"Expected: NEGATIVE")
    print(f"Got: {row_7_sentiment.upper()}")
    print(f"Result: {'✅ PERFECT!' if row_7_sentiment.lower() == 'negative' else '❌ NEEDS FIX!'}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()