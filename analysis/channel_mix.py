def channel_mix(df):
    return df.groupby('channel')['revenue'].sum() / df['revenue'].sum() * 100
