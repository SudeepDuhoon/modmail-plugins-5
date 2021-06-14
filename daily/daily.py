from discord.ext import commands
import discord

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(color=15383739)
        embed = discord.Embed(title="gay", description="wow im gay")

def setup(bot):
    bot.add_cog(Daily(bot))
