import pandas as pd

REQUIRED_COLS = ["order_id", "order_date", "customer_id", "product_name",
                 "units_sold", "unit_price", "unit_cost", "region"]

def validate_schema(df: pd.DataFrame) -> list[str]:
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    return missing

def validate_no_nulls(df: pd.DataFrame, cols: list) -> dict:
    return {c: int(df[c].isna().sum()) for c in cols if df[c].isna().any()}

def validate_positive_values(df: pd.DataFrame) -> pd.Series:
    return df[(df["unit_price"] <= 0) | (df["units_sold"] <= 0)].index

def run_all_checks(df: pd.DataFrame) -> dict:
    return {
        "missing_columns": validate_schema(df),
        "null_counts": validate_no_nulls(df, ["order_id", "order_date", "revenue"]),
        "invalid_rows": list(validate_positive_values(df)),
    }
