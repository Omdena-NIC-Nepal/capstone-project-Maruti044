"""
Example pipeline to clean, normalize, align, and geo-structure climate datasets.
"""

import pandas as pd
from cleaner import clean_data
from normalizer import convert_units, standardize
from aligner import temporal_align
from geo_structure import create_geodataframe, validate_coordinates, save_geodata

def run_pipeline(csv_path: str, datetime_col: str = 'date',
                 lon_col: str = 'longitude', lat_col: str = 'latitude',
                 output_gpkg: str = 'processed_data.gpkg'):
    print("🔍 Loading data...")
    df = pd.read_csv(csv_path)

    print("🧹 Cleaning data...")
    df = clean_data(df)

    print("⚖️ Converting units...")
    df = convert_units(df)

    print("📊 Standardizing data...")
    df_scaled = standardize(df.select_dtypes(include=['float64', 'int64']))
    df.update(df_scaled)

    print("🕒 Aligning temporally...")
    df = temporal_align(df, datetime_col)

    print("🗺️ Structuring geospatially...")
    gdf = create_geodataframe(df, lon_col, lat_col)
    gdf = validate_coordinates(gdf)

    print("💾 Saving as GeoPackage...")
    save_geodata(gdf, output_gpkg)

    print(f"✅ Pipeline completed. Output saved to: {output_gpkg}")

# Example usage:
if __name__ == "__main__":
    run_pipeline('data/climate_sample.csv')
