from data.loader import load_sales_data, get_region_summary, filter_by_period
from analysis.kpi import calculate_kpis, month_over_month, top_products
from visualization.charts import plot_monthly_revenue, plot_region_breakdown, plot_top_products
import pandas as pd
import os


def run_dashboard(start_date: str = "2024-01-01", end_date: str = "2024-12-31"):
    print("Loading data...")
    df = load_sales_data()
    df_filtered = filter_by_period(df, start_date, end_date)

    print("\n=== KPI Summary ===")
    kpis = calculate_kpis(df_filtered)
    for k, v in kpis.items():
        print(f"  {k}: {v}")

    os.makedirs("reports", exist_ok=True)
    monthly = month_over_month(df_filtered)
    plot_monthly_revenue(monthly, "reports/monthly_revenue.png")

    region_summary = get_region_summary(df_filtered)
    plot_region_breakdown(region_summary, "reports/region_breakdown.png")

    products = top_products(df_filtered)
    plot_top_products(products, "reports/top_products.png")

    print("\nCharts saved to /reports/")
    return kpis


if __name__ == "__main__":
    run_dashboard()
