def weekly_summary(df):
    df['week'] = df['order_date'].dt.to_period('W')
    return df.groupby('week').agg(revenue=('revenue','sum'), orders=('order_id','count'))
