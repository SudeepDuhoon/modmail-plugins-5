import discord
import json
import requests
from discord.ext import commands

class Genshin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = self.bot.main_color
        
    @commands.command(name="testing", aliases=['test'])
    async def bean(self, ctx, member: discord.Member = None, reason = None):
        await ctx.message.delete()
        if not member:
            embed = discord.Embed(title="Error", description="Please provide a user to bean!", color=self.bot.error_color)
            await ctx.send(embed=embed)
        else:
            if not reason:
                embed = discord.Embed(title="Bean | case 420", description=f"{member.mention} Has been beaned!", color=self.color)
                embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/819994849838366771.png")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Bean | case 69", description=f"{member.mention} Has been beaned for {reason}!", color=self.color)
                embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/819994849838366771.png")
                await ctx.send(embed=embed)          
                
    @commands.command(name="yuri3",aliases=["gaytime3"])
    async def gaytime(self, ctx):
        """
        Retrieves a random photo of Yae Sakura and Kallen Kaslana.
        """
        embed = discord.Embed(color=15383739, title='GI Bot', description="Currently we only provide Character's Brief Details. Feel free to support us with idea in [Github](https://github.com/rizkidn17/GenshinDiscordBot) or [Website](https://rizkidn17.github.io/GenshinDiscordBot/)")
        embed.set_footer(text='Disclaimer: This bot only for personal use and not related with Official Genshin Impact and Mihoyo')
        await ctx.send(embed=embed)
        
    
def setup(bot):
    bot.add_cog(Genshin(bot))
