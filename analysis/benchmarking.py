import pandas as pd

def benchmark_regions(df: pd.DataFrame, target_margin: float = 0.35) -> pd.DataFrame:
    region = df.groupby("region").agg(
        revenue=("revenue","sum"), avg_margin=("margin","mean"), orders=("order_id","nunique")
    ).reset_index()
    region["vs_target_margin"] = (region["avg_margin"] - target_margin).round(4)
    region["status"] = region["avg_margin"].apply(
        lambda m: "Above Target" if m >= target_margin else "Below Target"
    )
    return region

def benchmark_products(df: pd.DataFrame, n_top: int = 10) -> pd.DataFrame:
    prod = df.groupby("product_name").agg(
        revenue=("revenue","sum"), margin=("margin","mean")
    ).sort_values("revenue", ascending=False).head(n_top).reset_index()
    prod["revenue_rank"] = range(1, len(prod)+1)
    return prod
