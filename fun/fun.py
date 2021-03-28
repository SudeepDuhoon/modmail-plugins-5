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
        "As I see it, yes",
        "It is certain",
        "It is decidedly so",
        "Most likely",
        "Outlook good",
        "Signs point to yes",
        "Without a doubt",
        "Yes",
        "Yes – definitely",
        "You may rely on it",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
        #self.db = bot.plugin_db.get_partition(self)
  
    @commands.command(name="8ball",aliases=["8"])
    async def _8ball(self, ctx, *, question: str):
        """Ask 8 ball a question.
        Question must end with a question mark.
        """
        embed = discord.Embed(title='Question: | :8ball:', description=question, color=0x2332e4)
        embed.add_field(name='Answer:', value=choice(self.ball), inline=False)
        
        if question.endswith("?") and question != "?":
            await ctx.send(embed=embed)
        else:
            await ctx.send("That doesn't look like a question.")
      
def setup(bot):
    bot.add_cog(Fun(bot))
