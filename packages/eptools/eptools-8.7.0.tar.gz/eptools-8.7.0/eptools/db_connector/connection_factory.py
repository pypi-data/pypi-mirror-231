from .connectors import MySQLConnector, SQLServerConnector

class ConnectionFactory:
    @staticmethod
    def get_connector(database_type, credential_provider):

        connectors = {
            'mysql': MySQLConnector,
            'sql_server': SQLServerConnector
        }

        connector_class = connectors.get(database_type)
        if not connector_class:
            raise ValueError(f"Unsupported database type: {database_type}")
        
        return connector_class.get_connection(credential_provider)