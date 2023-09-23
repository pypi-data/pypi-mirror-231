import os
import json
import sys

class VariablesParser:

    def __init__(self, json_path, logs):
        self.logs = logs
        self._config_dict = self._get_json(json_path)
        self._arg_dict = self._get_args()
        self._env_dict = self._get_env()
        self._str_converters = {
            'int': int,
            'str': str,
            'float': float,
            'bool': lambda v: v.lower() in ['true', '1', 'yes', 'y']
        }
        self._native_converters = {
            'bool': {1: True, 0: False}
        }
        self.config = self._generate_config()

    def _get_json(self, json_path):
        with open(json_path, 'r') as file:
            return json.load(file)

    def _get_args(self):
        arg_dict = {}
        for arg in sys.argv[1:]:
            if arg.startswith('--'):
                key, value = arg[2:].split('=')
                arg_dict[key] = value
        return arg_dict

    def _get_env(self):
        env_dict = {}
        for key in self._config_dict.keys():
            if os.environ.get(key.upper()):
                env_dict[key] = os.environ.get(key.upper())
        return env_dict

    def _generate_config(self):
        output_config = {}
        for var_name, details in self._config_dict.items():
            var_type = details['type']
            default_value = details['value']
            args = self._arg_dict.get(var_name, default_value)
            value = self._env_dict.get(var_name, args)
            try:
                converted_value = self._convert_value(value, var_type)
                output_config[var_name] = converted_value
            except Exception as e:
                error = (f'Error converting value for {var_name}. ' 
                         f'Details: {str(e)}')
                self.logs.error(error)    
        return output_config

    def _convert_value(self, value, var_type):
        if isinstance(value, str):
            try:
                return self._str_converters[var_type](value)
            except KeyError:
                self.logs.error(f'Unsupported type: {var_type}.')
        else:
            if (var_type in self._native_converters 
                and value in self._native_converters[var_type]):
                return self._native_converters[var_type][value]
            elif type(value).__name__ == var_type:
                return value
            else:
                error = (f'Value type does not match expected type: {var_type}'
                         ' or cannot be converted.')
                self.logs.error(error)
                raise ValueError(error)
