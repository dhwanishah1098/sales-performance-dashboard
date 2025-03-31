from itertools import combinations
from collections import Counter
def basket_pairs(orders_df):
    pairs = Counter()
    for _, grp in orders_df.groupby('order_id')['product_id']:
        for a, b in combinations(sorted(grp), 2):
            pairs[(a,b)] += 1
    return pairs.most_common(20)
