import pandas as pd

def simple_ltv(df: pd.DataFrame, churn_rate: float = 0.05, margin: float = 0.35) -> pd.DataFrame:
    cust = df.groupby("customer_id").agg(
        avg_order_value=("revenue","mean"),
        purchase_frequency=("order_id","count"),
    ).reset_index()
    cust["ltv"] = (cust["avg_order_value"] * cust["purchase_frequency"] * margin / churn_rate).round(2)
    return cust.sort_values("ltv", ascending=False)
