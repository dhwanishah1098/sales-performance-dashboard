import pandas as pd
import numpy as np

def estimate_elasticity(df: pd.DataFrame, price_col: str = "unit_price", qty_col: str = "units_sold") -> float:
    log_price = np.log(df[price_col].replace(0, np.nan).dropna())
    log_qty   = np.log(df[qty_col].replace(0, np.nan).dropna())
    idx = log_price.index.intersection(log_qty.index)
    if len(idx) < 2:
        return float("nan")
    coeffs = np.polyfit(log_price[idx], log_qty[idx], 1)
    return round(coeffs[0], 3)  # price elasticity of demand
