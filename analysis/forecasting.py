import pandas as pd
import numpy as np


def simple_trend_forecast(monthly_df: pd.DataFrame, periods: int = 3) -> pd.DataFrame:
    revenue = monthly_df["revenue"].values
    x = np.arange(len(revenue))
    slope, intercept = np.polyfit(x, revenue, 1)
    forecast_x = np.arange(len(revenue), len(revenue) + periods)
    forecast_values = slope * forecast_x + intercept
    last_period = monthly_df["month"].iloc[-1]
    future_periods = [last_period + i + 1 for i in range(periods)]
    return pd.DataFrame({"month": future_periods, "forecast_revenue": forecast_values.round(2)})


def seasonality_index(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["month_num"] = df["order_date"].dt.month
    monthly_avg = df.groupby("month_num")["revenue"].mean()
    overall_avg = df["revenue"].mean()
    index = (monthly_avg / overall_avg).reset_index()
    index.columns = ["month_num", "seasonality_index"]
    return index
