from discord.ext import commands
import discord

class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = self.bot.main_color

    @commands.command()
    async def faq(self, ctx):
        embed = discord.Embed(title="gay", description="wow im gay")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FAQ(bot))
