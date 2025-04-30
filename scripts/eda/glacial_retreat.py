"""
Analyzes glacial retreat over time using area or volume data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_glacial_retreat(df: pd.DataFrame, date_col='date', area_col='glacier_area'):
    """Plots glacial area decline over time."""
    df[date_col] = pd.to_datetime(df[date_col])
    df_grouped = df.groupby(pd.Grouper(key=date_col, freq='Y'))[area_col].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_grouped, x=date_col, y=area_col)
    plt.title("Glacial Area Retreat Over Time")
    plt.xlabel("Year")
    plt.ylabel("Average Glacier Area (km²)")
    plt.tight_layout()
    plt.show()
