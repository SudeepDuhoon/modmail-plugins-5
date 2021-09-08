import asyncio
import discord
from discord.ext import commands
from pymongo import ReturnDocument

from core import checks
from core.models import PermissionLevel


class Mediaonly(commands.Cog):
    """Sets up media channel in discord. edited from 4jr's emoji plugin"""

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)
        bot.loop.create_task(self.load_variables())

    async def load_variables(self):
        self.config = await self.db.find_one({'_id': 'config'}) or {}

    async def delete(self, message, warning):
        if warning:
            await message.channel.send(warning, delete_after=5)
        try:
            await message.delete()
        except discord.NotFound:
            pass

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.config.get('status', True) and message.channel.id in self.config.get('channel_ids', []):
            if message.author.bot:
                await asyncio.sleep(5)
                await self.delete(message, warning=None)
            elif 'http' in message.content:
                if ('danbooru' in message.content or 'google' in message.content or 'pinterest' in message.content or 'safebooru' in message.content or 'gelbooru' in message.content):
                    await self.delete(message, warning=f'{message.author.mention}, this is not a primary source. Please repost with a link to the original artist. Example: <https://www.hoyolab.com/genshin/article/864292>')

            else:
                await self.delete(message, warning=f'{message.author.mention}, please repost with the source of the image as a full link. Example: <https://www.hoyolab.com/genshin/article/864292>')


    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    @commands.group(invoke_without_command=True)
    async def mediachannels(self, ctx):
        """Configure media only Channels, accepted media files are png, gif, jpg, jpeg and mp4"""
        await ctx.send_help(ctx.command)

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    @mediachannels.command(aliases=['channel'])
    async def channels(self, ctx, *channels_: discord.TextChannel):
        """Configure media Channel(s)"""
        self.config = await self.db.find_one_and_update(
            {'_id': 'config'}, {'$set': {'channel_ids': [i.id for i in channels_]}},
            return_document=ReturnDocument.AFTER,
            upsert=True
        )
        await ctx.send('Config set.')
        
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    @mediachannels.command()
    async def toggle(self, ctx):
        """Toggles status of the plugin"""
        self.config = await self.db.find_one_and_update(
            {'_id': 'config'}, {'$set': {'status': not self.config.get('status', True)}},
            return_document=ReturnDocument.AFTER,
            upsert=True
        )
        await ctx.send(f'Config set: Status {self.config.get("status", True)}.')


def setup(bot):
    bot.add_cog(Mediaonly(bot))
