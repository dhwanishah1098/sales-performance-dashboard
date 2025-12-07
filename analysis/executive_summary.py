def build_exec_summary(kpis: dict, targets: dict) -> str:
    lines = ['Executive Summary', '='*30]
    for metric, value in kpis.items():
        target = targets.get(metric)
        if target:
            att = value / target * 100
            lines.append(f'{metric}: {value:,.0f}  |  Target: {target:,.0f}  |  Attainment: {att:.1f}%')
        else:
            lines.append(f'{metric}: {value:,.0f}')
    return '\n'.join(lines)
