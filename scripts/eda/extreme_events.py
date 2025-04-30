"""
Identifies and visualizes extreme weather events.
"""

import pandas as pd
import matplotlib.pyplot as plt

def detect_extreme_temperatures(df: pd.DataFrame, threshold_high=40, threshold_low=-5, temp_col='temperature'):
    """Marks extreme high and low temperature events."""
    extremes = df[(df[temp_col] > threshold_high) | (df[temp_col] < threshold_low)]
    return extremes

def plot_extreme_event_frequency(df: pd.DataFrame, temp_col='temperature', date_col='date', threshold=40):
    """Bar plot of number of extreme heat events per year."""
    df[date_col] = pd.to_datetime(df[date_col])
    df['year'] = df[date_col].dt.year
    extreme_counts = df[df[temp_col] > threshold].groupby('year').size()

    plt.figure(figsize=(10, 5))
    extreme_counts.plot(kind='bar', color='crimson')
    plt.title(f"Extreme Heat Events per Year (>{threshold}°C)")
    plt.xlabel("Year")
    plt.ylabel("Number of Events")
    plt.tight_layout()
    plt.show()
