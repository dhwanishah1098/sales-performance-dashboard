import pandas as pd

def gross_margin(revenue: float, cost: float) -> float:
    return round((revenue - cost) / revenue * 100, 2) if revenue else 0.0

def customer_acquisition_cost(spend: float, new_customers: int) -> float:
    return round(spend / new_customers, 2) if new_customers else 0.0

def return_on_ad_spend(revenue: float, ad_spend: float) -> float:
    return round(revenue / ad_spend, 2) if ad_spend else 0.0

def net_promoter_score(promoters: int, detractors: int, total: int) -> float:
    return round(100 * (promoters - detractors) / total, 1) if total else 0.0
