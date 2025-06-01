def assign_price_band(price, bands=[(0,10,'budget'),(10,50,'mid'),(50,200,'premium'),(200,None,'luxury')]):
    for lo,hi,label in bands:
        if hi is None or lo <= price < hi: return label
    return 'unknown'
