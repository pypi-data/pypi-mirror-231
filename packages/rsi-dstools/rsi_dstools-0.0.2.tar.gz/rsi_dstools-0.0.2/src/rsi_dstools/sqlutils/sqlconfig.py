from abc import ABCMeta
import json
from os import path
from warnings import warn

from ..config.baseconfig import Config


class SQLConfig(Config):
    ''' Class to auto-search the provided file or directory
        for database connection json configuration info.
    '''
    def __init__(self, *args, debug=1, **kwargs):
        self.search_str = ['sql']
        super().__init__(*args, debug=debug, child=self, **kwargs)
        self.obfuscate_on_stringify = ['password','pw','pass']

    def get_conn_str(self):
        hasPW = (':'+self._config["password"] if self._config["password"] is not None and 
            len(self._config["password"]) else '')
        hasPort = (':'+str(self._config["port"]) if self._config["port"] is not None else '')
        has_db = ('/'+self._config["database"] if ("database" in self._config
            ) and self._config["database"] is not None else "")
        connection_str = (f'{self._config["dialect_driver"]}://{self._config["user"]}'
            f'{hasPW}@{self._config["host"]}{hasPort}'
            f'{has_db}') # connect to database
        return connection_str

    def validate(self, config):
        missing = [k for k in ["dialect_driver", "host", "port", "user"]
                if (k not in config)]
        assert len(missing) == 0, (
            f'configuration failed validation | missing keys: {", ".join(missing)}')
        if "database" not in config:
            warn("no default database found")
        
    def setup_config(self,pw=None, pwENVname='RPESQLAPI',**kwargs):
        ''' Automatically search the provided file or directory
            for database connection json configuration.
        '''
        from os import environ
        # if self.debug:
        #     print(f'running overridden version of setup_config() in {self.__class__.__name__}')
        _config = self.setup_base_config(**kwargs)

        if pw is not None:
            if 'password' in _config and len(_config['password']):
                warn('replacing existing password from configuration .json file')
            _config['password'] = pw
        elif 'password' not in _config and pwENVname in environ:
            _config['password'] = environ[pwENVname]
        elif 'password' not in _config:
            warn('no password specified')
            _config['password'] = None

        _config = self.override_config_file(_config,**kwargs)
        return _config
