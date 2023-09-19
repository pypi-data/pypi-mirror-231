import logging
from os import environ
from functools import cached_property
import json
import base64
import google.auth
from google.auth.transport.requests import AuthorizedSession
from airflow.secrets.base_secrets import BaseSecretsBackend
from airflow.utils.log.logging_mixin import LoggingMixin

log = logging.getLogger(__name__)

class CachingSecretManagerBackend(BaseSecretsBackend, LoggingMixin):
    NONE = object()

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
        self.cache = dict()

    @cached_property
    def client(self):
        credentials, _project = google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
        return AuthorizedSession(credentials)

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

    def get_value_from_secret(self, prefix, key, version='latest'):
        # Note: Python 3.8 does not yet have functool @cache decorator available
        ident = (prefix, key, version)
        result = self.cache.get(ident, self.NONE)
        if result != self.NONE:
            return result
        result = self.cache[ident] = self._get_value_from_secret(prefix, key, version=version)
        return result

    def _get_value_from_secret(self, prefix, key, version='latest'):
        env_value = self.get_value_from_env(prefix, key)
        if env_value:
            return env_value
        secret_id = f'{prefix}{key}'
        name = f'projects/{self.project_id}/secrets/{secret_id}/versions/{version}'
        try:
            response = self.client.get(f'https://secretmanager.googleapis.com/v1/{name}:access')
            data = response.json()['payload']['data']
            return base64.b64decode(data).decode('utf-8')
        except Exception as e:
            log.exception(f'Exception {e}: Could not load secret {secret_id}')
            return None

    def get_value_from_env(self, prefix, key):
        env_prefix = {self.variables_prefix: 'AIRFLOW_VAR_', self.connections_prefix: 'AIRFLOW_CONN_'}
        return environ.get(f'{env_prefix[prefix]}{key.upper()}')

