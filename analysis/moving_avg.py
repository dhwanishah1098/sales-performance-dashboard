import pandas as pd
def rolling_avg(df, col, window=4):
    return df[col].rolling(window, min_periods=1).mean()
