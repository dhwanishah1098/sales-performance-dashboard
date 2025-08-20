def promotion_lift(baseline_revenue, promo_revenue):
    if not baseline_revenue: return None
    return round((promo_revenue - baseline_revenue) / baseline_revenue * 100, 2)
