import os
import sys
import logging
from typing import Callable
from types import ModuleType

import yaml


ROOT_DIR = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))

log = logging.getLogger(__name__)


def getvars(module: ModuleType):
    var_names = {}
    for name in dir(module):
        var = getattr(module, name)
        if (not isinstance(var, (Callable, ModuleType)) and
                not name.startswith('__')):
            var_names[name] = var
    return var_names


class config:
    """
    Generete config file if not exist
    Set data from file to module

    :name: config module ex: fastconf.config(__name__)
    :file: config file name
    :dir:  directory to config file
    """

    def __init__(self,
                 name: str,
                 file: str='config.yml',
                 root: str=ROOT_DIR):
        self.config = sys.modules[name]
        self.path = os.path.join(root, file)
        self.vars = getvars(self.config)
        self._generate()

    def _generate(self):
        if os.path.exists(self.path):
            self._load()
        else:
            self._dump()

    def _load(self):
        with open(self.path, 'r') as file:
            load_vars = yaml.load(file, Loader=yaml.Loader)
            for k, v in load_vars.items():
                if k not in self.vars:
                    log.warning(f'Wrong field in config file: {k}')
                    continue
                def_var = getattr(self.config, k)
                var_type = type(def_var)
                if def_var is None:
                    setattr(self.config, k, v)
                setattr(self.config, k, var_type(v))

    def _dump(self):
        with open(self.path, 'w') as file:
            file.write(yaml.dump(self.vars))
