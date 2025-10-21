import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

def waterfall(categories: list, values: list, title: str = "Waterfall Chart", output_path: str = None):
    running = 0
    bottoms, heights, colors = [], [], []
    for v in values:
        bottoms.append(min(running, running + v))
        heights.append(abs(v))
        colors.append("#55A868" if v >= 0 else "#C44E52")
        running += v
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(categories, heights, bottom=bottoms, color=colors, edgecolor="white", linewidth=0.5)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title(title, fontweight="bold")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    if output_path: plt.savefig(output_path, dpi=150)
    return fig
