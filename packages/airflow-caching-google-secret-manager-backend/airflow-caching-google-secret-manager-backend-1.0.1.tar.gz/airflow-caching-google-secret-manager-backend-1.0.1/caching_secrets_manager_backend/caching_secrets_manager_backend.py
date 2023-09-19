import logging
from os import environ
from functools import cached_property, cache
from google.cloud import secretmanager_v1
from airflow.secrets.base_secrets import BaseSecretsBackend
from airflow.utils.log.logging_mixin import LoggingMixin

log = logging.getLogger(__name__)

class CachingSecretManagerBackend(BaseSecretsBackend, LoggingMixin):
    """
    This class is implemented after google-cloud-secret-manager <~2.11.0
    See also: https://cloud.google.com/python/docs/reference/secretmanager/latest
    """
    def __init__(
        self,
        *,
        connections_prefix = "af-conn-",
        variables_prefix = "af-var-",
        config_prefix = None,
        project_id,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.connections_prefix = connections_prefix
        self.variables_prefix = variables_prefix
        self.config_prefix = config_prefix
        self.project_id = project_id

    @cached_property
    def client(self):
        return secretmanager_v1.SecretManagerServiceClient()

    def get_conn_uri(self, conn_id):
        """
        Get secret connection value from the SecretManager.
        """
        if self.connections_prefix is None:
            return None
        return self.get_value_from_secret(self.connections_prefix, conn_id)

    def get_conn_value(self, conn_id):
        return self.get_conn_uri(conn_id)

    def get_variable(self, key):
        """
        Get Airflow Variable from the SecretManager
        """
        if self.variables_prefix is None:
            return None
        return self.get_value_from_secret(self.variables_prefix, key)

    def get_config(self, key):
        """
        Get Airflow Configuration
        """
        if self.config_prefix is None:
            return None
        return self.get_value_from_secret(self.config_prefix, key)

    @cache
    def get_value_from_secret(self, prefix, key, version='latest'):
        env_value = self.get_value_from_env(prefix, key)
        if env_value:
            return env_value
        secret_id = f'{prefix}{key}'
        name = f'projects/{self.project_id}/secrets/{secret_id}/versions/{version}'
        try:
            response = self.client.access_secret_version(name)
            return response.payload.data.decode('utf-8')
        except Exception as e:
            log.exception(f'Exception {e}: Could not load secret {secret_id}')
            return None

    def get_value_from_env(self, prefix, key):
        env_prefix = {self.variables_prefix: 'AIRFLOW_VAR_', self.connections_prefix: 'AIRFLOW_CONN_'}
        return environ.get(f'{env_prefix[prefix]}{key.upper()}')

