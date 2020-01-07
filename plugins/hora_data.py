from config import bot, bot_username
from datetime import date ,datetime, timezone, timedelta
import time
async def hora_data(msg):
    if msg.get('text'):
        #hora e data  --- obrigado ao guanabara pelo curso gratis kkjj
        if msg['text'] == 'que dia e hoje' or msg['text'] == 'Que dia é hoje' or msg['text'] == 'que dia é hoje':
        	#d = date.today()
            t = time.localtime()
            await bot.sendMessage(msg['chat']['id'],'Hoje é  {}/{}/{} e faltam poucos dias para começar a guerra!'.format(t[2],t[1],t[0]),reply_to_message_id=msg['message_id'])
        if msg['text'] == 'que hora é agora' or msg['text'] == 'que horas são agora' or msg['text'] == 'que hora e agora' or msg['text'] == 'que horas sao agora' or msg['text'] == 'Que hora é agora' or msg['text'] == 'Que hora é agora?' or  msg['text'] == 'Que horas são agora' or msg['text'] == 'Que horas são agora?' or msg['text'] == 'Que horas são?' or msg['text'] == 'Que horas são ' or msg['text'] == 'que horas são ' or msg['text'] == 'que horas sao':
            t = time.localtime()
            await bot.sendMessage(msg['chat']['id'],'Agora são {}:{}:{}'.format(t[3],t[4],t[5]),reply_to_message_id=msg['message_id'])
       



        






























            return True
