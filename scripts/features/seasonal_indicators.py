import pandas as pd

def add_seasonal_indicators(df: pd.DataFrame, date_col='date') -> pd.DataFrame:
    """Add monsoon and seasonal indicators based on month."""
    df['month'] = pd.to_datetime(df[date_col]).dt.month
    df['is_monsoon'] = df['month'].isin([6, 7, 8, 9])
    df['season'] = df['month'].map({
        12: 'Winter', 1: 'Winter', 2: 'Winter',
        3: 'Spring', 4: 'Spring', 5: 'Spring',
        6: 'Summer', 7: 'Summer', 8: 'Summer',
        9: 'Autumn', 10: 'Autumn', 11: 'Autumn'
    })
    return df
