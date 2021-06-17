import discord
from discord.ext import commands
from core import checks


class AutoMute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # On channel create set up mute stuff
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        guild = channel.guild
        role = discord.utils.get(guild.roles, name="Muted")
        if role == None:
            role = await guild.create_role(name="Muted")
        await channel.set_permissions(role, send_messages=False, add_reactions=False)


def setup(bot):
    bot.add_cog(AutoMute(bot))
