import logging
from enum import Enum
from random import randint,choice
import discord
from discord.ext import commands
from core import checks
import box
import json
import string
from core.models import PermissionLevel

Cog = getattr(commands, "Cog", object)

logger = logging.getLogger("Modmail")

class Fun(Cog):
    """Some Fun commands"""
  
    ball = [
        "https://cdn.discordapp.com/attachments/803032600331157536/825162201114345542/20210326_201853.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/776158264093442109/20201111_135539.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/781680555544150026/20201126_193344.jpg"
    ]
    
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
        #self.db = bot.plugin_db.get_partition(self)
  
    @commands.command(name="aki",aliases=["cat"])
    async def _aki(self, ctx):
        embed = discord.Embed(title=':black_cat:', color=15383739)
        embed.set_image(url='https://cdn.discordapp.com/attachments/568778270598889472/781680555544150026/20201126_193344.jpg')
        await ctx.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Fun(bot))
