import streamlit as st

def apply_filters(df):
    """Applies filters to the dataset."""
    st.title("Filters")
    
    # Filter by year
    year = st.slider("Select Year", min_value=2000, max_value=2025, value=2020)
    df = df[df['Year'] == year]
    
    # Filter by region
    region = st.selectbox("Select Region", df['Region'].unique())
    df = df[df['Region'] == region]
    
    return df
