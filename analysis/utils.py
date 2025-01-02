
def revenue_per_customer(df):
    return df.groupby("customer_id")["revenue"].sum().mean().round(2)
