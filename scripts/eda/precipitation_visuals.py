"""
Visualizes precipitation patterns and their change over time.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_precipitation(df: pd.DataFrame, date_col='date', precip_col='precipitation'):
    """Shows monthly average precipitation over years."""
    df[date_col] = pd.to_datetime(df[date_col])
    df['month'] = df[date_col].dt.month
    df_grouped = df.groupby('month')[precip_col].mean().reset_index()

    plt.figure(figsize=(10, 5))
    sns.barplot(data=df_grouped, x='month', y=precip_col, palette='Blues')
    plt.title("Average Monthly Precipitation")
    plt.xlabel("Month")
    plt.ylabel("Precipitation (cm)")
    plt.tight_layout()
    plt.show()

def plot_precipitation_trend(df: pd.DataFrame, region_col='region', date_col='date', precip_col='precipitation'):
    """Line plot of precipitation trends over time by region."""
    df[date_col] = pd.to_datetime(df[date_col])
    df_grouped = df.groupby([pd.Grouper(key=date_col, freq='Y'), region_col])[precip_col].mean().reset_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_grouped, x=date_col, y=precip_col, hue=region_col)
    plt.title("Precipitation Trends by Region")
    plt.xlabel("Year")
    plt.ylabel("Precipitation (cm)")
    plt.tight_layout()
    plt.show()
