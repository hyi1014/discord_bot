import os
import discord
import requests
import json

from dotenv import load_dotenv

#Give the authority to the client
#plz check the develope application of intents
client = discord.Client(intents = discord.Intents.all())

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
          .format(client))
    
@client.event
async def on_message(cxt):
    if cxt.author == client.user:
        return
    if cxt.content.startswith('$'):
        pic = discord.File('D:\\discord_bot\\picture\\LINE_P2022831_200638.jpg')
        await cxt.channel.send(file = pic)
    args = cxt.content.split(' ')
    if args[0] == '$':
        if len(args) > 1:
            if args[1] == "talkshit":
                quote = get_quote()
                await cxt.channel.send(quote)
            if args[1] == 'hunk':
                pic = discord.File('D:\\discord_bot\\picture\\LINE_P2022831_200638.jpg')
                await cxt.send(file = pic)

    
        
load_dotenv()
client.run(os.getenv("DC_TOKEN", default=""))
