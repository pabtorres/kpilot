from pyspark.sql import SparkSession
import time

def read_table_with_retry(
    spark: SparkSession,
    dbtable: str,
    connection_string: str,
    max_attempts: int = 3,
    sleep_seconds: int = 5
):
    """
    Lee una tabla desde Azure SQL con reintentos automáticos.

    Args:
        spark: Sesión Spark activa.
        dbtable: Nombre de la tabla a leer.
        connection_string: Cadena JDBC.
        max_attempts: Número máximo de intentos.
        sleep_seconds: Espera entre reintentos.

    Returns:
        Spark DataFrame.
    """
    for attempt in range(1, max_attempts + 1):
        try:
            return (
                spark.read.format("jdbc")
                .option("url", connection_string)
                .option("dbtable", dbtable)
                .load()
            )
        except Exception as e:
            if attempt == max_attempts:
                raise e
            time.sleep(sleep_seconds)


def read_query_as_pandas(
    spark: SparkSession,
    connection_string: str,
    query: str
):
    """
    Ejecuta una query SQL y devuelve un DataFrame de Pandas.
    """
    df = (
        spark.read.format("jdbc")
        .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver")
        .option("url", connection_string)
        .option("query", query)
        .load()
    )
    return df.toPandas()
