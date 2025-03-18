import pandas as pd
from config import DATA_PATH


def load_sales_data(filepath: str = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=["order_date"])
    df["month"] = df["order_date"].dt.to_period("M")
    df["quarter"] = df["order_date"].dt.to_period("Q")
    df["year"] = df["order_date"].dt.year
    df["revenue"] = df["units_sold"] * df["unit_price"]
    df["margin"] = (df["unit_price"] - df["unit_cost"]) / df["unit_price"]
    return df


def filter_by_period(df: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    mask = (df["order_date"] >= start) & (df["order_date"] <= end)
    return df.loc[mask].copy()


def get_region_summary(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("region").agg(
        revenue=("revenue", "sum"),
        units=("units_sold", "sum"),
        avg_margin=("margin", "mean"),
        orders=("order_id", "nunique")
    ).reset_index().sort_values("revenue", ascending=False)
