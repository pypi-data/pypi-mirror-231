from argparse import ArgumentParser, Namespace

import toml
import json

CONFIGTYPE_TOML = 0
CONFIGTYPE_JSON = 1

class ConfigParserException(Exception):
    def __init__(self,*args,**kwargs):
        super(ConfigParserException,self).__init__(*args, **kwargs)

class ParameterNotFound(Exception):
    def __init__(self,*args,**kwargs):
        super(ParameterNotFound,self).__init__(*args, **kwargs)

class UnknownConfigFileType(Exception):
    def __init__(self,*args,**kwargs):
        super(UnknownConfigFileType,self).__init__(*args, **kwargs)

class ConfigParser(ArgumentParser):

    def __init__(self,*args,**kwargs):
        super(ConfigParser,self).__init__(*args, **kwargs)
        self.__config_files = {}
        self.__config_paths = {}
        self.__loaded_configuration = {}

    def add_argument(self, *args , config_path=None, is_config_file=False, config_type="toml", file_priority=None, default=None, **kwargs):
        if config_path is None: 
            kwargs['default'] = default
        argument = super(ConfigParser,self).add_argument(*args, **kwargs)

        if is_config_file: 
            config_type = ConfigParser.guess_config_type("."+str(config_type) if config_type is not None else argument.default)
            if file_priority is not None:
                self.__config_files[argument.dest] = {"type": config_type, "priority":file_priority}
            else:
                [self.__config_files[k].__setitem__('priority',self.__config_files[k]['priority']+1) for k in self.__config_files]
                self.__config_files[argument.dest] = {"type": config_type, "priority":0}
            if len(set([v['priority'] for v in self.__config_files.values()])) != len(self.__config_files):
                raise ConfigParserException("A config file with this priority already exists")
            
        if config_path is not None:
            self.__config_paths[argument.dest] = ConfigParser.parse_config_path(config_path)
    
    def parse_args(self, args=None, namespace=None):
        self.namespace = namespace
        if namespace is None:
            self.namespace = Namespace()

        namespace = super(ConfigParser,self).parse_args(args=args,namespace=namespace)
        final_configs = {}
        for arg, path in self.__config_paths.items():
            value = getattr(namespace,arg,None)
            if value is not None:
                d = final_configs
                for part in path[:-1]:
                    d[part] = {}; d = d[part]
                d[path[-1]] = value

        self.configuration = {}
        for config_file, config_params in sorted(self.__config_files.items(), key=lambda x: x[1]['priority'], reverse=True):
            config_path = getattr(namespace,config_file)
            if config_path is None:
                continue
            self.__loaded_configuration[config_file] = parsed = ConfigParser.load_file(config_params['type'],config_path)
            ConfigParser.update_configuration(self.configuration, parsed)
            for var, path in self.__config_paths.items():
                try:
                    setattr(namespace,var,ConfigParser.get_config_by_path(parsed, path))
                except ParameterNotFound:
                    pass
        
        ConfigParser.update_configuration(self.configuration, final_configs)
        return super(ConfigParser,self).parse_args(args=args,namespace=namespace)
    
    def loaded_config(self, config_file):
        return self.__loaded_configuration.get(config_file,None)
        
    def parse_config_path(path):
        return path.split('.')
    
    def guess_config_type(filename):
        if filename.endswith('.toml'):
            return CONFIGTYPE_TOML
        if filename.endswith('.json'):
            return CONFIGTYPE_JSON
        raise UnknownConfigFileType(f"Cannot guess config type from file {filename}")
    
    def get_config_by_path(configuration, path, base_path=""):
        if len(path) == 0:
            raise ParameterNotFound("Can't fetch parameter with an empty path")
        
        apath = f"{base_path}.{path[0]}" if base_path is not None and len(base_path) > 0 else path[0]
        try:
            param = configuration[path[0]]
        except KeyError:
            raise ParameterNotFound(f"Can't find parameter {apath}")
        
        if len(path) == 1:
            return param
        if type(param) is dict:                
            return ConfigParser.get_config_by_path(param,path[1:],base_path=apath)

        raise ParameterNotFound(f"Path goes deeper than the possible level")
            
    def load_file(filetype, filepath):
        with open(filepath, encoding="utf8") as stream:
            content = stream.read()
        if filetype == CONFIGTYPE_JSON:
            return json.loads(content)
        if filetype == CONFIGTYPE_TOML:
            return toml.loads(content)
        raise UnknownConfigFileType(f"Unkown config file type {filetype}")
    
    def update_configuration(original_config, new_config):
        new_keys = set(new_config).difference(set(original_config))
        common_keys = set(new_config).intersection(set(original_config))
        for k in common_keys:
            if type(original_config[k]) is dict and type(new_config[k]) is not dict:
                raise Exception("Unmatched config type")
            if type(original_config[k]) is dict:
                ConfigParser.update_configuration(original_config[k],new_config[k])
            else:
                original_config[k] = new_config[k]
        for k in new_keys:
            original_config[k] = new_config[k]