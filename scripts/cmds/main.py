import os
import discord

from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def test(self, ctx):
        await ctx.channel.send("test")

def setup(bot):
    print("TESTSETETSET")
    bot.add_cog(Main(bot))


    
