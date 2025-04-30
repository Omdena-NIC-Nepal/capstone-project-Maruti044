import pandas as pd

def add_lag_features(df: pd.DataFrame, cols: list, lags: list) -> pd.DataFrame:
    """Add lag features for time-series forecasting."""
    for col in cols:
        for lag in lags:
            df[f'{col}_lag_{lag}'] = df[col].shift(lag)
    return df

def add_rolling_features(df: pd.DataFrame, cols: list, windows: list) -> pd.DataFrame:
    """Add rolling mean features."""
    for col in cols:
        for win in windows:
            df[f'{col}_roll_mean_{win}'] = df[col].rolling(window=win).mean()
    return df
