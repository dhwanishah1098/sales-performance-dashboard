def deseasonalise(df, value_col, seasonal_index):
    df['season_index'] = df['order_date'].dt.month.map(seasonal_index)
    df[f'{value_col}_adj'] = df[value_col] / df['season_index']
    return df
