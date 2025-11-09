import pandas as pd
from datetime import date

def days_remaining_in_quarter() -> int:
    today = date.today()
    q_end_month = ((today.month - 1) // 3 + 1) * 3
    q_end = date(today.year if q_end_month <= 12 else today.year + 1,
                 q_end_month % 12 or 12, 30)
    return (q_end - today).days

def quarterly_run_rate(df: pd.DataFrame, days_elapsed: int, total_days: int = 90) -> float:
    actual = df["revenue"].sum()
    return round(actual / days_elapsed * total_days, 2) if days_elapsed else 0.0

def goal_gap(run_rate: float, target: float) -> dict:
    gap = target - run_rate
    return {
        "run_rate": run_rate,
        "target": target,
        "gap": round(gap, 2),
        "pct_to_goal": round(run_rate / target * 100, 1) if target else 0.0,
        "on_track": gap <= 0,
    }
