"""
Computes and visualizes correlations between climate variables and impacts.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(df: pd.DataFrame, variables: list):
    """Plots a heatmap of the correlation matrix for selected variables."""
    corr = df[variables].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', square=True)
    plt.title("Correlation Matrix of Climate Variables")
    plt.tight_layout()
    plt.show()

def compute_statistical_correlations(df: pd.DataFrame, var1: str, var2: str):
    """Computes Pearson and Spearman correlations between two variables."""
    from scipy.stats import pearsonr, spearmanr
    pearson_corr, _ = pearsonr(df[var1], df[var2])
    spearman_corr, _ = spearmanr(df[var1], df[var2])
    return {
        'pearson': round(pearson_corr, 3),
        'spearman': round(spearman_corr, 3)
    }
