def customer_health_score(recency, frequency, monetary, weights=(0.3,0.3,0.4)):
    r_score = max(0, 100 - recency / 3)
    f_score = min(100, frequency * 10)
    m_score = min(100, monetary / 20)
    return round(weights[0]*r_score + weights[1]*f_score + weights[2]*m_score, 1)
