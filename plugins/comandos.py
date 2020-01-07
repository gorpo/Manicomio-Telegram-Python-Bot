from config import bot, bot_username

async def comandos(msg):
    if msg.get('text'):
       #if msg['text'] == '/dados' or msg['text'] == '!dados' or msg['text'] == '/dados@' + bot_username:
        #explicacões para os users do comando do bot 
        if msg['text'].split()[0] == '/comandos@gorpo_bot':
            await bot.sendMessage(msg['chat']['id'], """Nem todos os comandos do bot podem funcionar para os usuarios, administradores tem privilegios em cima de alguns comandos: 

/comandos@gorpo_bot
/start - inicia o bot
/welcome - Define a mensagem de welcome.
/ban- bane usuario
/unban - desbane usuario
/kick -kicka usuario
/mute - muta usuario
/unmute - desmuta usuario
/unwarn - Remove as advert?ncias do usuario.
/warn - Adverte um usuario.
/pin - fixa posts
/unpin - desfixa os posts
/title - muda o titulo do grupo
/defregras - define regras
/regras - ve as regras
/config - informacoes ser?o enviadas no privado
/admdebug -  debug do admin
/tr - Traduz um texto.
/yt - Pesquisa videos no YouTube.
/ytdl - Baixa o audio de um video no YouTube.
/r - pesquisa um termo no redit
/clima - Exibe informacoes de clima
/coub - Pesquisa de pequenas anima??es
/dados - jogo de dados
/gif - gif do giphy
/git - usuario do github
/id - id do usuario
/ip - informa dados de um ip
/jsondump - retorna dados formatados
/stickerid - pega id de um sticker
/getsticker - baixa um sticker
/criar_sticker - cria um pacote de stickers
/kibar  - copia um sticker para o pacote de stickers
/pypi - pesquisa libs python
/rextester - interpretador de varias linguagens de programa??o
/mark - Repete o texto informado usando Markdown
/html - Repete o texto informado usando HTML
/request - Faz uma requisicao a um site
fala - Repete o texto que voce pedir para ele falar
site - exibe o site da equipe
facebook - exibe o facebook da equipe, cadastre-se
netflix - exibe nosso site de netflix gratis
iptv - exibe nosso site de iptv gratis
anime - exibe nosso site de anime gratis
pkg - exibe nosso site de pkg's para ps3 gratis
biblioteca - exibe nossa biblioteca hacker
curso - exibe nosso site de  cursos
doadores - exibe instruces completas para doadores
painel - exibe nosso painel hacker
E temos muitos mais comandos de zoeira e informativos ocultos!

[*]COMANDOS DOS ADMINISTRADORES[+]
/ban - Bane um usuario.
/config - Envia um menu de configuraces.
/defregras - Define as regras do grupo.
/kick - Kicka um inscrito.
/mute - Restringe um usuario.
/pin - Fixa uma mensagem no grupo.
/title - Define o titulo do grupo.
/unban - Desbane um usuario.
/unmute - Desrestringe um usucrio.
/unpin - Desfixa a mensagem fixada no grupo.
/unwarn - Remove as advert?ncias do usuario.
/warn - Adverte um usuario.
/welcome - Define a mensagem de welcome.

[*]FERRAMENTAS PARA USUARIOS[*]
/clima - Exibe informaces de clima.
/coub - Pesquisa de pequenas anima??es.
/echo - Repete o texto informado.
/gif - Pesquisa de GIFs.
/git - Envia informaces de um user do GitHub.
/html - Repete o texto informado usando HTML.
/ip - Exibe informaces sobre um IP/dominio.
/jsondump - Envia o json da mensagem.
/mark - Repete o texto informado usando Markdown.
/print - Envia uma print de um site.
/pypi - Pesquisa de m?dulos no PyPI.
/r - Pesquisa de topicos no Reddit
/request - Faz uma requisicao a um site.
/shorten - Encurta uma URL.
/token - Exibe informaces de um token de bot.
/tr - Traduz um texto.
/yt - Pesquisa v?deos no YouTube.
/ytdl - Baixa o ?udio de um v?deo no YouTube.

[*]COMANDOS PARA USUARIOS[*]
/admins - Mostra a lista de admins do chat.
/dados - Envia um numero aleatorio de 1 a 6.
/bug - Reporta um bug ao meu desenvolvedor.
/id - Exibe suas informaces ou de um usuario.
/ping - Responde com uma mensagem de ping.
/regras - Exibe as regras do grupo.
/roleta - Para jogar a Roleta Russa.


""",
                                                  reply_to_message_id=msg['message_id'])    


        
#[*] COMANDOS ACEITOS APENAS PELO GORPO [*]
#*!backup* - Faz backup do bot.
#*!cmd* - Executa um comando.
#*!chat* - Obtem infos de um chat.
#*!del* - Deleta a mensagem respondida.
#*!doc* - Envia um documento do server.
#*!eval* - Executa uma função Python.
#*!exec* - Executa um código Python.
#*!leave* - O bot sai do chat.
#*!plist* - Lista os plugins ativos.
#*!promote* - Promove alguém a admin.
#*!restart* - Reinicia o bot.
#*!upgrade* - Atualiza a base do bot.
#*!upload* - Envia um arquivo para o servidor.





























            return True
