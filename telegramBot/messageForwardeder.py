api_id=000000
api_hash='XXXXXXXXXXXXXXXX'
app_title='TheCoolInvestor'
app_short_name='TheCoolInvestor'

import asyncio
from telethon import TelegramClient, sync, events

client = TelegramClient('session_name', api_id, api_hash).start()


async def sendToGroups(event):
    await client.send_message(-1001945508703, event.message)
    await client.send_message(-1001833328420, event.message)
    await client.send_message(-1001905014374, event.message)
    await client.send_message(-1002121131434, event.message)
    await client.send_message(-1002133513866, event.message)
    await client.send_message(-1002056442424, event.message)

@client.on(events.NewMessage(chats=-1002008905623))
async def handler(event):
    await sendToGroups(event)

@client.on(events.NewMessage(chats=-1001809265514))
async def handler(event):
    await sendToGroups(event)

with client:
    print("Welcome back!!!\n")
    client.run_until_disconnected()