import os
from .credential_provider import CredentialProvider

class EnvironmentVariableProvider(CredentialProvider):
    def get_credentials(self, db_type: str):
        return {
            'host': os.getenv(f'{db_type.upper()}_DB_HOST'),
            'user': os.getenv(f'{db_type.upper()}_DB_USER'),
            'password': os.getenv(f'{db_type.upper()}_DB_PASSWORD'),
            'dbname': os.getenv(f'{db_type.upper()}_DB_NAME'),
        }