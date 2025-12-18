import pandas as pd

def estimate_market_share(own_revenue: float, market_data: pd.DataFrame) -> dict:
    total = market_data["revenue"].sum() + own_revenue
    own_share = round(own_revenue / total * 100, 2)
    competitor_shares = (market_data.assign(
        share_pct=lambda d: (d["revenue"] / total * 100).round(2)
    )[["competitor","share_pct"]].sort_values("share_pct", ascending=False).reset_index(drop=True))
    return {"own_share_pct": own_share, "total_market": round(total, 2), "competitors": competitor_shares}
