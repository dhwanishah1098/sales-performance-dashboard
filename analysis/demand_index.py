def demand_index(units_sold, avg_units):
    if not avg_units: return 0
    return round(units_sold / avg_units, 3)

def flag_high_demand(df, threshold=1.3):
    df['demand_index'] = df.apply(lambda r: demand_index(r['units'], r['avg_units']), axis=1)
    return df[df['demand_index'] >= threshold]
