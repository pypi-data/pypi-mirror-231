from .connection_factory import ConnectionFactory


class DatabaseManager:
    def __init__(self, database_type, credential_provider):
        self.database_type = database_type
        self.credential_provider = credential_provider

    def select_query(self, query, params=None):
        connection = ConnectionFactory.get_connector(self.database_type, self.credential_provider)
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()

    def insert_update_delete_query(self, query, params=None):
        connection = ConnectionFactory.get_connector(self.database_type, self.credential_provider)
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                connection.commit()
        finally:
            connection.close()

    def execute_stored_procedure(self, procedure_name, *args):
        connection = ConnectionFactory.get_connector(self.database_type, self.credential_provider)
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"EXEC {procedure_name} {', '.join(args)}")
                connection.commit()
                if cursor.description:  # Check if the procedure returned a result set
                    return cursor.fetchall()
        finally:
            connection.close()