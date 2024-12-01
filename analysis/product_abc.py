def classify_abc(df, revenue_col="revenue", id_col="product_id"):
    """ABC classification: A=top 70%, B=70-90%, C=90-100% of revenue."""
    df = df.sort_values(revenue_col, ascending=False).copy()
    df["cum_pct"] = df[revenue_col].cumsum() / df[revenue_col].sum() * 100
    df["abc_class"] = "C"
    df.loc[df["cum_pct"] <= 70, "abc_class"] = "A"
    df.loc[(df["cum_pct"] > 70) & (df["cum_pct"] <= 90), "abc_class"] = "B"
    return df[[id_col, revenue_col, "cum_pct", "abc_class"]]
