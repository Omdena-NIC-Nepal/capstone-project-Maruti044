"""
Run full EDA using actual preprocessed and raw climate datasets.
"""

import pandas as pd
import geopandas as gpd
from temperature_analysis import plot_temperature_trend_by_region, plot_temp_vs_elevation
from precipitation_visuals import plot_monthly_precipitation, plot_precipitation_trend
from extreme_events import detect_extreme_temperatures, plot_extreme_event_frequency
from glacial_retreat import plot_glacial_retreat
from correlation_analysis import plot_correlation_matrix, compute_statistical_correlations

# File paths
RAW_DATA_PATH = 'data/raw/climate_raw.csv'
PROCESSED_DATA_PATH = 'data/processed/climate_processed.gpkg'

def run_eda():
    print("📥 Loading raw data...")
    df_raw = pd.read_csv(RAW_DATA_PATH)

    print("📥 Loading processed geospatial data...")
    df_processed = gpd.read_file(PROCESSED_DATA_PATH)

    # Temperature Analysis
    print("🌡️ Analyzing Temperature Trends...")
    plot_temperature_trend_by_region(df_processed, region_col='region', temp_col='temperature')
    plot_temp_vs_elevation(df_processed, temp_col='temperature', elev_col='elevation')

    # Precipitation Analysis
    print("🌧️ Analyzing Precipitation Patterns...")
    plot_monthly_precipitation(df_raw, date_col='date', precip_col='precipitation')
    plot_precipitation_trend(df_raw, region_col='region', date_col='date', precip_col='precipitation')

    # Extreme Weather Events
    print("🔥 Detecting Extreme Temperature Events...")
    extremes = detect_extreme_temperatures(df_processed, threshold_high=35, threshold_low=0, temp_col='temperature')
    print(f"Detected {len(extremes)} extreme temperature events.")
    plot_extreme_event_frequency(df_processed, temp_col='temperature', date_col='date', threshold=35)

    # Glacial Retreat
    print("🧊 Analyzing Glacial Retreat...")
    plot_glacial_retreat(df_raw, date_col='date', area_col='glacier_area')

    # Correlation Analysis
    print("🔗 Performing Correlation Analysis...")
    variables = ['temperature', 'precipitation', 'elevation', 'glacier_area']
    plot_correlation_matrix(df_processed, variables)
    corrs = compute_statistical_correlations(df_processed, 'temperature', 'glacier_area')
    print(f"Correlation (Temperature vs Glacier Area): {corrs}")

if __name__ == "__main__":
    run_eda()
