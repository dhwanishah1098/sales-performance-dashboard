import pandas as pd
import pytest
from analysis.forecasting import simple_trend_forecast

def test_forecast_length():
    df = pd.DataFrame({
        "month": pd.period_range("2024-01", periods=6, freq="M"),
        "revenue": [100000, 105000, 102000, 110000, 115000, 120000]
    })
    result = simple_trend_forecast(df, periods=3)
    assert len(result) == 3
    assert "forecast_revenue" in result.columns
