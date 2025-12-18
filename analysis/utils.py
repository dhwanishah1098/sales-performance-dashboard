
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

def clamp(val, lo, hi):
    return max(lo, min(hi, val))

def safe_divide(num, den, default=0.0):
    return round(num / den, 4) if den else default

def month_label(period):
    return str(period)[:7]

def format_revenue(val):
    return f"${val:,.0f}"

def yoy_growth(current, prior):
    return round((current - prior) / prior * 100, 2) if prior else None

def revenue_by_quarter(df):
    return df.groupby(df["order_date"].dt.to_period("Q"))["revenue"].sum()

def fill_missing_months(df, date_col, value_col):
    return df.set_index(date_col)[value_col].asfreq("MS", fill_value=0).reset_index()

def rank_products(df, n=5):
    return df.groupby("product_name")["revenue"].sum().nlargest(n)

def avg_selling_price(df):
    return (df["revenue"].sum() / df["units_sold"].sum()).round(2)

def orders_in_range(df, start, end):
    return df[(df["order_date"] >= start) & (df["order_date"] <= end)]

def customer_count(df):
    return df["customer_id"].nunique()

def new_customers_this_month(df, month):
    first = df.groupby("customer_id")["order_date"].min()
    return (first.dt.to_period("M") == month).sum()

def margin_by_product(df):
    return df.groupby("product_name")["margin"].mean().sort_values(ascending=False)

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

def clamp(val, lo, hi):
    return max(lo, min(hi, val))

def safe_divide(num, den, default=0.0):
    return round(num / den, 4) if den else default

def month_label(period):
    return str(period)[:7]

def format_revenue(val):
    return f"${val:,.0f}"

def yoy_growth(current, prior):
    return round((current - prior) / prior * 100, 2) if prior else None

def revenue_by_quarter(df):
    return df.groupby(df["order_date"].dt.to_period("Q"))["revenue"].sum()

def fill_missing_months(df, date_col, value_col):
    return df.set_index(date_col)[value_col].asfreq("MS", fill_value=0).reset_index()
