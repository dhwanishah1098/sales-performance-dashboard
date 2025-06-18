import os
import yaml

_DEFAULT = {
    "data_path": "data/sales_data.csv",
    "report_output": "reports/",
    "fiscal_year_start": 4,
    "revenue_target_monthly": 500_000,
    "target_margin": 0.35,
}

def load(path: str = "config.yaml") -> dict:
    if os.path.exists(path):
        with open(path) as f:
            user = yaml.safe_load(f) or {}
        return {**_DEFAULT, **user}
    return _DEFAULT
