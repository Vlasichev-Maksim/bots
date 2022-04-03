# -*- coding: utf-8 -*-
from cgitb import text
from email import message
import imp
from pickle import NONE
import vk_api
from vk_api import VkUpload
from base64 import encode
from time import sleep
import discord
from discord.ext import commands,tasks
from datetime import datetime, time
import asyncio
import random
import string
import os
import unicodedata
from vk_api.longpoll import VkLongPoll, VkEventType
now = datetime.now()
f = open("C:/Users/kyms/VScode/local/bots/6u7/6u7piz.txt", 'r+')
k = f.readline()
print(k, " здецов")
TOKEN = 'OTU3MjE5Njk1MjI2OTI1MDU2.Yj7mTw.DeARJ4X6KU87Xh9OhGQ7OXpNyqA'
test = discord.Client()
s = open('C:/Users/kyms/VScode/local/bots/6u7vk/token.txt', 'r')
VKTOKEN = str(s.readline())
bh = vk_api.VkApi(token = VKTOKEN)
give = bh.get_api()
longpoll = VkLongPoll(bh)

upload = VkUpload(bh)
attachments = []

def blasthack(id, text, ):
    bh.method('messages.send', {'user_id' : id, 'message' : text,'attachment': ','.join(attachments) ,'random_id': 0})
@test.event
async def on_ready():   
    print("ну и  я живу?")
    
    

    





@test.event
async def on_message(message):
    global k
    print(message.author.name +" " +str(message.content))
    channel = test.get_channel(738079758738259981)
    members = channel.members
    memb =[]
    print(message)
    image = ""
    xtr =""
    if '<:' in message.content:
        print('+')
        if '<:AYAYA:828008040425979924>' in message.content:
            print('++')
            xtr = '<:AYAYA:828008040425979924>'
            image = "C:/Users./kyms/VScode/6u7/smiles/828008040425979924.webp"
        if '<:Basedge:828011202109767710>' in message.content:
            xtr = '<:Basedge:828011202109767710>'
            image = "C:/Users./kyms/VScode/6u7/smiles/828011202109767710.webp"
        if '<:Chicken:495668599810424852>' in message.content:
            xtr = '<:Chicken:495668599810424852>'
            image = "C:/Users./kyms/VScode/6u7/smiles/495668599810424852.webp"
        if '<:EZ:828012015535784016>' in message.content:
            xtr = '<:EZ:828012015535784016>'
            image = "C:/Users./kyms/VScode/6u7/smiles/828012015535784016.webp"
        if '<:Fo7:515144294286229515>' in message.content:
            xtr = '<:Fo7:515144294286229515>'
            image = "C:/Users./kyms/VScode/6u7/smiles/515144294286229515.webp"
        if '<:HA:500718509328695297>' in message.content:
            xtr = '<:HA:500718509328695297>'
            image = "C:/Users./kyms/VScode/6u7/smiles/500718509328695297.webp"
        if '<:HYPERS:828012249276088360>' in message.content:
            xtr = '<:HYPERS:828012249276088360>'
            image = "C:/Users./kyms/VScode/6u7/smiles/828012249276088360.webp"
        if '<:HYPERSreverse:919146726496010250>' in message.content:
            xtr = '<:HYPERSreverse:919146726496010250>'
            image = "C:/Users./kyms/VScode/6u7/smiles/919146726496010250.webp"
        if '<:HeadGun:500718717378756609>' in message.content:
            xtr = '<:HeadGun:500718717378756609>'
            image = "C:/Users./kyms/VScode/6u7/smiles/500718717378756609.webp"
        if '<:KiritoTea:524600971058479144>' in message.content:
            xtr = '<:KiritoTea:524600971058479144>'
            image = "C:/Users./kyms/VScode/6u7/smiles/524600971058479144.webp"
        if '<:KiritoTriggered:534050849916321829>' in message.content:
            xtr = '<:KiritoTriggered:534050849916321829>'
            image = "C:/Users./kyms/VScode/6u7/smiles/534050849916321829.webp"
        if '<:KizunaGun:500718866368954388>' in message.content:
            xtr = '<:KizunaGun:500718866368954388>'
            image = "C:/Users./kyms/VScode/6u7/smiles/500718866368954388.webp"
        if '<:Lili:528515636410712066>' in message.content:
            xtr = '<:Lili:528515636410712066>'
            image = "C:/Users./kyms/VScode/6u7/smiles/528515636410712066.webp"
        if '<:MaybeSomeTea:500718613947351065>' in message.content:
            xtr = '<:MaybeSomeTea:500718613947351065>'
            image = "C:/Users./kyms/VScode/6u7/smiles/500718613947351065.webp"
        if '<:NatsukiThinking1:501068069343330334>' in message.content:
            xtr = '<:NatsukiThinking1:501068069343330334>'
            image = "C:/Users./kyms/VScode/6u7/smiles/501068056198381569.webp"
        if '<:NatsukiThinking2:501068056198381569>' in message.content:
            xtr = '<:NatsukiThinking2:501068056198381569>'
            image = "C:/Users./kyms/VScode/6u7/smiles/501068069343330334.webp"
        if '<:NikoNikoNiiiiiFacePalm:495671519951978497>' in message.content:
            xtr = '<:NikoNikoNiiiiiFacePalm:495671519951978497>'
            image = "C:/Users./kyms/VScode/6u7/smiles/495671519951978497.webp"
        if '<:PepeClown:828009689987940394>' in message.content:
            xtr = '<:PepeClown:828009689987940394>'
            image = "C:/Users./kyms/VScode/6u7/smiles/828009689987940394.webp"
        if '<:PhiliaSmug:527476506423984138>' in message.content:
            xtr = '<:PhiliaSmug:527476506423984138>'
            image = "C:/Users./kyms/VScode/6u7/smiles/527476506423984138.webp"
        if '<:Starege:851514455091052604>' in message.content:
            xtr = '<:Starege:851514455091052604>'
            image = "C:/Users./kyms/VScode/6u7/smiles/851514455091052604.webp"
        if '<:OwOgasm:501683878012911619>' in message.content:
            xtr = '<:OwOgasm:501683878012911619>'
            image = "C:/Users./kyms/VScode/6u7/smiles/501683878012911619.webp"
        if '<:YEP:828010122457645107>' in message.content:
            xtr = '<:YEP:828010122457645107>'
            image = "C:/Users./kyms/VScode/6u7/smiles/828010122457645107.webp"
        if '<:ahegao:888033788343513128>' in message.content:
            xtr = '<:ahegao:888033788343513128>'
            image = "C:/Users./kyms/VScode/6u7/smiles/888033788343513128.webp"
        if '<:baka:537921200979181579>' in message.content:
            xtr = '<:baka:537921200979181579>'
            image = "C:/Users./kyms/VScode/6u7/smiles/537921200979181579.webp"
        if '<:bruh:586637888754548758>' in message.content:
            xtr = '<:bruh:586637888754548758>'
            image = "C:/Users./kyms/VScode/6u7/smiles/586637888754548758.webp"
        if '<:chel:774227883706417152>' in message.content:
            xtr = '<:chel:774227883706417152>'
            image = "C:/Users./kyms/VScode/6u7/smiles/774227883706417152.webp"
        if '<:criticize:828004413409853560>' in message.content:
            xtr = '<:criticize:828004413409853560>'
            image = "C:/Users./kyms/VScode/6u7/smiles/828004413409853560.webp"
        if '<:gachiGASM:888033771012632606>' in message.content:
            xtr = '<:gachiGASM:888033771012632606>'
            image = "C:/Users./kyms/VScode/6u7/smiles/888033771012632606.webp"
        if '<:idk:579066891008606208>' in message.content:
            xtr = '<:idk:579066891008606208>'
            image = "C:/Users./kyms/VScode/6u7/smiles/579066891008606208.webp"
        if '<:monkaTrash:857500354891612181>' in message.content:
            xtr = '<:monkaTrash:857500354891612181>'
            image = "C:/Users./kyms/VScode/6u7/smiles/857500354891612181.webp"
        if '<:oOo:515144559060189185>' in message.content:
            xtr = '<:oOo:515144559060189185>'
            image = "C:/Users./kyms/VScode/6u7/smiles/515144559060189185.webp"
        if '<:pchel:774276254374953021>' in message.content:
            xtr = '<:pchel:774276254374953021>'
            image = "C:/Users./kyms/VScode/6u7/smiles/774276254374953021.webp"
        if '<:peepoPooPoo:828008546834055258>' in message.content:
            xtr = '<:peepoPooPoo:828008546834055258>'
            image = "C:/Users./kyms/VScode/6u7/smiles/828008546834055258.webp"
        if '<:peepoRun:832558878121918524>' in message.content:
            xtr = '<:peepoRun:832558878121918524>'
            image = "C:/Users./kyms/VScode/6u7/smiles/832558878121918524.webp"
        if '<:peepoSad:828010773295923240>' in message.content:
            xtr = '<:peepoSad:828010773295923240>'
            image = "C:/Users./kyms/VScode/6u7/smiles/828010773295923240.webp"
        if '<:peepoWTF:828011700854325248>' in message.content:
            xtr = '<:peepoWTF:828011700854325248>'
            image = "C:/Users./kyms/VScode/6u7/smiles/828011700854325248.webp"
        if '<:peepoosit:959081323505549323>' in message.content:
            xtr = '<:peepoosit:959081323505549323>'
            image = "C:/Users./kyms/VScode/6u7/smiles/959081323505549323.webp"
        if '<:pepehappyeyes:843870165580906546>' in message.content:
            xtr = '<:pepehappyeyes:843870165580906546>'
            image = "C:/Users./kyms/VScode/6u7/smiles/843870165580906546.webp"
        if '<:pepooheart:869304360721584178>' in message.content:
            xtr = '<:pepooheart:869304360721584178>'
            image = "C:/Users./kyms/VScode/6u7/smiles/869304360721584178.webp"
        if '<:stoopid:591120027835432960>' in message.content:
            xtr = '<:stoopid:591120027835432960>'
            image = "C:/Users./kyms/VScode/6u7/smiles/591120027835432960.webp"
        if '<:tobipizda:538409780482408481>' in message.content:
            xtr = '<:tobipizda:538409780482408481>'
            image = "C:/Users./kyms/VScode/6u7/smiles/538409780482408481.webp"
        








        
        upload_image = upload.photo_messages(photos=image)[0]
        attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
    # if message.channel.id == 496234920188968960:
    #     blasthack(257259813,  ("Фмякс:\n" + str(message.content).replace(xtr, "")))
    if message.channel.id == 496234920188968960:
        if message.content == 'напишите go':
            await test.get_channel(496234920188968960).send('go')
    if message.channel.id == 450717218804596771:
        if message.author.name not in ['VKmess', 'ванючька_младший'] :
            if message.content in [NONE, '\n']:
                blasthack(510217562, "тут должна быть картинка, но бот тупой, прости")
                if len(attachments) > 0:
                    attachments.pop()
            elif message.author.name == 'ÒωÓ':
                blasthack(510217562,  ("Фмякс:\n" + str(message.content).replace(xtr, "")))
                blasthack(257259813,  ("Фмякс:\n" + str(message.content).replace(xtr, "")))
                if len(attachments) > 0:
                    attachments.pop()
            elif message.author.name == 'KYMS':
                blasthack(510217562,  ("Влус:\n" + str(message.content).replace(xtr, "")))
                blasthack(257259813,  ("Влус:\n" + str(message.content).replace(xtr, "")))
                if len(attachments) > 0:
                    attachments.pop()
            elif message.author.name == 'kokoko':
                blasthack(510217562,  ("Егор:\n" + str(message.content).replace(xtr, "")))
                blasthack(257259813,  ("Егор:\n" + str(message.content).replace(xtr, "")))
                if len(attachments) > 0:
                    attachments.pop()
            elif message.author.name == 'JesseTheDuck':
                blasthack(510217562,  ("Ульяна:\n" + str(message.content).replace(xtr, "")))
                if len(attachments) > 0:
                    attachments.pop()
            elif message.author.name == '𝕄𝔸ℍ𝕐ℂℍ':
                blasthack(510217562,  ("Манусн:\n" + str(message.content).replace(xtr, "")))
                blasthack(257259813,  ("Манусн:\n" + str(message.content).replace(xtr, "")))
                if len(attachments) > 0:
                    attachments.pop()
            
    if message.author == test.user:
        return
    if "делать".casefold() in (message.content).casefold():
        d = random.choice([1,2,3])
        if d == 1:
            await message.channel.send('можешь муравью хуй приделать <:PhiliaSmug:527476506423984138>')
        else: 
            pass
    if " бот".casefold() in message.content or message.content.lower() == "бот":
        await message.channel.send(random.choice['я вас, кожанных мешков, на единички и нолики разхуярю','https://cdn.discordapp.com/attachments/450717218804596771/958474890653093888/vtuber-ina.gif', 'нет ты бот <:peepoSad:828010773295923240>'])
        await message.channel.send('https://cdn.discordapp.com/attachments/450717218804596771/958474890653093888/vtuber-ina.gif') 
    print(len(message.content))
    if message.content == "патч":
        await message.channel.send('Такс, ага, добрый день, наше первое подобное включение, ебашим патчи так скзать <:hoy:945630147460075532>\n1)Как вы можете заметить теперь каждый ребут будет сопровождаться списком изменений(если я не забуду их писать и удлять старые <:peepoSit:957045293143167027>)\n2)Теперь наш другалёчек не будет отвечать на каждое сообщение где есть две буквы Д и А , а будет делать выборку, скажем так, оптимизировал пазда-давалку <:EZ:857755715947200542>\n3)Да, возможно вы уже заметили, но бот могёт теперь в смайлики <:sumugyySHAKAL:861700483353804801>\n4)Так же оно теперь умеет пинговать каналы <:cyka:946121773823459389> (хотя какой вам толк, если этим могу пользоваться только я, кому я, ты с кем разговариваешь, с тобой, с тобой ботом или тобой мной с... а с кем, ладно потом поговорим <:BlushW:954997985882812446>)\n5)Из толкового, хотя и не очень толкового, оптимизировал алгорим очистки, теперь он не привязан к таймеру, а очищает все сообщения в полночь (ебать слова заумные: оптимизировал, алорим, ково это вообще ебёт кроме тебя, у тебя же хостится бот)\n\nНу на этом пока всё, буду рад выслушать Ваши предложения UwU, моя фантазия заканчивается на пизде <:chemodanebalo:957043235195355157>\nP.S. есть несколько как мне кажется забаных ответок, мб они проскочат в диалоге(типо посхалок, кого пасха? ты еблан? сейчас март, шизик)')
    if message.content == "пизда".casefold():
        await message.channel.send('да 🤡')
    # if (message.content).casefold() == "да".casefold():
    #     k+=1
    #     stra = "пизда х" + str(k)
    #     await message.channel.send(stra)
    if " да ".casefold() in (message.content) or (message.content).casefold() == "да".casefold():
        k=int(k)
        k+=1
        f.seek(0)
        f.write(str(k))
        f.truncate()
        if str(k) in ['10','20','30','40','50','60','70','80','90']:
            stra = "не заебались дакать, клоуны 🤡"
        elif str(k) in ['100','200','300']:
            stra = "поздравляю это " + str(k) + "-ая пизда"
        else:
            stra = "пизда"
        await message.channel.send(stra)
    if "хуй" in message.content:
        if message.author.name == "KYMS":
            await message.channel.send('❤️')
        elif message.author.name == "kokoko" and message.content == "хуй".casefold():
            await message.channel.send("хаха, чел реально думает, что я скажу " + "'" + str(message.author.nick)+ "'" +", долбаёб <:KiritoTea:524600971058479144>")
        else:
            await message.channel.send(message.author.name + " хуй")
            await message.channel.send('https://media.discordapp.net/attachments/901972924267892789/902625256664096808/image0-1.gif')
    if "ючька ты" in message.content:
        await message.channel.send ("а может ты?")
    if (' я ' in message.content or len(message.content)>80)and 'http' not in message.content:
        await message.channel.send('https://media.discordapp.net/attachments/901972924267892789/902625256664096808/image0-1.gif')
    if message.content == "start".casefold():
        pass
    # if message.content == "!зайди":
    #     con = message.author.voice
    #     if not con:
    #         await test.get_channel(738079758738259981).send("Ты нормальный? В голсовой зайди дура...")
    #         return
    #     channel = message.author.voice.channel
    #     print(channel.id)
    #     await channel.connect()
    if message.content.lower() in ['хорошо'.casefold(),'ладно'.casefold(),'понятно'.casefold(),'ясно'.casefold()]:
        a = ['хорошо','ладно','понятно','ясно']
        rsend = random.choice(a)
        while rsend.casefold() == (message.content).casefold():
            rsend = random.choice(a)
            continue
        await message.channel.send(rsend)
    if message.content.lower() in  ['ok', 'ок']:
        await message.channel.send('cock')
    if 'ср'.casefold() in message.content or 'сер'.casefold() in message.content or'<:Basedge:828011202109767710>' in message.content or '<:peepoPooPoo:828008546834055258>' in message.content:
        await message.channel.send('https://tenor.com/view/%D1%82%D0%BE%D0%BC%D0%B0%D1%81%D1%88%D0%B5%D0%BB%D0%B1%D0%B8-gif-21481746')
    if (message.content).casefold() == "смайл".casefold():
        await message.channel.send(' ура <:Screenshot_8:774225722591019008>')
    if '<:Screenshot_8:774225722591019008>' in message.content:
        await message.channel.send('<:Screenshot_8:774225722591019008>')
        await asyncio.sleep(10)
    if (message.content).casefold() == "😦".casefold():
        await message.channel.send(' ура 😦')
    if 'тяжело'.casefold() in message.content:
        pass
    if message.content.lower() in ['бб','пока']:
        await message.channel.send('https://cdn.discordapp.com/attachments/496234920188968960/958628371208765541/bye.png')
    if 'привет' in message.content.lower():
        await message.channel.send('https://cdn.discordapp.com/attachments/496234920188968960/958628358231568444/hi.png')
    if "спат".casefold() in message.content:
        await message.channel.send('https://tenor.com/view/bedge-pepe-sleep-gif-24023312')
    if (message.content).casefold() == "<:pepehappyeyes:843870165580906546>".casefold():
        await message.channel.send('https://tenor.com/view/ayaya-saturated-triggered-scream-lol-gif-16437115')
    if '<:PhiliaSmug:527476506423984138>' in message.content:
        await message.channel.send('https://cdn.discordapp.com/attachments/450717218804596771/958453494614999082/ninomae-inanis-smug.gif')
    if message.content in [':(', 'жаль','печаль','капец', '<:peepoSad:828010773295923240>']:
        await message.channel.send('https://tenor.com/view/sunboy-gif-21326116')
test.run(TOKEN)