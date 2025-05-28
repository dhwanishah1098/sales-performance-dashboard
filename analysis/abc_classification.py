import pandas as pd

def abc_classify(df: pd.DataFrame, product_col: str = "product_name", value_col: str = "revenue") -> pd.DataFrame:
    agg = df.groupby(product_col)[value_col].sum().reset_index().sort_values(value_col, ascending=False)
    agg["cumulative_pct"] = agg[value_col].cumsum() / agg[value_col].sum() * 100
    agg["class"] = agg["cumulative_pct"].apply(lambda x: "A" if x <= 70 else ("B" if x <= 90 else "C"))
    return agg
