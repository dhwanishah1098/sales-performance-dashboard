import plotly.graph_objects as go

def plot_trend_overlay(df, metric_col, target_col=None):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["date"], y=df[metric_col],
                             mode="lines+markers", name=metric_col))
    if target_col and target_col in df.columns:
        fig.add_trace(go.Scatter(x=df["date"], y=df[target_col],
                                 mode="lines", name="Target",
                                 line=dict(dash="dot", color="red")))
    fig.update_layout(title=f"{metric_col} vs Target", template="plotly_white")
    return fig
