def generate_query_for_resultados_generales(
    databricks_table: str,
    grupo_rollout_input: str,
    metrics_dict: dict
) -> str:
    """
    Genera una query SQL para obtener KPIs desde una tabla de Databricks.

    Args:
        databricks_table: Nombre completo de la tabla (con schema).
        grupo_rollout_input: Grupo o rollout a filtrar.
        metrics_dict: Diccionario con mapeo de métricas (metric_i -> name_i).

    Returns:
        Query SQL lista para ejecutar.
    """
    query = f"""
    SELECT 
        DATEADD(day, -1, fecha) AS Fecha,
        grupo AS Grupo,
        [{metrics_dict['metric_1']}] AS {metrics_dict['name_1']},
        [{metrics_dict['metric_2']}] AS {metrics_dict['name_2']},
        [{metrics_dict['metric_3']}] AS {metrics_dict['name_3']}
    FROM {databricks_table}
    WHERE grupo IN ('{grupo_rollout_input}')
    """
    return query.strip()
