import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_weekly_heatmap(df: pd.DataFrame, output_path: str = None):
    df = df.copy()
    df["week"] = df["order_date"].dt.isocalendar().week.astype(int)
    df["day"] = df["order_date"].dt.day_name()
    pivot = df.pivot_table(index="day", columns="week", values="revenue", aggfunc="sum")
    day_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    pivot = pivot.reindex([d for d in day_order if d in pivot.index])
    fig, ax = plt.subplots(figsize=(16, 5))
    sns.heatmap(pivot, cmap="YlOrRd", ax=ax, linewidths=0.3, cbar_kws={"label":"Revenue"})
    ax.set_title("Revenue Heatmap — Day × Week", fontweight="bold")
    plt.tight_layout()
    if output_path: plt.savefig(output_path, dpi=150)
    return fig
