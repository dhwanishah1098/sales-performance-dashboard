def growth_accounting(prev_rev, new_rev, churned_rev, expanded_rev):
    return {
        'new': new_rev,
        'expansion': expanded_rev,
        'churn': -churned_rev,
        'net_new': new_rev + expanded_rev - churned_rev,
        'growth_rate': (new_rev + expanded_rev - churned_rev) / (prev_rev or 1) * 100,
    }
