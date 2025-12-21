def annual_review(df_list: list, year: int) -> dict:
    import pandas as pd
    combined = pd.concat(df_list)
    yearly = combined[combined['order_date'].dt.year == year]
    prev = combined[combined['order_date'].dt.year == year - 1]
    return {
        'revenue': yearly['revenue'].sum(),
        'yoy_growth': (yearly['revenue'].sum() - prev['revenue'].sum()) / (prev['revenue'].sum() or 1) * 100,
        'orders': len(yearly),
        'customers': yearly['customer_id'].nunique(),
    }
