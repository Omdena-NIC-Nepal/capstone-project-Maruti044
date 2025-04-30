"""
Handles raw data cleaning:
- Remove duplicates
- Handle missing values with imputation
- Outlier detection and removal
"""

import pandas as pd
from sklearn.impute import SimpleImputer

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate records from the dataframe."""
    return df.drop_duplicates()

def impute_missing_values(df: pd.DataFrame, strategy='mean') -> pd.DataFrame:
    """
    Imputes missing values using specified strategy: 'mean', 'median', or 'most_frequent'.
    """
    imputer = SimpleImputer(strategy=strategy)
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    return df_imputed

def remove_outliers(df: pd.DataFrame, z_thresh=3) -> pd.DataFrame:
    """
    Removes outliers based on Z-score threshold.
    """
    from scipy import stats
    z_scores = stats.zscore(df.select_dtypes(include=['float64', 'int64']))
    abs_z_scores = abs(z_scores)
    filtered_entries = (abs_z_scores < z_thresh).all(axis=1)
    return df[filtered_entries]

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Full cleaning pipeline."""
    df = remove_duplicates(df)
    df = impute_missing_values(df)
    df = remove_outliers(df)
    return df
