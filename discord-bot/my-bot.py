from datetime import datetime
import discord
import os
from dotenv import load_dotenv

import sys
sys.path.append(r'D:\project\footystats')
from server.api import static

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

    if message.content.startswith('$dl'):
        live = static()
        events = live.get_events()
        gwid = message.content[3:]
        deadline = datetime.fromisoformat(events.iloc[int(gwid)-1][2]).strftime('%I:%M%p %b %d %Y')
        await message.channel.send(f'Deadline time for gameweek {gwid}: {deadline}.')

client.run(os.environ.get('TOKEN'))