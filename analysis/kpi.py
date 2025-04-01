import pandas as pd
import numpy as np
from config import REVENUE_TARGET_MONTHLY, TARGET_MARGIN


def calculate_kpis(df: pd.DataFrame) -> dict:
    total_revenue = df["revenue"].sum()
    total_units = df["units_sold"].sum()
    avg_order_value = total_revenue / df["order_id"].nunique()
    avg_margin = df["margin"].mean()
    return {
        "total_revenue": round(total_revenue, 2),
        "total_units": int(total_units),
        "avg_order_value": round(avg_order_value, 2),
        "avg_margin": round(avg_margin, 4),
        "revenue_vs_target": round(total_revenue / REVENUE_TARGET_MONTHLY, 3),
        "margin_vs_target": round(avg_margin / TARGET_MARGIN, 3),
    }


def month_over_month(df: pd.DataFrame) -> pd.DataFrame:
    monthly = df.groupby("month")["revenue"].sum().reset_index()
    monthly["prev_revenue"] = monthly["revenue"].shift(1)
    monthly["mom_growth"] = (monthly["revenue"] - monthly["prev_revenue"]) / monthly["prev_revenue"]
    return monthly


def top_products(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    return (
        df.groupby("product_name")
        .agg(revenue=("revenue", "sum"), units=("units_sold", "sum"))
        .sort_values("revenue", ascending=False)
        .head(n)
        .reset_index()
    )


def sales_velocity(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["week"] = df["order_date"].dt.isocalendar().week
    return df.groupby(["year", "week"])["units_sold"].sum().reset_index()
