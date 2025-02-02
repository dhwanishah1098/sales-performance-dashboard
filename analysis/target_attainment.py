def target_attainment(actual, target):
    if not target: return None
    return round(actual / target * 100, 1)
