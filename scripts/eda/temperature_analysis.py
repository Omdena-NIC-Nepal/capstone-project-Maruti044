"""
Analyzes temperature trends across regions and elevations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_temperature_trend_by_region(df: pd.DataFrame, region_col='region', temp_col='temperature'):
    """Line plot of average temperature over time for each region."""
    df['date'] = pd.to_datetime(df['date'])
    df_grouped = df.groupby([pd.Grouper(key='date', freq='Y'), region_col])[temp_col].mean().reset_index()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_grouped, x='date', y=temp_col, hue=region_col)
    plt.title("Temperature Trends by Region")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.show()

def plot_temp_vs_elevation(df: pd.DataFrame, temp_col='temperature', elev_col='elevation'):
    """Scatter plot of temperature vs elevation."""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=elev_col, y=temp_col)
    plt.title("Temperature vs Elevation")
    plt.xlabel("Elevation (m)")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.show()
