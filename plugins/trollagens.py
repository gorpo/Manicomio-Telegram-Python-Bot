from config import bot, bot_username
import random

async def trollagens(msg):
    if msg.get('text'):

        #SEU COMANDO PERSONALIZADO 1
        if msg['text'] == '*********':
            await bot.sendMessage(msg['chat']['id'], '`*************`','markdown',reply_to_message_id=msg['message_id'])
        #SEU COMANDO PERSONALIZADO2
        if msg['text'] == '*********':
            await bot.sendMessage(msg['chat']['id'], '`*************`','markdown',reply_to_message_id=msg['message_id'])
        


        #Exemplo de uma imagem randomica do bot.....
        elif msg['text'].split()[0] == 'gato':
            gato1 = str('https://i.kym-cdn.com/entries/icons/original/000/026/489/crying.jpg')
            gato2 = str('https://i.kym-cdn.com/photos/images/newsfeed/001/384/542/f03.jpg')
            gato3 = str('https://i.kym-cdn.com/photos/images/newsfeed/001/384/543/865.jpg')
            gato4 = str('https://pics.ballmemes.com/sad-cat-61204342.png')
            lista = [gato1,gato2,gato3,gato4]
            escolhido = random.choice(lista) 
            await bot.sendPhoto(msg['chat']['id'],escolhido, reply_to_message_id=msg['message_id'])    
         

        #Exemplo de uma mensagem randomica do bot.....
        elif msg['text'].split()[0] == 'maconha':
            gato1 = str('O gorpo fuma muito')
            gato2 = str('maconha é bom pra caralho')
            gato3 = str('maconharia feio')
            gato4 = str('quem nunca fumou um baseadiho?')
            lista = [gato1,gato2,gato3,gato4]
            escolhido = random.choice(lista) 
            await bot.sendMessage(msg['chat']['id'],escolhido, reply_to_message_id=msg['message_id'])    
        #replica segunda palavra somente    
        elif msg['text']  == 'teste qualidade':
            dividido = msg['text'].split()
            primeira =  msg['text'][0]
            segunda = msg['text'][6:]
            await bot.sendMessage(msg['chat']['id'],segunda, reply_to_message_id=msg['message_id'])    

        #replica segunda palavra somente    
        elif msg['text']  == 'calc    ':
            dividido = msg['text'].split()
            primeira =  int(msg['text'][5])
            segunda = int(msg['text'][7])
            soma = primeira + segunda
            await bot.sendMessage(msg['chat']['id'],soma, reply_to_message_id=msg['message_id'])    
            


        
        #exemplo de foto hospedada no pc
        elif msg['text'].split()[0] == 'foto':
            await bot.sendPhoto(msg['chat']['id'], open('fotos/foto.jpg','rb'), reply_to_message_id=msg['message_id'])    
            await bot.sendPhoto(msg['chat']['id'], open('fotos/foto2.jpg','rb'), reply_to_message_id=msg['message_id']) 
            await bot.sendPhoto(msg['chat']['id'], open('fotos/foto3.jpg','rb'), reply_to_message_id=msg['message_id']) 
            

   #exemplos de stickers pegar id /jsondump
        elif msg['text'].split()[0] == 'cp':
            await bot.sendSticker(msg['chat']['id'], sticker='CAADAgADFAIAAiXfMB4Hf647jciFlxYE', reply_to_message_id=msg['message_id']) 
   #exemplos de stickers pegar id /jsondump
        elif msg['text'] == 'http injector':
            await bot.sendDocument(msg['chat']['id'], document='BQADAQADaAADLwfYRuyWgyR0n8a4FgQ', reply_to_message_id=msg['message_id']) 
        
        elif msg['text'] == 'ehi secreta do behemoth':
            await bot.sendDocument(msg['chat']['id'], document='BQADAQADjAADUmHxR6cWprvULnsfFgQ', reply_to_message_id=msg['message_id']) 
            await bot.sendMessage(msg['chat']['id'], '`Nome: TCXS  -  Senha: 1234 - Limite: 100 - Validade: 02/11/2020`','markdown', reply_to_message_id=msg['message_id'])    
            

 #exemplo de foto com ID para pegar vai na foto e usa /jsondump
        elif msg['text'].split()[0] == 'gg':
            await bot.sendPhoto(msg['chat']['id'], photo='AgADAQADSqgxGy7CcUSgw_29_s9XZ2T7awYABAEAAwIAA3kAA0D9AQABFgQ', reply_to_message_id=msg['message_id'])   
       





        #Exemplo de uma mensagem randomica do bot.....
        elif msg['text'] == 'seu cu':
            cu1 = str('`Pau no seu cu filho da puta!`')
            cu2 = str('`Seu cu o caralho para de fala merda mano!`')
            cu3 = str('`É mais arregaçado que o da minha mão quela vaca vadia galinah piranha!`')
            cu4 = str('`O da sua namorada quela puta rampeira!`')
            cu5 = str('`Ah legal, chegou o mano que só fala bosta no grupo!`')
            cu6 = str('`Seu cu, meu cu, teu cu o cu de todo mundo, foda-se!`')
            cu7 = str('`Eu lambo!`')
            cu8 = str('`Empurro a bosta com o pau!`')
            cu9 = str('`Ta arregaçado!`')
            cu10 = str('`Não tem mais nenhuma prega!`')
            cu11 = str('`Estourei ele!`')
            cu12 = str('`O meu ta suave!`')
            cu13 = str('`Eu o @Gorpo Orko @usergutto @mahayana66 fizemos um estrago!`')
            lista = [cu1,cu2,cu3,cu4,cu5,cu6,cu7,cu8,cu9,cu10,cu11,cu12,cu13]
            escolhido = random.choice(lista) 
            await bot.sendMessage(msg['chat']['id'],escolhido, 'markdown',reply_to_message_id=msg['message_id'])   
       




























            return True
