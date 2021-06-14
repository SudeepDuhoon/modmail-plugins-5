from discord.ext import commands
from datetime import date, datetime
import discord

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
        embed = discord.Embed(color=15383739)
        embed = discord.Embed(title="gay", description="wow im gay")
    if datetime.today().isoweekday() == 1:
        await ctx.send(embed=embed)
    else:
        if not datetime.today().isoweekday() == 1:
        embed = discord.Embed(title="Error", description="Please provide a user to bean!")
        await self.ctx.send(embed=)

def setup(bot):
    bot.add_cog(Daily(bot))
