import discord
import os
from dotenv import load_dotenv

import sys
sys.path.append(r'D:\project\footystats')
from server.api import static

from datetime import datetime

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$gw1'):
        live = static()
        events = live.get_events()
        await message.channel.send(f'Deadline time: {datetime.fromisoformat(events.iloc[0][2]).date()}')

client.run(os.environ.get('TOKEN'))
