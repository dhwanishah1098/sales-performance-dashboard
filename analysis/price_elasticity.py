def estimate_elasticity(pct_qty_change, pct_price_change):
    if not pct_price_change: return None
    return round(pct_qty_change / pct_price_change, 3)
