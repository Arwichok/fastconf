# FastConf

Simple lib for configuration

[![pypi](https://img.shields.io/pypi/v/fastconf.svg)](https://pypi.org/project/fastconf/)

#### Install   
```
$ pip install fastconf
```


#### Example project structure

```
main.py
core/
    __init__.py
    config.py
```

**main.py**    
```python
from core import config
print('TOKEN:', config.TOKEN)
```
**core/config.py**
```python
import fastconf
TOKEN = '...'
fastconf.config(__name__)
```

#### Run project:
```
$ python main.py
TOKEN: ...
```

The **config.yml** file is created in the project root directory.

Change him:
```
TOKEN: 'MY_TOKEN'
```

#### Run again
```
$ python main.py
TOKEN: MY_TOKEN
```


`fastconf.config(name, file='config.yml', root=ROOT_DIR)`

`name` - current name of config module   
`file` - name config file    
`dir` - path to config dir    