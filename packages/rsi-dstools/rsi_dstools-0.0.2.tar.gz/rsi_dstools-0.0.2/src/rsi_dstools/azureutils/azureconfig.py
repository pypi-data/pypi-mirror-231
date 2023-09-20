from os import path
import pandas as pd
from warnings import warn
import azure
from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication, InteractiveLoginAuthentication
import azureml
from ..config.baseconfig import Config


class AzureConfig(Config):
    ''' Class to auto-search the provided file or directory
        for Azure setup information json configuration.

        Azure configuration information can arrive through 
        azure*config*.json files, or through ENV variables
        prefixed with 'RSI_AZURE_'

    '''
    _workspace = None
    key_check_primary = 'subscription_id'
    def __init__(self, *args, search_prefix='RSI_AZURE_', debug=0, **kwargs) -> None:
        self.search_str = ['azure']
        if 'read_all' not in kwargs:
            kwargs['read_all'] = True
        self.search_prefix = search_prefix
        super().__init__(*args,debug=debug,child=self,**kwargs)
        self.obfuscate_on_stringify = ['subscription_id', 'password']
        self.obfuscate_func = lambda x, _type: (str(x)[:(0 if 'pass' in _type else -int(len(str(x))/2))] + 
            ('*' * (4 if 'pass' in _type else int(len(str(x))/2)) if len(str(x)) > 8 else '****'))

        if self.debug > 2:
            print(self.__repr__())

        # attempt to authenticate using Service Principal if a secret  
        # and client ID are found in the config files read in
        sp = None
        if 'password' in self._config:
            if self.debug:
                print('found SP credentials in config file(s) or env variables')
            try:
                from azureml._vendor.azure_cli_core.azclierror import AuthenticationError as AuthError
            except AttributeError:
                AuthError = None
            try:
                sp = ServicePrincipalAuthentication(
                    tenant_id=self._config['tenantid'], # tenantID
                    service_principal_id=self._config['clientid'], # clientId
                    service_principal_password=self._config['password']) # clientSecret
                self._workspace = Workspace.get(
                    name=self._config['workspace_name'],
                    subscription_id=self._config['subscription_id'],
                    resource_group=self._config['resource_group'],
                    auth=sp)
            except azure.core.exceptions.ClientAuthenticationError as e:
                warn((f'problem authenticating Azure workspace from config: {self.file_loc}\n'
                    f'exception was: {str(e)}\n...will attempt interactive auth'))
            except Exception as e:
                if (AuthError and isinstance(e, AuthError)) or ('authentication' in str(e)):
                    raise(Exception(str(e) + '\n...with credentials:\n' + self.__repr__()))
        # otherwise, attempt standard authentication
        if self._workspace is None:
            try:
                self._workspace = (Workspace.from_config(self.file_loc, 
                    auth=InteractiveLoginAuthentication(force=True)) if self.file_loc else None)

            except Exception as e:
                if self.error_no_file_found:
                    raise(e)
                else:
                    warn((f'problem establishing Azure workspace from {self.file_loc}\n'
                        f'exception was: {str(e)}'))
                    self._workspace = None

    @property
    def Workspace(self):
        return self._workspace

    def get_workspace_str(self):
        return self.__repr__(self)

    def validate(self, config):
        missing = [k for k in  ["subscription_id", "resource_group", "workspace_name"]
                if (k not in config)]
        if (self.file_loc is not None):
            assert len(missing) == 0, (
                f'configuration failed validation | missing keys: {", ".join(missing)}')
        
        
    def setup_config(self,*args,**kwargs):
        ''' Automatically search the provided file or directory
            for database connection json configuration.
        '''
        from os import environ
        # if self.debug:
        #     print(f'running overridden version of setup_config() in {self.__class__.__name__}')
        _config = self.override_config_file(self.setup_base_config(), **kwargs)

        # automatically use-lower case from possible upper-case env vars
        override_params = {k.lower(): v 
            for k, v in self.__class__.get_env_overrides(self.search_prefix).items()}
        # self.warn_updates(_config, override_params)
        _config = self.override_config_file(_config, source='env', **override_params)
        return _config

