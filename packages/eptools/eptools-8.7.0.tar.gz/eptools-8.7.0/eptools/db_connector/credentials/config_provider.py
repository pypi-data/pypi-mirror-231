import json
from .credential_provider import CredentialProvider

class ConfigurationFileProvider(CredentialProvider):
    def __init__(self, filepath: str) -> None:
        super().__init__()
        self.filepath = filepath
        self.credentials = self._load_credentials()

    def _load_credentials(self):
        with open(self.filepath, 'r') as file:
            return json.load(file)

    def get_credentials(self, db_type: str):
        return self.credentials.get(db_type, {})