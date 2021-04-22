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

class Thighs(Cog):
    """
    Commands that Sage has made for the server.
    """
  
    image = [
        "https://i.imgur.com/hj6KIMe.png",
        "https://i.imgur.com/xUaAxak.png",
        "https://i.imgur.com/RaqNOao.png",
        "https://cdn.discordapp.com/attachments/819078728130887742/834687080000913419/qGnFz6r.gif",
        "https://i.imgur.com/K3BKdDn.png",
        "https://i.imgur.com/9dNehDs.png",
        "https://i.imgur.com/crRccvJ.png",
        "https://i.imgur.com/EJMitjX.png",
        "https://i.imgur.com/gSsGYP2.png"
    ]
    
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
        #self.db = bot.plugin_db.get_partition(self)
  
    @commands.command(name="thighs",aliases=["thigh"])
    async def _thighs(self, ctx):
    channel = client.get_channel(822310331321155665)
    if channel == ctx.channel:
        """
        Retrieves a random photo of Honkai Thighs.
        """
        embed = discord.Embed(color=15383739)
        embed.set_image(url=choice(self.image))
        await ctx.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Thighs(bot))
