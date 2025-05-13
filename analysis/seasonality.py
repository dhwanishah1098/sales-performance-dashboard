import pandas as pd
def seasonal_index(df, date_col='order_date', value_col='revenue'):
    df['month'] = pd.to_datetime(df[date_col]).dt.month
    monthly_avg = df.groupby('month')[value_col].mean()
    return (monthly_avg / monthly_avg.mean()).round(3)
