def contribution_margin(revenue, variable_costs):
    cm = revenue - variable_costs
    return {'cm_abs': round(cm, 2), 'cm_pct': round(cm / revenue * 100, 2) if revenue else 0}

def breakeven_units(fixed_costs, price_per_unit, variable_cost_per_unit):
    margin = price_per_unit - variable_cost_per_unit
    return round(fixed_costs / margin) if margin else None
