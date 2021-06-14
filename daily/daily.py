from discord.ext import commands
import discord

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
    if date.today().weekday() == 0:
        embed = discord.Embed(color=15383739)
        embed = discord.Embed(title="gay", description="wow im gay")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="Please provide a user to bean!")
        await self.ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Daily(bot))
