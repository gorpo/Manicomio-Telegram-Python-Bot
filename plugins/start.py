# Copyright (C) 2018-2019 Amano Team <contact@amanoteam.ml>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from amanobot.namedtuple import InlineKeyboardMarkup

import keyboard
from config import bot, version, bot_username, git_repo
from db_handler import cursor
from get_strings import strings, Strings

async def start(msg):
    if msg.get('text'):
        strs = Strings(msg['chat']['id'])

        if msg['text'] == '/start' or msg['text'] == '!start' or msg['text'].split()[
            0] == '@gorpo_bot' + bot_username or msg['text'] == 'start':

            if msg['chat']['type'] == 'private':
                kb = InlineKeyboardMarkup(inline_keyboard=[
                    [dict(text=strs.get('commands_button'), callback_data='all_cmds')] +
                    [dict(text=strs.get('infos_button'), callback_data='infos')],
                    [dict(text=strs.get('lang_button'), callback_data='change_lang')] +
                    [dict(text=strs.get('add_button'), url='https://t.me/{}?startgroup=new'.format(bot_username))]
                ])
                smsg = strs.get('pm_start_msg')
            else:
                kb = InlineKeyboardMarkup(inline_keyboard=[
                    [dict(text=strs.get('start_pm_button'), url='https://t.me/{}?start=start'.format(bot_username))]
                ])
                smsg = strs.get('start_msg')

            await bot.sendMessage(msg['chat']['id'], smsg,
                                  reply_to_message_id=msg['message_id'], reply_markup=kb)
            return True


    elif msg.get('data') and msg.get('message'):
        strs = Strings(msg['message']['chat']['id'])

        cmds_back = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text=strs.get('back_button'), callback_data='all_cmds')]
        ])

        start_back = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text=strs.get('back_button'), callback_data='start_back')]
        ])

        if msg['data'] == 'tools_cmds':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      text='''*Ferramentas:*

/clima - Exibe informações de clima.
/coub - Pesquisa de pequenas animações.
/echo - Repete o texto informado.
/gif - Pesquisa de GIFs.
/git - Envia informações de um user do GitHub.
/html - Repete o texto informado usando HTML.
/ip - Exibe informações sobre um IP/domínio.
/jsondump - Envia o json da mensagem.
/mark - Repete o texto informado usando Markdown.
/print - Envia uma print de um site.
/pypi - Pesquisa de módulos no PyPI.
/r - Pesquisa de tópicos no Reddit
/request - Faz uma requisição a um site.
/shorten - Encurta uma URL.
/token - Exibe informações de um token de bot.
/tr - Traduz um texto.
/yt - Pesquisa vídeos no YouTube.
/ytdl - Baixa o áudio de um vídeo no YouTube.''',
                                      parse_mode='Markdown',
                                      reply_markup=cmds_back)
            return True


        elif msg['data'] == 'admin_cmds':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      '''*Comandos administrativos:*
[+]TODOS COMANDOS LISTADOS ATE ULTIMA ATUALIZACAO[+]
/comandos@gorpo_bot
/start - inicia o bot
/ban- bane usuario
/unban - desbane usuario
/kick -kicka usuario
/mute - muta usuario
/unmute - desmuta usuario
/pin - fixa posts
/unpin - desfixa os posts
/title - muda o titulo do grupo
/defregras - define regras
/regras - ve as regras
/config - informa??es ser?o enviadas no privado
/admdebug -  debug do admin
/tr - Traduz um texto.
/yt - Pesquisa v?deos no YouTube.
/ytdl - Baixa o ?udio de um v?deo no YouTube.
/r - pesquisa um termo no redit
/clima - Exibe informa??es de clima
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
/request - Faz uma requisi??o a um site
fala - Repete o texto que voce pedir para ele falar
site - exibe o site da equipe
facebook - exibe o facebook da equipe, cadastre-se
netflix - exibe nosso site de netflix gratis
iptv - exibe nosso site de iptv gratis
anime - exibe nosso site de anime gratis
pkg - exibe nosso site de pkg's para ps3 gratis
biblioteca - exibe nossa biblioteca hacker
curso - exibe nosso site de  cursos
doadores - exibe instru??es completas para doadores
painel - exibe nosso painel hacker

[*]COMANDOS EXCLUSIVOS DA ADM[*]
/ban - Bane um usuário.
/config - Envia um menu de configurações.
/defregras - Define as regras do grupo.
/kick - Kicka um usuário.
/mute - Restringe um usuário.
/pin - Fixa uma mensagem no grupo.
/title - Define o título do grupo.
/unban - Desbane um usuário.
/unmute - Desrestringe um usuário.
/unpin - Desfixa a mensagem fixada no grupo.
/unwarn - Remove as advertências do usuário.
/warn - Adverte um usuário.
/welcome - Define a mensagem de welcome.''',
                                      parse_mode='Markdown',
                                      reply_markup=cmds_back)
            return True


        elif msg['data'] == 'user_cmds':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      '''*Comandos para usuários normais:*

/admins - Mostra a lista de admins do chat.
/dados - Envia um número aleatório de 1 a 6.
/bug - Reporta um bug ao meu desenvolvedor.
/id - Exibe suas informações ou de um usuário.
/ping - Responde com uma mensagem de ping.
/regras - Exibe as regras do grupo.
/roleta - Para jogar a Roleta Russa.''',
                                      parse_mode='Markdown',
                                      reply_markup=cmds_back)
            return True


        elif msg['data'] == 'start_back':
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text=strs.get('commands_button'), callback_data='all_cmds')] +
                [dict(text=strs.get('infos_button'), callback_data='infos')],
                [dict(text=strs.get('lang_button'), callback_data='change_lang')] +
                [dict(text=strs.get('add_button'), url='https://t.me/{}?startgroup=new'.format(bot_username))]
            ])
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      strs.get('pm_start_msg'),
                                      reply_markup=kb)
            return True


        elif msg['data'] == 'change_lang':
            langs_kb = InlineKeyboardMarkup(inline_keyboard=
                                            [[dict(text='{lang_flag} {lang_name}'.format(**strings[x]),
                                                   callback_data='set_lang ' + x)] for x in strings] +
                                            [[dict(text=strs.get('back_button'), callback_data='start_back')]]
                                            )
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      "Select your prefered lang below:",
                                      reply_markup=langs_kb)
            return True


        elif msg['data'].split()[0] == 'set_lang':
            cursor.execute('UPDATE users SET chat_lang = ? WHERE user_id = ?',
                           (msg['data'].split()[1], msg['message']['chat']['id']))
            usr_lang = Strings(msg['message']['chat']['id'])
            start_back = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text=usr_lang.get('back_button'), callback_data='start_back')]
            ])
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      usr_lang.get('lang_changed'),
                                      reply_markup=start_back)
            return True


        elif msg['data'] == 'all_cmds':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      'Selecione uma categoria de comando para visualizar.\n\nCaso precise de ajuda com o bot ou tem alguma sugestão entre no @AmanoChat',
                                      reply_markup=keyboard.all_cmds)
            return True


        elif msg['data'] == 'infos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      '''• Manicomio Bot

Version: {version}
Nosso site: <a href="https://tcxsproject.com">Manicomio TCXS Project</a>
Developers: <a href="https://github.com/gorpo">GorpoOrko</>


Partnerships:
 » <a href="https://t.me/tcxsproject2">telegram</>

©2020 - <a href="https://t.me/tcxsproject2">TCXS Project™</>'''.format(version=version, sourcelink=git_repo[0]),
                                      parse_mode='html',
                                      reply_markup=start_back,
                                      disable_web_page_preview=True)
            return True
