def churn_revenue_impact(churned_customers_df, avg_order_value, purchase_freq_per_year):
    annual_lost = churned_customers_df['monetary'].sum()
    count = len(churned_customers_df)
    return {'churned_customers': count, 'annual_revenue_at_risk': round(annual_lost, 2),
            'avg_ltv_lost': round(avg_order_value * purchase_freq_per_year * 3, 2)}
