import pandas as pd

def returns_rate(orders_df: pd.DataFrame, returns_df: pd.DataFrame) -> pd.DataFrame:
    merged = (orders_df.groupby("product_name")["order_id"].count()
              .reset_index(name="total_orders")
              .merge(returns_df.groupby("product_name")["return_id"].count()
                    .reset_index(name="total_returns"), on="product_name", how="left"))
    merged["total_returns"] = merged["total_returns"].fillna(0)
    merged["return_rate_pct"] = (merged["total_returns"] / merged["total_orders"] * 100).round(2)
    return merged.sort_values("return_rate_pct", ascending=False)
