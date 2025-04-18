import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd


def plot_monthly_revenue(monthly_df: pd.DataFrame, output_path: str = None):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(monthly_df["month"].astype(str), monthly_df["revenue"], color="#4C72B0")
    ax.set_title("Monthly Revenue", fontsize=14, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    plt.xticks(rotation=45)
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
    return fig


def plot_region_breakdown(region_df: pd.DataFrame, output_path: str = None):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].pie(region_df["revenue"], labels=region_df["region"], autopct="%1.1f%%", startangle=90)
    axes[0].set_title("Revenue by Region")
    axes[1].barh(region_df["region"], region_df["avg_margin"], color="#55A868")
    axes[1].set_xlabel("Avg Margin")
    axes[1].set_title("Margin by Region")
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
    return fig


def plot_top_products(product_df: pd.DataFrame, output_path: str = None):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(product_df["product_name"], product_df["revenue"], color="#C44E52")
    ax.set_xlabel("Revenue ($)")
    ax.set_title("Top Products by Revenue", fontsize=13, fontweight="bold")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
    return fig
