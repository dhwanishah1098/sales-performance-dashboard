import plotly.express as px
def plot_dow_hour_heatmap(df, value_col='revenue'):
    pivot = df.pivot_table(index='day_of_week', columns='hour', values=value_col, aggfunc='mean')
    return px.imshow(pivot, title=f'{value_col} by Day & Hour', aspect='auto')
