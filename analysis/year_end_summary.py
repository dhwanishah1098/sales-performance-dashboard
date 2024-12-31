def compute_year_end_kpis(df, year: int) -> dict:
    """Aggregate annual KPIs for year-end summary report."""
    yearly = df[df["order_date"].dt.year == year]
    return {
        "year": year,
        "total_revenue": yearly["revenue"].sum(),
        "total_orders": len(yearly),
        "unique_customers": yearly["customer_id"].nunique(),
        "avg_order_value": yearly["revenue"].mean(),
        "best_month": yearly.groupby(yearly["order_date"].dt.month)["revenue"]
                           .sum().idxmax(),
    }
