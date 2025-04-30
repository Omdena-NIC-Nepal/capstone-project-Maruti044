import streamlit as st
import geopandas as gpd

def show_map(gdf):
    """Displays a geospatial map of climate-related data."""
    st.title("Geospatial Map")
    
    st.write("Displaying the geospatial map of climate data...")
    st.map(gdf)
