
def revenue_per_customer(df):
    return df.groupby("customer_id")["revenue"].sum().mean().round(2)

def orders_per_day(df):
    return df.groupby("order_date")["order_id"].nunique()

def active_regions(df):
    return sorted(df["region"].dropna().unique().tolist())
