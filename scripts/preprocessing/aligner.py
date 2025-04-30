"""
Aligns datasets temporally and handles missing timepoints.
"""

import pandas as pd

def temporal_align(df: pd.DataFrame, datetime_col: str, freq: str = 'M') -> pd.DataFrame:
    """
    Resample the dataset to the desired frequency (e.g., monthly 'M', daily 'D') and fill missing dates.
    """
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    df = df.set_index(datetime_col)
    df_aligned = df.resample(freq).mean()
    df_aligned = df_aligned.interpolate(method='linear')
    df_aligned = df_aligned.reset_index()
    return df_aligned

def merge_time_series(dfs: list, datetime_col: str, how: str = 'outer') -> pd.DataFrame:
    """
    Merge multiple time series dataframes based on datetime.
    """
    merged_df = dfs[0]
    for df in dfs[1:]:
        merged_df = pd.merge(merged_df, df, on=datetime_col, how=how)
    merged_df = merged_df.sort_values(by=datetime_col)
    return merged_df
