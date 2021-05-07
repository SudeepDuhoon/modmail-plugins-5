import os
import discord
import requests
import json
from discord.ext import commands

class Genshin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def about2(self, ctx):
    embeded = discord.Embed(title='GI Bot',description="Currently we only provide Character's Brief Details. Feel free to support us with idea in [Github](https://github.com/rizkidn17/GenshinDiscordBot) or [Website](https://rizkidn17.github.io/GenshinDiscordBot/)")
    embeded.set_footer(text='Disclaimer: This bot only for personal use and not related with Official Genshin Impact and Mihoyo')
    await ctx.send(embed=embeded)
    
def setup(bot):
    bot.add_cog(Genshin(bot))
