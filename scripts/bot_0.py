import os
import discord
# import requests
# import json

from dotenv import load_dotenv
from discord.ext import commands
#Give the authority to the client
#plz check the develope application of intents

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
# with open('setting.json', mode='r', encoding='utf8') as jflie:
#     jdata = json.load(jflie)

@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))
#
# @client.event
# async def on_message(cxt):
#     if cxt.author == client.user:
#         return
#     if cxt.content.startswith('$'):
#         pic = discord.File('D:\\discord_bot\\picture\\LINE_P2022831_200638.jpg')
#         await cxt.channel.send(file = pic)
#     args = cxt.content.split(' ')
#     if args[0] == '$':
#         if len(args) > 1:
#             if args[1] == "talkshit":
#                 quote = get_quote()
#                 await cxt.channel.send(quote)
#             if args[1] == 'hunk'
#                 pic = discord.File('D:\\discord_bot\\picture\\LINE_P2022831_200638.jpg')
#                 await cxt.send(file =y pic)
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        # print(F'cmds.{filename[:-3]}')
        # await bot.load_extension(F'cmds.{filename[-3]}')
        bot.load_extension(f'cmds.{filename[:-3]}')
        print(filename)

load_dotenv()
bot.run(os.getenv("DC_TOKEN", default=""))
