
def revenue_per_customer(df):
    return df.groupby("customer_id")["revenue"].sum().mean().round(2)

def orders_per_day(df):
    return df.groupby("order_date")["order_id"].nunique()

def active_regions(df):
    return sorted(df["region"].dropna().unique().tolist())

def top_region(df):
    return df.groupby("region")["revenue"].sum().idxmax()

def units_per_order(df):
    return (df.groupby("order_id")["units_sold"].sum().mean()).round(2)

def weekly_revenue(df):
    return df.resample("W", on="order_date")["revenue"].sum()

def pct_change(a, b):
    return round((b - a) / a * 100, 2) if a else 0.0
