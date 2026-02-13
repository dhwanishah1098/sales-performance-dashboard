# Sales Performance Dashboard

An interactive Python dashboard for tracking and visualizing sales KPIs across regions, products, and time periods.

## Features
- Real-time KPI tracking (Revenue, Margin, Units Sold, AOV)
- Regional & product-level drill-down
- Month-over-month and year-over-year comparisons
- Revenue forecasting with trend and seasonality analysis
- Automated Excel report generation with formatted sheets

## Project Structure
```
sales-performance-dashboard/
├── data/loader.py          # Data ingestion and cleaning
├── analysis/
│   ├── kpi.py              # KPI calculations
│   └── forecasting.py      # Revenue forecasting
├── visualization/charts.py # Matplotlib chart generators
├── export/report_builder.py# Excel report builder
├── dashboard.py            # Main entry point
└── config.py               # Configuration
```

## Setup
```bash
pip install -r requirements.txt
python dashboard.py --start 2024-01-01 --end 2024-12-31
```
