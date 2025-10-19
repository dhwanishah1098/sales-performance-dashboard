from datetime import date
def annualised_run_rate(ytd_revenue, as_of: date = None):
    d = as_of or date.today()
    day_of_year = d.timetuple().tm_yday
    return round(ytd_revenue / day_of_year * 365, 2)
