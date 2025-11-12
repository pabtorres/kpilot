def generate_connection_string(servername: str, databasename: str, timeout: int = 30) -> str:
    """
    Genera una cadena de conexión JDBC para Azure SQL Database con autenticación MSI.
    """
    return (
        f"jdbc:sqlserver://{servername}.database.windows.net:1433;"
        f"database={databasename};"
        "encrypt=true;"
        "trustServerCertificate=false;"
        "hostNameInCertificate=*.database.windows.net;"
        f"loginTimeout={timeout};"
        "authentication=ActiveDirectoryMSI;"
    )
