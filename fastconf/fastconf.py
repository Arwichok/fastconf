import os
import sys
import json
import pathlib

from typing import Callable
from types import ModuleType

import yaml

__main__ = sys.modules['__main__'].__file__

_avialable_ext = ['json', 'yaml', 'yml']

_dumpnone = lambda d: ''
_loadnone = lambda s: {}

_dumpjson = lambda d: json.dumps(d, indent=4)
_loadjson = lambda s: json.loads(s)

_dumpyaml = lambda d: yaml.dump(d)
_loadyaml = lambda s: yaml.load(s, Loader=yaml.Loader)

_dumps = {
    "json": _dumpjson,
    "yaml": _dumpyaml,
    "yml": _dumpyaml,
}
_loads = {
    "json": _loadjson,
    "yaml": _loadyaml,
    "yml": _loadyaml,
}

def getvars(module: ModuleType):
    var_names = {}
    for name in dir(module):
        var = getattr(module, name)
        if (not isinstance(var, (Callable, ModuleType)) and
                not name.startswith('__')):
            var_names[name] = var
    return var_names

class config:
    def __init__(self, name:str, 
                 ext='json', file='config', main=__main__):
        self.config = sys.modules[name]
        self.ext = ext
        self.root = os.path.dirname(os.path.abspath(main))
        self.path = os.path.join(self.root, file+'.'+ext)
        self.vars = getvars(self.config)
        self._load_config()
        self.vars['ROOT_DIR'] = self.root

    def _load_config(self):
        if os.path.exists(self.path):
            self._load()
        elif self.ext in _avialable_ext:
            self._dump()
        else:
            raise Exception(f"Wrong extension type: {self.ext}\n"
                f"Avialable: {', '.join(_avialable_ext)}")

    def _load(self):
        with open(self.path, 'r') as file:
            load = _loads.get(self.ext) or _loadnone
            loadvars = load(file.read())
            for k, v in loadvars.items():
                defvar = getattr(self.config, k)
                setattr(self.config, k, type(defvar)(v))

    def _dump(self):
        with open(self.path, 'w') as file:
            dump = _dumps.get(self.ext) or _dumpnone
            file.write(dump(self.vars))
