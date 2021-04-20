import discord
from discord.ext import commands

class bean(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = self.bot.main_color
        
    @commands.command(name="bean", aliases=['fban'])
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
        
def setup(bot):
    bot.add_cog(bean(bot))
