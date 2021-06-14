from discord.ext import commands
from datetime import date, datetime
import discord

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
    if datetime.today().isoweekday() == 1:
        embed = discord.Embed(color=15383739)
        embed=discord.Embed(title="gay", description="wow im gay")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color=15383739)
        embed=discord.Embed(title="it is monday", description="wow im gay")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Daily(bot))
