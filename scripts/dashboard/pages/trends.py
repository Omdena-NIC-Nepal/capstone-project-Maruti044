import sys
import streamlit as st
import pandas as pd
import geopandas as gpd
sys.path.append("F:/AI traning with Omeda NIc/GroupA/solution/capstone-project-Maruti044/scripts")
from eda.temperature_analysis import plot_temperature_trend_by_region, plot_temp_vs_elevation
from eda.precipitation_visuals import plot_monthly_precipitation, plot_precipitation_trend
from eda.extreme_events import detect_extreme_temperatures, plot_extreme_event_frequency
from eda.glacial_retreat import plot_glacial_retreat
from eda.correlation_analysis import plot_correlation_matrix, compute_statistical_correlations


# File paths
RAW_DATA_PATH = 'data/raw/climate_raw.csv'
PROCESSED_DATA_PATH = 'data/processed/climate_processed.gpkg'

def show_trends():
    st.title("📈 Climate Trends & EDA")

    # Load data
    with st.spinner("📥 Loading raw data..."):
        df_raw = pd.read_csv(RAW_DATA_PATH)
    st.success("Raw data loaded!")

    with st.spinner("📥 Loading processed geospatial data..."):
        df_processed = gpd.read_file(PROCESSED_DATA_PATH)
    st.success("Processed geospatial data loaded!")

    # Temperature Analysis
    st.header("🌡️ Temperature Trends")
    st.subheader("Temperature Trend by Region")
    fig1 = plot_temperature_trend_by_region(df_processed, region_col='region', temp_col='temperature')
    st.pyplot(fig1)

    st.subheader("Temperature vs Elevation")
    fig2 = plot_temp_vs_elevation(df_processed, temp_col='temperature', elev_col='elevation')
    st.pyplot(fig2)

    # Precipitation Analysis
    st.header("🌧️ Precipitation Patterns")
    st.subheader("Monthly Precipitation Trends")
    fig3 = plot_monthly_precipitation(df_raw, date_col='date', precip_col='precipitation')
    st.pyplot(fig3)

    st.subheader("Precipitation Trend by Region")
    fig4 = plot_precipitation_trend(df_raw, region_col='region', date_col='date', precip_col='precipitation')
    st.pyplot(fig4)

    # Extreme Events
    st.header("🔥 Extreme Weather Events")
    st.subheader("Detecting Extreme Temperature Events")
    extremes = detect_extreme_temperatures(df_processed, threshold_high=35, threshold_low=0, temp_col='temperature')
    st.write(f"📌 Detected **{len(extremes)}** extreme temperature events.")

    st.subheader("Extreme Event Frequency Over Time")
    fig5 = plot_extreme_event_frequency(df_processed, temp_col='temperature', date_col='date', threshold=35)
    st.pyplot(fig5)

    # Glacial Retreat
    st.header("🧊 Glacial Retreat Analysis")
    fig6 = plot_glacial_retreat(df_raw, date_col='date', area_col='glacier_area')
    st.pyplot(fig6)

    # Correlation
    st.header("🔗 Correlation Analysis")
    variables = ['temperature', 'precipitation', 'elevation', 'glacier_area']
    fig7 = plot_correlation_matrix(df_processed, variables)
    st.pyplot(fig7)

    corrs = compute_statistical_correlations(df_processed, 'temperature', 'glacier_area')
    st.write(f"📊 **Correlation (Temperature vs Glacier Area)**: `{corrs:.3f}`")
if __name__ == "__main__":
    show_trends()