from config import bot, bot_username
from datetime import date ,datetime, timezone, timedelta
import time
async def comandospersonalizados(msg):
    if msg.get('text'):
       
       #comando1
        if msg['text'] == 'comando1':
            await bot.sendMessage(msg['chat']['id'], 'oque o bot responde','markdown',reply_to_message_id=msg['message_id'])
       #comando2
        if msg['text'] == 'comando2':
            await bot.sendMessage(msg['chat']['id'], 'oque o bot responde','markdown',reply_to_message_id=msg['message_id'])
        



























        