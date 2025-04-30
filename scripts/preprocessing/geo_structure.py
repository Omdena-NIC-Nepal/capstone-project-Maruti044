"""
Create and validate georeferenced dataset structures for spatial analysis.
"""

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

def create_geodataframe(df: pd.DataFrame, lon_col: str = 'longitude', lat_col: str = 'latitude') -> gpd.GeoDataFrame:
    """
    Converts a DataFrame with longitude and latitude columns into a GeoDataFrame.
    """
    geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry)
    gdf.set_crs(epsg=4326, inplace=True)  # WGS84
    return gdf

def validate_coordinates(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Validates that coordinates are within acceptable bounds (longitude: -180 to 180, latitude: -90 to 90).
    """
    valid = (gdf.geometry.x >= -180) & (gdf.geometry.x <= 180) & \
            (gdf.geometry.y >= -90) & (gdf.geometry.y <= 90)
    return gdf[valid]

def save_geodata(gdf: gpd.GeoDataFrame, path: str):
    """
    Saves the GeoDataFrame to a GeoPackage file.
    """
    gdf.to_file(path, driver="GPKG")
