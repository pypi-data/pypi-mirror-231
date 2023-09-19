import json
from abc import ABC, abstractmethod
import textwrap
from pytzen.logs import Logger

class ZenGenerator(ABC):

    def __init__(self, json_path, log_level='INFO', **kwargs):
        self.class_pattern = self._get_class_pattern(json_path)
        self.__doc__ = self._generate_class_doc()
        self._create_objects(kwargs)
        self.log = Logger(name=str(self.__class__), level=log_level)
    
    def _get_class_pattern(cls, json_path):
        with open(json_path) as file:
            class_pattern = json.load(file)
        return class_pattern

    def _generate_class_doc(self, width=68, indent=' '*4):
        doc_str = self.class_pattern['description'] + '\n'
        def add_object(obj, doc_str):
            doc_str += f'\n{obj.capitalize()}:\n'
            for k, v in self.class_pattern[obj].items():
                line = f'- {k}: {v}'
                doc_str += textwrap.fill(text=line, width=width, 
                                         subsequent_indent=indent) + '\n'
            return doc_str
        for obj in ['inputs', 'attributes', 'methods']:
            doc_str = add_object(obj, doc_str)
        return doc_str

    def _create_objects(self, kwargs):
        for input_name in self.class_pattern['inputs']:
            if input_name not in kwargs:
                raise ValueError(f'{input_name} must be provided!')
            setattr(self, input_name, kwargs[input_name])
        for attr_name in self.class_pattern['attributes']:
            setattr(self, attr_name, None)
        for method_name in self.class_pattern['methods']:
            vars()[method_name] = abstractmethod(lambda self: None)