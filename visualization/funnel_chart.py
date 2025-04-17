import plotly.graph_objects as go
def funnel_chart(stages: list[str], values: list[float], title='Conversion Funnel'):
    fig = go.Figure(go.Funnel(y=stages, x=values, textinfo='value+percent initial'))
    fig.update_layout(title=title)
    return fig
