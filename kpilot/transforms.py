import pandas as pd

def normalize_percentages(df: pd.DataFrame, metrics_dict: dict) -> pd.DataFrame:
    """
    Divide por 100 las columnas que representan KPIs porcentuales.
    """
    for i in range(1, 4):
        name_kpi = metrics_dict.get(f'name_{i}')
        if name_kpi in df.columns and 'KPI_' in name_kpi:
            df[name_kpi] = df[name_kpi] / 100
    return df
