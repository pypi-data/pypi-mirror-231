from abc import ABC, abstractmethod
from asyncore import write
from email.mime import multipart
from os import environ, path, PathLike, listdir
from string import printable
import yaml
from glob import glob
from warnings import warn
import json


def load_json(file):
    with open(file,'r') as f:
        data = json.load(f)
    return data

def load_yaml(file):
    with open(file,'r') as f:
        data = yaml.safe_load(f)
    return data

def load_env(file, search_prefix, env_comment_marker='#'):
    data = {}
    warn_invalid_viable_lines = False
    with open(file,'r') as f:
        lines = [ln for ln in f.read().split('\n') 
            if len(ln) > 0 and not(ln.strip().startswith(env_comment_marker))]
        if len(lines) == 0:
            print(f'no config data found in: {file}')
            return {}
        for ln in lines:
            if '=' not in ln:
                if not(ln.startswith(env_comment_marker)) and len(ln.strip()):
                    warn_invalid_viable_lines = True
                continue
            k, v = tuple(list(ln.split('='))[:2])
            k = k.strip()
            if k.lower().startswith('export ') and len(k) > 7:
                k = k[:7].lower() + k[7:]
                k = k.split('export ')[-1]
            if search_prefix is not None and k.startswith(search_prefix):
                k = ''.join(k.split(search_prefix)[1:])
            # strip out comments and whitespace, and then assign to the LHS key
            data[k] = v.split(env_comment_marker)[0].strip() 
    if warn_invalid_viable_lines:
        warn(f'not every viable line has an "=" delimiting key-value pairs in: {file}')
    return data


class Config(ABC):
    """
    Configuration base class.

    Allows scanning of local directory or provided folders
    for the relevant configuration files. Reads in these
    parameters or environment variables and makes them
    accessible in a dictionary-like manner.
    """
    search_str = None
    search_prefix = None
    ext = 'json'
    base_str = '*config'
    comment_marker = '#'
    key_check_primary = None
    file_has_pw_keys = ['password', 'pw']

    def __init__(self, *args, child=None, debug=1, base_str=None,
            error_no_file_found=True, ext=None, read_all=False,
            key_check_primary=None, **kwargs):
        """
        Args:
            (first position arg) (str/pathlike, optional): directory 
                in which files should be found or file from which 
                config params should be aggregated 
            params (dict,optional): base set of parameters 
                with which to populate the config object
            dir (str/pathlike, optional): the directory in 
                which to look for config files (default in 
                the current working directory)
            debug=1 (int): debug level
            base_str='*config' (str): substring to search for when 
                sifting through relevant configuration files
            search_str=None (str or list[str]): secondary string(s)
                with which to filter the config files found in the 
                specified directory
            error_no_file_found=True (bool): raise an error if no
                configuration file is found
            ext='json' (str): the extension to look for when
                searching for config files (default will change
                depending on the child config class type)
            key_check_primary=None (str): the key of the parameter
                key-value pair that must exist in the primary config
                file (i.e., there may be multiple .yml or .env files,
                but this key will indicate which is the correct one
                to use)
        """
        self._config = {}
        self.loc = None
        self.file_loc = None
        self.file_locs = None
        self.file_has_passwords = None
        if base_str is not None:
            self.base_str = base_str
        self.debug = debug
        self.error_no_file_found = error_no_file_found
        self.read_all = read_all
        self.obfuscate_on_stringify = []
        self.obfuscate_func = lambda x, _type: '****'
        if ext is not None:
            self.ext = ext
        if key_check_primary is not None:
            self.key_check_primary = key_check_primary
        self.config_str_selector = None
        if len(args):
            if isinstance(args[0],(str,PathLike)):
                self.loc = path.realpath(args[0])
                if debug > 1:
                    print(f'{child.__class__.__name__}: using provided location: {self.loc}')
            elif isinstance(args[0],list):
                assert all(isinstance(l,(str,PathLike)) for l in args[0]), (
                    'providing urls must be valid PathLike strings')
                self.loc = [path.realpath(l) for l in args[0]]
                if debug > 1:
                    print(f'{child.__class__.__name__}: using provided locations: {self.loc}')
            elif isinstance(args[0],dict):
                kwargs.update(**args[0])
            args = args[1:]
        if 'search_str' in kwargs:
            self.search_str = (kwargs['search_str']
                if isinstance(kwargs['search_str'],list) 
                else [kwargs['search_str']])
        assert self.search_str is None or (isinstance(self.search_str, list) and 
                all(isinstance(el,str) for el in self.search_str)), (
            'search_str should be a list of strings')
        if child is not None:
            child._config = child.setup_config(*args,**kwargs)
            child.validate(child._config)
        else:
            self._config = self.setup_config(*args,**kwargs)

    @abstractmethod
    def validate(self,*args, **kwargs):
        raise NotImplementedError('this method should be implemented by the child class')

    def get_obfuscated(self, k, v):
        return (v if not(any(kk.lower() in k.lower() 
            for kk in self.obfuscate_on_stringify)) else self.obfuscate_func(v,k))

    def __repr__(self):
        return (self.__class__.__name__ + 
            ' | {\n   ' + '\n   '.join([f'{k}:{self.get_obfuscated(k, v)}' 
                for k, v in self._config.items()]) + ' }')

    def __contains__(self,key):
        return key in self._config

    def __getitem__(self,key):
        return self._config[key]

    def get(self,key, key_error=False):
        if key not in self._config:
            if key_error:
                raise KeyError(f'key "{key}" not found')
            return
        return self._config[key]

    def setkeyvalue(self,key,value,env=False,write_to_file=None):
        '''
        NOTE: trying to ensure no one accidentally 
        overrides a parameter of importance by forcing 
        this call instead of overloading the 
        operator (i.e., via __setitem__)
        '''
        self._config[key] = value
        if env:
            environ[('' if self.search_prefix is None else self.search_prefix) + key] = value
        if write_to_file:
            with open(write_to_file,'w') as f:
                if env:
                    envkey = ('' if self.search_prefix is None else self.search_prefix) + key
                    f.write(f'{envkey.upper()}={value}\n')
                else:
                    f.write(json.dumps({key: value}, indent=3))

    @property
    def file_locs_no_pws(self):
        return [f for f, has_pw in zip(self.file_locs,
            self.file_has_passwords) if not(has_pw)]

    def items(self,filter=None):
        for k,v in self._config.items():
            if filter is None:
                yield k,v
            else:
                if k in filter:
                    yield k,v

    def dict_elem(self):
        return {k:v for k, v in self._config.items()}

    def setup_config(self,*args,**kwargs):
        '''
        for inheriting classes reimplementing this function
        they should contain the following 'setup_base_config` 
        call followed by custom overrides and then by key-word
        overrides
        '''
        _config = self.setup_base_config()
        return self.override_config_file(_config,**kwargs)

    def setup_base_config(self,*args,**kwargs):
        ''' Automatically search the provided file or directory
            for database connection json/env/etc configuration.
        '''
        if self.loc is None:
            self.loc = path.abspath(path.curdir)
        multipaths = isinstance(self.loc,list)
        if not(multipaths) and path.isfile(self.loc):
            _files = [path.realpath(self.loc)]
            self.search_str = None
        else:
            if not(multipaths):
                loc = [self.loc]
            else:
                loc = self.loc
            _files = []
            for l in loc:
                if self.ext != 'env':
                    __files = glob(path.join(l,self.base_str+'*.'+self.ext))
                else:
                    __files = [path.join(l,f) for f in listdir(l) if f.endswith(self.ext)]
                _files.extend(__files)    
        if self.debug > 2:
            print(f'{self.ext} files found: {_files}')

        # Only check for string search matches against the file itself (and
        # nothing in the fullpath up to the filename)
        files = [f for f in _files if self.search_str is None or 
            any([st.lower() in path.split(f)[-1].lower() for st in self.search_str])]

        if self.debug > 2:
            print(f'{self.ext} | using {self.search_str}, filtered files found: {files}')

        if self.ext != 'env':
            if len(files) > 1:
                warn((f'for {self.base_str} type: {self.__class__.__name__} '
                    f'found more than one ({self.ext}) '
                    f'{self.base_str} file in this directory, ' + 
                    ('overriding / replacing according to read-in order' 
                        if self.read_all else 'using first file found')))
        if len(files) == 0:
            if self.error_no_file_found:
                raise IOError((f'could not find a .{self.ext} config '
                    f'file in {self.loc}:\n'
                    f'Files in this directory:\n{_files}'))
            elif (self.ext != 'env'):
                warn('could not find config file in this directory, '
                    f'{self.__class__.__name__} object unpopulated')
                return {}
        self.file_locs = files
        self.file_has_passwords = [False for f in files]
        if (self.ext != 'env') and not(self.key_check_primary):
            self.file_loc = (files if self.read_all else files[0])
        _config = {}
        if self.ext in ['yml', 'yaml', 'json']:
            if self.ext == 'json':
                reader = load_json 
            else:
                reader = load_yaml
            found_pkey = False
            for fi, _file in enumerate(files):
                file = path.realpath(_file)
                new = reader(file)
                if self.debug > 4:
                    print(f'read file: {file} with keys:\n{list(new.keys())}')
                if any([any(kk in k for kk in self.file_has_pw_keys) for k in new.keys()]):
                    self.file_has_passwords[self.file_locs.index(_file)] = True
                    if self.debug > 4:
                        print('    >>> updating file password status')
                if not(self.read_all) and (
                        (fi > 1 and not(self.key_check_primary)) or (
                        self.key_check_primary and found_pkey)):
                    continue

                if self.key_check_primary:
                    found_pkey = (self.key_check_primary.lower() in [
                        nk.lower() for nk in new.keys()])
                    if found_pkey:
                        if (self.key_check_primary not in new):
                            warn("found matching config file with primary key, "
                                "but the letter case of the key string was mismatched")
                        self.file_loc = file
                    if found_pkey or self.read_all:
                        _config.update(new)
                else:
                    _config.update(new)
                    if not(self.read_all):
                        break
        else:
            self.file_loc = files
            reader = lambda fn: load_env(fn, self.search_prefix, 
                env_comment_marker=self.comment_marker)
            if self.ext != 'env':
                warn('attempting to parse as .env file, may not produce valid config')
            warn_override = []
            _config = {}
            for _file in files:
                file = path.realpath(_file)
                __config = reader(file)
                for k in __config:
                    if k in _config:
                        warn_override.append(k)
                _config.update(__config)

            if warn_override:
                if len(files) > 1:
                    warn(('found more than one config file in this directory, '
                        f'overridden were: {warn_override}'))
                else:
                    raise KeyError((f'found config variable more one time in this .{self.ext} ' 
                        f'file, overrides: {warn_override}'))
        self._reader_used = reader
        return _config

    @staticmethod
    def get_env_overrides(search_prefix):
        if search_prefix is None:
            return {}
        from os import environ
        env_overrides = {}
        for k,v in environ.items():
            if k.startswith(search_prefix):
                value = v
                try:
                    value = float(v)
                except (TypeError,ValueError):
                    pass
                try:
                    value = int(v)
                except (TypeError,ValueError):
                    pass
                env_overrides[k.split(search_prefix)[-1]] = value
        return env_overrides

    # def warn_updates(self, config, updates):
    #     unique_updates = {k: v for k, v in updates.items() if k in config}
    #     if self.debug and unique_updates:
    #         matching_updates = {
    #             k: v if not(any(kk.lower() in k.lower() 
    #                 for kk in self.obfuscate_on_stringify)) else self.obfuscate_func(v, k)
    #                 for k, v in unique_updates.items()}
    #         print(f'overwriting env variables: {matching_updates}')

    def lowerkeys(self):
        return {k.lower():v for k, v in self._config.items()}
        
    def replace_config(self,new_config):
        self._config = new_config

    def override_config_file(self,_config, source='', **kwargs):
        '''should be called at the end of the custom setup_config'''
        warnlist = []
        for k,v in kwargs.items():
            if k in _config and _config[k] is not None and len(_config[k]):
                warnlist.append(k)
            _config[k] = v
        if warnlist:
            warn(f'{(source + " items " if len(source) else "")}replacing existing config elements obtained from .{self.ext} file | {warnlist}')
        return _config

class YmlConfig(Config):

    def __init__(self,*args, debug=1, **kwargs) -> None:
        self.search_str = ['yaml', 'yml']
        self.base_str = '*'
        self.ext = 'yml'
        super().__init__(*args, debug=debug, child=self, **kwargs)
        self.obfuscate_on_stringify = ['password', 'pw']

    def validate(self,*args, **kwargs):
        return True

class EnvConfig(Config):

    def __init__(self,*args, search_prefix='RSI_', debug=1, 
            skipload_env_var=False, **kwargs) -> None:
        self.search_str = ['env']
        self.ext = 'env'
        self.search_prefix = (search_prefix if not(skipload_env_var) else None)
        super().__init__(*args, debug=debug, child=self, **kwargs)
        self.obfuscate_on_stringify = ['password', 'pw']

    def validate(self,*args, **kwargs):
        return True

    def setkeyvalue(self,key,value,envfile=None):
        super().setkeyvalue(key,value,env=True, write_to_file=envfile)

    def setup_config(self,*args,**kwargs):
        ''' Automatically search the provided file or directory
            for database connection json configuration.
        '''
        _config = self.override_config_file(self.setup_base_config(), **kwargs)
        override_params = self.__class__.get_env_overrides(self.search_prefix)
        # self.warn_updates(_config, override_params)
        _config = self.override_config_file(_config, source='env', **override_params)

        return _config
