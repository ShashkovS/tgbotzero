def help():
    print('''# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Вот пример очень простого бота:
from tgbotzero import *

# Токен нужно получить у https://t.me/BotFather
TOKEN = '123:123:tokenHereFromBotFatherInTelegram'

# Функция on_message принимает на вход строку с сообщением 
# и должна вернуть строку с ответом 
def on_message(msg: str):
    return "Твоё сообщение: " + msg

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
''')
