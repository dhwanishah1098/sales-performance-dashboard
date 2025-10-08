import pandas as pd

def conversion_funnel(df: pd.DataFrame, stages: list) -> pd.DataFrame:
    counts = {s: df[df["stage"] == s]["user_id"].nunique() for s in stages}
    records = []
    prev = None
    for stage, count in counts.items():
        conv = round(count / prev * 100, 2) if prev else 100.0
        records.append({"stage": stage, "users": count, "conversion_rate_pct": conv})
        prev = count
    return pd.DataFrame(records)
