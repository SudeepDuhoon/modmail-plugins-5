import discord
from discord.ext import commands
import asyncio
from datetime import datetime


class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.maincolor = 0x06c9ff
        self.errorcolor = 0xFF0000
        self.log_channel = 855018986936336407  # ID of the log channel
        self.defaultRole = 874129898707513344  # ID of the Discord Member role
        self.unverifiedRole = 874137536983875634 # ID of unverified role

    @commands.command(name="send-verify")
    @commands.has_permissions(administrator=True)
    async def sendverifymsg(self, ctx):
        embed = discord.Embed(
            title="**Verification**",
            description="To gain access to the Team Hope Discord Server, you will have to verify.\n\nVerifying means that you have agreed to our Rules and Guidelines\n\nOur Rules and Guidelines can be found in <#586650192896589840> and <#737311986697764954>!\n\nTo verify, please type `verify` in this channel!",
            color=self.maincolor
        )
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        else:
            if message.channel.id == 737356477404151856:
                if message.content.lower() == "verify":
                    guild = message.guild
                    role = guild.get_role(self.defaultRole)
                    un = guild.get_role(self.unverifiedRole)
                    await message.author.remove_roles(un)
                    await message.author.add_roles(role)
                    log_channel = guild.get_channel(self.log_channel)
                    await message.add_reaction("\U00002705")
                    embed = discord.Embed(
                        title="Someone just verified!",
                        description=f"{message.author.mention} just verified!\n\nHis ID is {message.author.id}\n\nThe message ID is {message.id}\nThe channel ID is {message.channel.id}\nThe message was sent at {message.created_at}",
                        color=self.maincolor
                    )
                    await log_channel.send(embed=embed)
                    await asyncio.sleep(2)
                    await message.delete()
                    try:
                        embed = discord.Embed(
                            title="Verification",
                            description="You are now verified in the Team Hope Discord Server!",
                            color=self.maincolor
                        )
                        await message.author.send(embed=embed)
                    except:
                        print(f"Couldn't send {message.author.name} his verification acceptation")

                else:
                    await message.delete()
                    return


def setup(bot):
    bot.add_cog(Verify(bot))
