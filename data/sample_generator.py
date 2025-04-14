import pandas as pd
import numpy as np
from datetime import date, timedelta
import random

REGIONS = ["North","South","East","West","Central"]
PRODUCTS = ["Widget A","Widget B","Widget C","Gadget X","Gadget Y",
            "Tool Pro","Tool Lite","Service Basic","Service Premium","Bundle Pack"]

def generate_sales(n: int = 5000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    start = date(2024, 1, 1)
    dates = [start + timedelta(days=int(d)) for d in rng.integers(0, 365, n)]
    return pd.DataFrame({
        "order_id": [f"ORD-{i:05d}" for i in range(n)],
        "order_date": dates,
        "customer_id": [f"CUST-{rng.integers(100, 1500)}" for _ in range(n)],
        "product_name": [random.choice(PRODUCTS) for _ in range(n)],
        "region": [random.choice(REGIONS) for _ in range(n)],
        "units_sold": rng.integers(1, 20, n),
        "unit_price": rng.uniform(50, 500, n).round(2),
        "unit_cost": rng.uniform(20, 300, n).round(2),
    })

if __name__ == "__main__":
    df = generate_sales()
    df.to_csv("data/sample_sales.csv", index=False)
    print(f"Generated {len(df)} rows -> data/sample_sales.csv")
