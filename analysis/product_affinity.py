import pandas as pd
from itertools import combinations
from collections import Counter

def basket_pairs(df: pd.DataFrame) -> pd.DataFrame:
    orders = df.groupby("order_id")["product_name"].apply(list)
    pairs = Counter()
    for prods in orders:
        for a, b in combinations(sorted(set(prods)), 2):
            pairs[(a, b)] += 1
    return (pd.DataFrame([(a, b, c) for (a,b),c in pairs.items()],
                         columns=["product_a","product_b","co_occurrences"])
            .sort_values("co_occurrences", ascending=False)
            .reset_index(drop=True))
