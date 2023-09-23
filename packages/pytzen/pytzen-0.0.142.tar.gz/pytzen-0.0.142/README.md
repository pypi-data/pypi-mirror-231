# `pytzen`
----

## Disclaimer:
This library is offered 'as-is' with **no official support, maintenance, or warranty**. Primarily, `pytzen` is an experimentation, which may not be apt for production settings. Users are encouraged to delve into the library but should note that the developers won't actively address arising issues.

## Code Access:
The associated GitHub repository is private. Direct access to the source code's versioning or issue tracking is restricted. However, the source code is available on this page and in the **Download files** section:
- **Source Distribution**: `pytzen-*.tar.gz`
- **Built Distribution**: `pytzen-*-py3-none-any.whl`

## Usage Caution:
We are not liable for issues stemming from the library's usage in production environments. Users should extensively test and vet the library in a safe space before expansive implementation.

----

## `pytzen.prototype`

The `Prototype` class is a tool tailored for data scientists operating primarily within the Jupyter Notebook environment. It's designed to simplify and expedite the process of class generation and prototyping, especially for dynamic model applications. Here's what it brings to the table:

- **Dynamic Class Creation**: Using a simple JSON configuration file, `Prototype` helps you create Python classes with predefined attributes, inputs, and methods. This allows for dynamic and on-the-fly class instantiation, saving time and effort.
  
- **Auto-Documentation**: Leveraging the information from the JSON configuration, `Prototype` automatically generates documentation for each class. This ensures that every created class comes with clear and consistent docstrings, enhancing understandability.
  
- **Rapid Prototyping**: `Prototype` is designed for an interactive environment like Jupyter Notebook. It allows for quick class definition, testing of models, and iterative tweaking—all without restarting the kernel or re-writing large chunks of code.
  
- **Config-Driven Design**: Whether you're pulling configuration details from external data sources or have a predefined set of attributes and methods, `Prototype` lets you mold classes as per your requirements. This is particularly useful when classes need to be generated based on changing data or configurations.
  
- **System Extensions**: If you have an existing system or application, `Prototype` can serve as a handy tool to enrich it. By facilitating the addition of new class plugins or extensions, it helps in expanding functionalities and adding new features seamlessly.

Note: Always make sure that the JSON configuration files are structured correctly and kept secure, especially if they can influence the behavior of the generated classes. Incorrect configurations can lead to unexpected behaviors or vulnerabilities.

## Usage


```python
import sys
sys.path.append('/home/pytzen/lab/pytzen/src')
import os
os.environ['PROTOTYPE_PATH'] = '/home/pytzen/lab/pytzen/prototype'
import inspect
from pytzen.logs import Logger
```


```python
#%%writefile pattern.py
from pytzen.prototype import Prototype

class ClassPattern(Prototype):

    def _out_of_box(self):
        print('I am a private method to be run inside another method.')

    def some_method(self):
        self.logs.info('Creating some_method.')
        self.some_attribute = 'some_attribute'
        print(f'Implemented some_method and {self.some_attribute}.')
    
    def another_method(self):
        self._out_of_box()
        self.logs.info('Creating another_method.')
        self.another_attribute = 'another_attribute'
        print(f'Implemented another_method and {self.another_attribute}.')
```


```python
from pattern import ClassPattern
cp = ClassPattern(some_input='some_input', another_input='another_input')
cp.some_method()
cp.another_method()
```

    2023-09-22 13:33:49,412 - <class 'pattern.ClassPattern'> - INFO - Creating some_method.
    2023-09-22 13:33:49,412 - <class 'pattern.ClassPattern'> - INFO - Creating another_method.


    Implemented some_method and some_attribute.
    I am a private method to be run inside another method.
    Implemented another_method and another_attribute.



```python
print(cp.__doc__)
```

    Docstring explaining the class. Docstring explaining the class.
    
    Inputs:
    - some_input: Docstring explaining the input. Docstring explaining
        the input.
    - another_input: Docstring explaining another input. Docstring
        explaining another input.
    
    Attributes:
    - some_attribute: Docstring explaining the attribute. Docstring
        explaining the attribute.
    - another_attribute: Docstring explaining another attribute.
        Docstring explaining another attribute.
    
    Methods:
    - some_method: Docstring explaining the method. Docstring explaining
        the method.
    - another_method: Docstring explaining another method. Docstring
        explaining another method.
    


## module `prototype`

```python
import json
import os
from abc import ABC, abstractmethod
import textwrap
from pytzen.logs import Logger
```

### class `prototype.Prototype`


```python
print(inspect.getsource(Prototype))
```

    class Prototype(ABC):
    
        def __init__(self, log_level='INFO', **kwargs):
            self._class_name = self.__class__.__name__
            self._prototype_path = os.environ.get('PROTOTYPE_PATH', '.')
            self._class_pattern = self._get_class_pattern()
            self.__doc__ = self._generate_class_doc()
            self._create_objects(kwargs)
            self.logs = Logger(name=str(self.__class__), level=log_level)
        
        def _get_class_pattern(self):
            json_path = os.path.join(self._prototype_path, 
                                     f'classes/{self._class_name}.json')
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
            for obj in ['inputs', 'attributes', 'methods']:
                doc_str = add_object(obj, doc_str)
            return doc_str
    
        def _create_objects(self, kwargs):
            for input_name in self._class_pattern['inputs']:
                if input_name not in kwargs:
                    raise ValueError(f'{input_name} must be provided!')
                setattr(self, input_name, kwargs[input_name])
            for attr_name in self._class_pattern['attributes']:
                setattr(self, attr_name, None)
            for method_name in self._class_pattern['methods']:
                vars()[method_name] = abstractmethod(lambda self: None)
    


## module `logs`

### class `logs.Logger`

```python
import logging
import traceback
```


```python
print(inspect.getsource(Logger))
```

    class Logger:
    
        def __init__(self, name: str, level: str) -> None:
    
            self.logger: logging.Logger = logging.getLogger(name)
            self.logger.propagate = False
            set_level = logging._nameToLevel[level]
            self.logger.setLevel(set_level)
            if not self.logger.handlers:
                msg = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                formats: str = msg
                formatter = logging.Formatter(formats)
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(formatter)
                self.logger.addHandler(console_handler)
    
        def debug(self, message: str) -> None: 
            self.logger.debug(message)
    
        def info(self, message: str) -> None: 
            self.logger.info(message)
    
        def warning(self, message: str) -> None: 
            self.logger.warning(message)
    
        def error(self, message: str) -> None:
            self.logger.error(message)
            print(traceback.format_exc())
    
        def critical(self, message: str) -> None:
            self.logger.critical(message)
            print(traceback.format_exc())
    

