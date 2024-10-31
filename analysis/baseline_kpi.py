def compute_baseline_kpis(df):
    """Compute baseline KPIs for period comparison."""
    return {
        "total_revenue": df["revenue"].sum(),
        "avg_order_value": df["revenue"].mean(),
        "order_count": len(df),
        "unique_customers": df["customer_id"].nunique(),
    }
