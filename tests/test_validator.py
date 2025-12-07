import pandas as pd
import pytest
from data.validator import validate_schema, validate_no_nulls, run_all_checks

@pytest.fixture
def valid_df():
    return pd.DataFrame({
        "order_id": ["O1","O2"],
        "order_date": pd.to_datetime(["2024-01-01","2024-01-02"]),
        "customer_id": ["C1","C2"],
        "product_name": ["A","B"],
        "units_sold": [1,2],
        "unit_price": [100.0,200.0],
        "unit_cost": [60.0,120.0],
        "region": ["North","South"],
        "revenue": [100.0, 400.0],
        "margin": [0.4, 0.4],
    })

def test_valid_schema(valid_df):
    assert validate_schema(valid_df) == []

def test_no_nulls(valid_df):
    assert validate_no_nulls(valid_df, ["order_id","revenue"]) == {}
