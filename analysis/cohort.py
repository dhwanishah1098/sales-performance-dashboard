import pandas as pd


def cohort_analysis(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["cohort_month"] = df.groupby("customer_id")["order_date"].transform("min").dt.to_period("M")
    df["order_month"] = df["order_date"].dt.to_period("M")
    df["period_number"] = (df["order_month"] - df["cohort_month"]).apply(lambda x: x.n)
    cohort = df.groupby(["cohort_month", "period_number"])["customer_id"].nunique().reset_index()
    cohort_size = cohort[cohort["period_number"] == 0].set_index("cohort_month")["customer_id"]
    cohort["retention_rate"] = cohort.apply(
        lambda r: r["customer_id"] / cohort_size[r["cohort_month"]], axis=1
    )
    return cohort.pivot(index="cohort_month", columns="period_number", values="retention_rate")
