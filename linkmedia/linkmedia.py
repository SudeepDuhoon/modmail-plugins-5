import asyncio
import discord
from discord.ext import commands
from pymongo import ReturnDocument

from core import checks
from core.models import PermissionLevel


class Medialink(commands.Cog):
    """Sets up media+link channel in discord. edited from 4jr's emoji plugin"""

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)
        bot.loop.create_task(self.load_variables())

    async def load_variables(self):
        self.config = await self.db.find_one({'_id': 'config'}) or {}

    async def delete(self, message, warning):
        if warning:
            await message.channel.send(warning, delete_after=10)
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
                if not ('youtube' in message.content or 'facebook' in message.content or 'discord' in message.content or 'tiktok' in message.content or 'instagram' in message.content or 'twitter' in message.content or 'png' in message.content or 'jpg' in message.content or 'gif' in message.content or 'jpeg' in message.content or 'mov' in message.content  or 'mp4' in message.content):
                    await self.delete(message, warning=f'{message.author.mention}, only direct media links and YouTube, Facebook, Discord, Tiktok, Instagram, Twitter links are allowed. Contact @Eden Support#3893 if you want to add any other website.')

            elif len(message.attachments):
                if not (message.attachments[0].filename.endswith('.png') or message.attachments[0].filename.endswith('.gif') or message.attachments[0].filename.endswith('.jpeg') or message.attachments[0].filename.endswith('.jpg') or message.attachments[0].filename.endswith('.mov') or message.attachments[0].filename.endswith('.mp4')):
                    await self.delete(message, warning=f'{message.author.mention}, only png, gif, jpg, jpeg, mov and mp4 attachemnets are allowed here 📷')

            else:
                await self.delete(message, warning=f'{message.author.mention}, only media + captions and their links are allowed. If you wish to add a caption, edit your original message.')


    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    @commands.group(invoke_without_command=True)
    async def mediachannels(self, ctx):
        """Configure media+links only Channels, accepted media files are png, gif, jpg, jpeg, mov and mp4"""
        """accepted websites are YouTube, Facebook, Discord, Tiktok, Instagram and Twitter"""
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
    bot.add_cog(Medialink(bot))
