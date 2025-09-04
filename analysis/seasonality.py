import pandas as pd
import numpy as np

def decompose_trend(monthly_df: pd.DataFrame, value_col: str = "revenue") -> pd.DataFrame:
    df = monthly_df.copy().reset_index(drop=True)
    df["trend"] = df[value_col].rolling(3, center=True).mean()
    df["detrended"] = df[value_col] - df["trend"]
    df["seasonal_index"] = df["detrended"] / df["trend"]
    return df

def peak_months(df: pd.DataFrame) -> pd.Series:
    df = df.copy()
    df["month_num"] = pd.PeriodIndex(df["month"].astype(str), freq="M").month
    return df.groupby("month_num")["revenue"].mean().idxmax()
