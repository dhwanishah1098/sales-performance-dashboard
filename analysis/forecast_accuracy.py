def mape(actual, predicted):
    pairs = [(a,p) for a,p in zip(actual,predicted) if a]
    if not pairs: return None
    return round(sum(abs(a-p)/a for a,p in pairs) / len(pairs) * 100, 2)

def rmse(actual, predicted):
    n = len(actual)
    return round((sum((a-p)**2 for a,p in zip(actual,predicted)) / n)**0.5, 4)
