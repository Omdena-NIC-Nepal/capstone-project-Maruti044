import streamlit as st
import pandas as pd

def show_reports():
    st.title("Reports")
    
    # Load report data (can be pre-generated reports or summaries)
    df = pd.read_csv("data/processed_climate_data.csv")
    
    st.subheader("Climate Data Summary")
    st.write(df.describe())
    
    # Generate and download report
    st.subheader("Download Climate Report")
    report_button = st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False),
        file_name="climate_data_report.csv",
        mime="text/csv"
    )
