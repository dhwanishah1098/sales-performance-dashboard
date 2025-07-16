import pytest
from analysis.metrics import gross_margin, return_on_ad_spend, net_promoter_score

def test_gross_margin():
    assert gross_margin(100, 60) == 40.0

def test_roas():
    assert return_on_ad_spend(10000, 2000) == 5.0

def test_nps():
    assert net_promoter_score(70, 10, 100) == 60.0

def test_gm_zero_revenue():
    assert gross_margin(0, 50) == 0.0
