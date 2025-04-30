import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def normalize_features(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Standardize numerical features."""
    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df

def apply_pca(df: pd.DataFrame, cols: list, n_components=2) -> pd.DataFrame:
    """Apply PCA for dimensionality reduction."""
    pca = PCA(n_components=n_components)
    pca_components = pca.fit_transform(df[cols])
    for i in range(n_components):
        df[f'pca_{i+1}'] = pca_components[:, i]
    return df
