import vk_api
import os
import string
import asyncio
import discord
from vk_api.longpoll import VkLongPoll, VkEventType
f = open('C:/Users/kyms/VScode/local/bots/6u7vk/token.txt')
DTOKEN = 'OTU4Nzc3NDY4NDYwODg4MTI3.YkSRGQ.0Zrlom-tFly0vAt-qDgDoBXHr8A'
TOKEN = str(f.readline())
bh = vk_api.VkApi(token = TOKEN)
give = bh.get_api()
longpoll = VkLongPoll(bh)
test = discord.Client()
@test.event
async def on_ready(): 
    print('yep')
    await test.get_channel(496234920188968960).send('напишите go')
    
@test.event
async def on_message(message):
    if message.content == 'go':
        print('lets go')
        while True:
            for event in longpoll.listen():
                print(longpoll.listen(), event.type, VkEventType.MESSAGE_NEW)
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        png_url = event.message['attachments'][0]['photo']['sizes'][-1]['url']
                        vkmessage = event.text.lower()
                        id = event.user_id
                        print(id)
                        vkms = str(vkmessage)
                        await test.get_channel(450717218804596771).send(vkms)
                        if png_url != '':
                            await test.get_channel(450717218804596771).send(png_url)
                        
test.run(DTOKEN)