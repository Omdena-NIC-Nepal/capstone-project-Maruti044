import streamlit as st
from pages.home import show
from pages.trends import show_trends
from pages.predictions import show_predictions
from pages.reports import show_reports
import streamlit as st


def main():
    st.set_page_config(page_title="Climate Change Dashboard", page_icon="??", layout="wide")
    
    # Sidebar navigation
    st.sidebar.title("Climate Change Dashboard")
    page = st.sidebar.radio("Select a page", ["Home", "Trends", "Predictions", "Reports"])

    # Display the selected page
    if page == "Home":
        show()
    elif page == "Trends":
        show_trends()
    elif page == "Predictions":
        show_predictions()
    elif page == "Reports":
        show_reports()

if __name__ == "__main__":
    main()