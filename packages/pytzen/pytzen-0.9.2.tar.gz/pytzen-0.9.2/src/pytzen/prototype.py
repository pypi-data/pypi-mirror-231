import json
import os
from abc import ABC
import textwrap
from pytzen.logs import Logger
from pytzen.parser import VariablesParser

class SharedData: ...

class Prototype(ABC):
    config = None
    data = None

    def __init__(self, log_level='INFO', **kwargs):
        self._prototype_path = os.environ.get('PROTOTYPE_PATH', '.')
        self._class_pattern = self._get_class_pattern()
        self.__doc__ = self._generate_class_doc()
        self._get_data()
        self._create_objects(kwargs)
        self._get_logger(log_level)
        self._get_config()
        
    
    def _get_class_pattern(self):
        class_name = self.__class__.__name__
        json_path = os.path.join(self._prototype_path, 
                                 f'classes/{class_name}.json')
        with open(json_path) as file:
            class_pattern = json.load(file)
        return class_pattern

    def _generate_class_doc(self, width=68, indent=' '*4):
        doc_str = self._class_pattern['description'] + '\n'
        def add_object(obj, doc_str):
            doc_str += f'\n{obj.capitalize()}:\n'
            for k, v in self._class_pattern[obj].items():
                line = f'- {k}: {v}'
                doc_str += textwrap.fill(text=line, width=width, 
                                         subsequent_indent=indent) + '\n'
            return doc_str
        for obj in ['inputs', 'attributes', 'methods', 'data']:
            if obj in self._class_pattern:
                doc_str = add_object(obj, doc_str)
        return doc_str

    def _create_objects(self, kwargs):
        if 'inputs' in self._class_pattern:
            for input_name in self._class_pattern['inputs']:
                if input_name not in kwargs:
                    raise ValueError(f'{input_name} must be provided!')
                setattr(self, input_name, kwargs[input_name])
    
    def _get_logger(self, log_level):
        logger_name = str(self.__class__)
        self.logs = Logger(name=logger_name, level=log_level)

    def _get_config(self):
        if not Prototype.config:
            config_path = os.path.join(self._prototype_path, 'config.json')
            if os.path.exists(config_path):
                parser = VariablesParser(json_path=config_path, logs=self.logs)
                Prototype.config = parser.config
    
    def _get_data(self):
        if not Prototype.data:
            Prototype.data = SharedData()
    
    def status(self):
        expected_objects = []
        for inp in self._class_pattern.get('inputs', []):
            expected_objects.append(inp)
        for att_name in self._class_pattern.get('attributes', {}):
            expected_objects.append(att_name)
            if att_name not in self.__dict__:
                self.logs.info(f"The attribute '{att_name}' is not defined.")
        for met_name in self._class_pattern.get('methods', {}):
            expected_objects.append(met_name)
            if not hasattr(self, met_name):
                self.logs.info(f"The method '{met_name}' is not defined.")
        for data_name in self._class_pattern.get('data', {}):
            expected_objects.append(data_name)
            if data_name not in Prototype.data.__dict__:
                self.logs.info(f"The data '{data_name}' is not defined.")
        all_methods = [attr for attr in dir(self) 
                       if callable(getattr(self, attr)) 
                       and attr in self.__class__.__dict__]
        all_instance_attributes = set(self.__dict__.keys())
        exclude = {'_class_pattern', '__doc__', 'logs', '_prototype_path'}
        out_of_box = (all_instance_attributes | set(all_methods)) - \
            set(expected_objects) - exclude
        self.logs.info(f'The object(s) {out_of_box} was(were) not designed.')   