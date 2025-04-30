"""
Normalizes and standardizes datasets:
- Converts units (if needed)
- Standardizes values (zero mean, unit variance)
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def standardize(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize features by removing mean and scaling to unit variance."""
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df.select_dtypes(include=['float64', 'int64']))
    df_scaled = pd.DataFrame(scaled, columns=df.select_dtypes(include=['float64', 'int64']).columns)
    return df_scaled

def minmax_normalize(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize features to a 0-1 range."""
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df.select_dtypes(include=['float64', 'int64']))
    df_normalized = pd.DataFrame(scaled, columns=df.select_dtypes(include=['float64', 'int64']).columns)
    return df_normalized

def convert_units(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert measurement units:
    - mm to cm for precipitation
    - Kelvin to Celsius for temperature
    """
    if 'precipitation' in df.columns:
        df['precipitation'] = df['precipitation'] / 10  # mm to cm
    if 'temperature' in df.columns:
        df['temperature'] = df['temperature'] - 273.15  # Kelvin to Celsius
    return df
