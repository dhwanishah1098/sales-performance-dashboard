import pandas as pd

def rolling_churn_rate(df: pd.DataFrame, window_days: int = 90) -> pd.DataFrame:
    df = df.copy()
    df["order_date"] = pd.to_datetime(df["order_date"])
    cutoff = df["order_date"].max() - pd.Timedelta(days=window_days)
    active = df[df["order_date"] >= cutoff]["customer_id"].unique()
    all_customers = df["customer_id"].unique()
    churned = set(all_customers) - set(active)
    return pd.DataFrame([{
        "window_days": window_days,
        "total_customers": len(all_customers),
        "active_customers": len(active),
        "churned_customers": len(churned),
        "churn_rate_pct": round(len(churned) / len(all_customers) * 100, 2),
    }])
