"""
Run full pipeline for preprocessing, EDA, and feature engineering on climate data.
"""

import pandas as pd
import geopandas as gpd
from cleaner import clean_data
from normalizer import normalize_data
from aligner import align_temporal_data
from geo_structure import create_geospatial_structure
from temperature_analysis import plot_temperature_trend_by_region, plot_temp_vs_elevation
from precipitation_visuals import plot_monthly_precipitation, plot_precipitation_trend
from extreme_events import detect_extreme_temperatures, plot_extreme_event_frequency
from glacial_retreat import plot_glacial_retreat
from correlation_analysis import plot_correlation_matrix, compute_statistical_correlations
from climate_indices import compute_drought_index, compute_heat_stress_index
from seasonal_indicators import add_seasonal_indicators
from time_series_features import add_lag_features, add_rolling_features
from spatial_features import compute_spatial_proximity, spatial_join_with_admin_boundaries
from dimensionality import normalize_features, apply_pca

# File paths
RAW_DATA_PATH = 'data/raw/climate_raw.csv'
PROCESSED_DATA_PATH = 'data/processed/climate_processed.gpkg'
ADMIN_BOUNDARIES_PATH = 'data/spatial/admin_boundaries.shp'  # Example spatial file for spatial joins

def run_pipeline():
    print("📥 Loading raw data...")
    df_raw = pd.read_csv(RAW_DATA_PATH)

    print("📥 Loading processed geospatial data...")
    df_processed = gpd.read_file(PROCESSED_DATA_PATH)

    # 1. Data Preprocessing
    print("🔧 Cleaning data...")
    df_clean = clean_data(df_raw)
    df_clean = normalize_data(df_clean)
    df_clean = align_temporal_data(df_clean)
    df_clean = create_geospatial_structure(df_clean)

    # 2. Feature Engineering
    print("⚙️ Engineering features...")

    # Compute climate indices
    df_clean['drought_index'] = compute_drought_index(df_clean)
    df_clean['heat_stress_index'] = compute_heat_stress_index(df_clean)

    # Add seasonal indicators (Monsoon, Season)
    df_clean = add_seasonal_indicators(df_clean)

    # Add time-series features (Lags, Rolling means)
    df_clean = add_lag_features(df_clean, cols=['temperature', 'precipitation'], lags=[1, 2, 3])
    df_clean = add_rolling_features(df_clean, cols=['temperature', 'precipitation'], windows=[3, 6])

    # Spatial features (Proximity to specific location, spatial join with admin boundaries)
    target_point = gpd.GeoSeries([Point(85.3240, 27.7172)])  # Example coordinate for Kathmandu
    df_clean = compute_spatial_proximity(df_processed, target_point)
    admin_boundaries = gpd.read_file(ADMIN_BOUNDARIES_PATH)
    df_clean = spatial_join_with_admin_boundaries(df_processed, admin_boundaries)

    # Dimensionality Reduction (PCA)
    df_clean = normalize_features(df_clean, cols=['temperature', 'precipitation', 'elevation'])
    df_clean = apply_pca(df_clean, cols=['temperature', 'precipitation', 'elevation'], n_components=2)

    # 3. Exploratory Data Analysis
    print("🌡️ Analyzing Temperature Trends...")
    plot_temperature_trend_by_region(df_clean, region_col='region', temp_col='temperature')
    plot_temp_vs_elevation(df_clean, temp_col='temperature', elev_col='elevation')

    print("🌧️ Analyzing Precipitation Patterns...")
    plot_monthly_precipitation(df_clean, date_col='date', precip_col='precipitation')
    plot_precipitation_trend(df_clean, region_col='region', date_col='date', precip_col='precipitation')

    print("🔥 Detecting Extreme Weather Events...")
    extremes = detect_extreme_temperatures(df_clean, threshold_high=35, threshold_low=0, temp_col='temperature')
    print(f"Detected {len(extremes)} extreme temperature events.")
    plot_extreme_event_frequency(df_clean, temp_col='temperature', date_col='date', threshold=35)

    print("🧊 Analyzing Glacial Retreat...")
    plot_glacial_retreat(df_raw, date_col='date', area_col='glacier_area')

    print("🔗 Performing Correlation Analysis...")
    variables = ['temperature', 'precipitation', 'elevation', 'glacier_area']
    plot_correlation_matrix(df_clean, variables)
    corrs = compute_statistical_correlations(df_clean, 'temperature', 'glacier_area')
    print(f"Correlation (Temperature vs Glacier Area): {corrs}")

if __name__ == "__main__":
    run_pipeline()
