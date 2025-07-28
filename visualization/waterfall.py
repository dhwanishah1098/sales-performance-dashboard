import plotly.graph_objects as go
def waterfall_chart(categories, values, title='Revenue Waterfall'):
    fig = go.Figure(go.Waterfall(x=categories, y=values, connector={'line':{'color':'rgb(63,63,63)'}}))
    fig.update_layout(title=title, showlegend=False)
    return fig
