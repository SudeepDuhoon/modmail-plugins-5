from discord.ext import commands
from datetime import date, datetime
import discord

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
        if datetime.today().isoweekday() == 0:
            # it is Sunday
            embed = discord.Embed(title="Sunday", description="It is Sunday.")
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 1:
            # it is Monday
            embed = discord.Embed(title="Monday", colour=discord.Colour(0x51c47a), description="It is Monday.")
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 2:
            # it is Tuesday
            embed = discord.Embed(title="Tuesday", colour=discord.Colour(0x51c47a), description="It is Tuesday.")
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 3:
            # it is Wednesday
            embed = discord.Embed(title="Wednesday", colour=discord.Colour(0x51c47a), description="It is Wednesday.")
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 4:
            # it is Thursday
            embed = discord.Embed(title="Thursday", colour=discord.Colour(0x51c47a), description="It is Thursday.")
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 5:
            # it is Friday
            embed = discord.Embed(title="Friday", colour=discord.Colour(0x51c47a), description="It is Friday.")
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 6:
            # it is Friday
            embed = discord.Embed(title="Saturday", colour=discord.Colour(0x51c47a), description="It is Saturday.")
            await ctx.send(embed=embed)   

def setup(bot):
    bot.add_cog(Daily(bot))
