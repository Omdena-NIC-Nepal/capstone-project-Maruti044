import geopandas as gpd
from shapely.geometry import Point

def compute_spatial_proximity(gdf: gpd.GeoDataFrame, target_point: Point, col_name='distance_to_point') -> gpd.GeoDataFrame:
    """Compute distance from each point to a target location."""
    gdf[col_name] = gdf.geometry.distance(target_point)
    return gdf

def spatial_join_with_admin_boundaries(gdf: gpd.GeoDataFrame, admin_boundaries: gpd.GeoDataFrame, how='left') -> gpd.GeoDataFrame:
    """Perform spatial join with administrative boundaries (e.g., districts)."""
    return gpd.sjoin(gdf, admin_boundaries, how=how, predicate='intersects')
