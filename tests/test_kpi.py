import pytest
import pandas as pd
from analysis.kpi import calculate_kpis, month_over_month


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "order_id": [1, 2, 3, 4],
        "order_date": pd.to_datetime(["2024-01-05", "2024-01-15", "2024-02-10", "2024-02-20"]),
        "units_sold": [10, 5, 8, 3],
        "unit_price": [100, 200, 150, 300],
        "unit_cost": [60, 120, 90, 180],
        "region": ["North", "South", "North", "East"],
        "product_name": ["A", "B", "A", "C"],
    })


def test_calculate_kpis(sample_df):
    sample_df["revenue"] = sample_df["units_sold"] * sample_df["unit_price"]
    sample_df["margin"] = (sample_df["unit_price"] - sample_df["unit_cost"]) / sample_df["unit_price"]
    sample_df["month"] = sample_df["order_date"].dt.to_period("M")
    kpis = calculate_kpis(sample_df)
    assert kpis["total_units"] == 26
    assert kpis["avg_margin"] == pytest.approx(0.4, 0.01)
