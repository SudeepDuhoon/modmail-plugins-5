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

class Yuri(Cog):
    """
    Commands that Sage has made for the server.
    """
  
    image = [
        "https://cdn.discordapp.com/attachments/799069920402341893/833069759120801842/maxresdefault-2.png",
        "https://safebooru.org//samples/3024/sample_b820a529526c890d5da3786ff121c8fc30e61e97.jpg?3148813"
    ]
    
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
        #self.db = bot.plugin_db.get_partition(self)
  
    @commands.command(name="yuri",aliases=["gaytime"])
    async def _gaytime(self, ctx):
        """
        Retrieves a random photo of Yae Sakura and Kallen Kaslana.
        """
        embed = discord.Embed(color=15383739)
        embed.set_image(url=choice(self.image))
        await ctx.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Yuri(bot))
