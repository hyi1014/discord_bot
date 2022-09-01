import os
import discord
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
          .format(client))
    
@client.event
async def on_message(cxt):
    if cxt.author == client.user:
        return
    
    if cxt.content.startswith('$'):
        await cxt.channel.send('bibibi')
        
load_dotenv()
client.run(os.getenv("DC_TOKEN", default=""))