# FastConf

Simple lib for configuration

[![pypi](https://img.shields.io/pypi/v/fastconf.svg)](https://pypi.org/project/fastconf/)

#### Install   
```
$ pip install fastconf
```


#### Example project structure

```
__main__.py
core/
    __init__.py
    config.py
```

**__main__.py**
```python
from core import config
print('token:', config.token)
```
**core/config.py**
```python
import fastconf
token = '...'
fastconf.config(__name__, 'yml')
```

#### Run project:
```
$ python .
token: ...
```

The **config.yml** file is created in the project root directory.

Change him:
```
token: 'MY_TOKEN'
```

#### Run again
```
$ python .
token: MY_TOKEN
```


`fastconf.config(name, ext='json', file='config', main=main)`

`name` - current name of config module   
`ext`  - type of config file (json, yaml, yml)    
`file` - name config file    
`main` - path to config file    


`core.config.ROOT_DIR` return the project root directory.