<p align="center">
<a href="https://pypi.org/project/tgbotzero/" target="_blank">
<img alt="PyPI" src="https://img.shields.io/pypi/v/tgbotzero">
</a>
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/tgbotzero">
<img alt="GitHub" src="https://img.shields.io/github/license/ShashkovS/tgbotzero">
</p>

# TgBotZero
Телеграм-боты в пару строчек кода.
Простые телеграм-боты должно быть очень просто делать!


## Примеры

Бот, показывающий твоё сообщение:

``` python
import tgbotzero

TOKEN = '123123123:tokenFromBotFatherInTelegram'


def on_message(msg: str):
    return "Твоё сообщение: " + msg
```

<img alt="echobot" src="docs/echobot.png" width="417">


# Установаа

Введите в терминале:
```shell
pip install tgbotzero --upgrade --user
```


Или запустите эту программу:

```python
import os, sys
python = sys.executable
user = '--user' if 'venv' not in python and 'envs' not in python else ''
cmd = f'"{python}" -m pip install tgbotzero --upgrade {user}'
os.system(cmd)
```

# [Contributing](CONTRIBUTING.md) 
