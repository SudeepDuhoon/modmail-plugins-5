from discord.ext import commands
from datetime import date, datetime
import discord

class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def faq(self, ctx):
        if datetime.today().isoweekday() == 1:
            embed = discord.Embed(title="gay", description="wow im gay")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FAQ(bot))
