import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import re
import asyncio
import sys
import traceback

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h":3600, "s":1, "m":60, "d":86400}

class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for v, k in matches:
            try:
                time += time_dict[k] * float(v)
            except KeyError:
                raise commands.BadArgument("{} is an invalid time-key! h/m/s/d are valid!".format(k))
            except ValueError:
                raise commands.BadArgument("{} is not a number!".format(v))
        return time

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.errorcolor = 0xFF2B2B
        self.blurple = 0x7289DA

    #On channel create set up mute stuff
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        guild = channel.guild
        role = discord.utils.get(guild.roles, name = "Muted")
        if role == None:
            role = await guild.create_role(name = "Muted")
        await channel.set_permissions(role, send_messages = False)

    #Purge
    @commands.command(aliases = ["clear"])
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def purge(self, ctx, amount = 10):
        max_purge = 2000
        if amount >= 1 and amount <= max_purge:
            await ctx.channel.purge(limit = amount + 1)
            embed = discord.Embed(
                title = "Purge",
                description = f"Purged {amount} message(s)!",
                color = self.blurple
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
            if modlog == None:
                return
            if modlog != None:
                embed = discord.Embed(
                    title = "Purge",
                    description = f"{amount} message(s) have been purged by {ctx.author.mention} in {ctx.message.channel.mention}",
                    color = self.blurple
                )
                await modlog.send(embed = embed)
        if amount < 1:
            embed = discord.Embed(
                title = "Purge Error",
                description = f"You must purge more then {amount} message(s)!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            await ctx.message.delete()
        if amount > max_purge:
            embed = discord.Embed(
                title = "Purge Error",
                description = f"You must purge less then {amount} messages!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            await ctx.message.delete()

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions",
                description = "You are missing the **Supporter** permission level!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            await ctx.message.delete()

    #Kick
    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def kick(self, ctx, member : discord.Member = None, *, reason = None):
        if member == None:
            embed = discord.Embed(
                title = "Kick Error",
                description = "Please specify a member!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
        else:
            if member.id == ctx.message.author.id:
                embed = discord.Embed(
                    title = "Kick Error",
                    description = "You can't kick yourself!",
                    color = self.blurple
                )
                await ctx.send(embed = embed)
            else:
                if reason == None:
                    await member.kick(reason = f"Moderator - {ctx.message.author.name}#{ctx.message.author.discriminator}.\nReason - No reason proivded.")
                    embed = discord.Embed(
                        title = "Kick",
                        description = f"{member.mention} has been kicked by {ctx.message.author.mention}.",
                        color = self.blurple
                    )
                    await ctx.send(embed = embed)
                    modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
                    if modlog == None:
                        return
                    if modlog != None:
                        embed = discord.Embed(
                            title = "Kick",
                            description = f"{member.mention} has been kicked by {ctx.message.author.mention} in {ctx.message.channel.mention}.",
                            color = self.blurple
                        )
                        await modlog.send(embed = embed)
                else:
                    await member.kick(reason = f"Moderator - {ctx.message.author.name}#{ctx.message.author.discriminator}.\nReason - {reason}")
                    embed = discord.Embed(
                        title = "Kick",
                        description = f"{member.mention} has been kicked by {ctx.message.author.mention} for {reason}",
                        color = self.blurple
                    )
                    await ctx.send(embed = embed)
                    modlog = discord.utils.get(ctx.guild.text_channels, name = "modlog")
                    if modlog == None:
                        return
                    if modlog != None:
                        embed = discord.Embed(
                            title = "Kick",
                            description = f"{member.mention} has been kicked by {ctx.message.author.mention} in {ctx.message.channel.mention} for {reason}",
                            color = self.blurple
                        )
                        await modlog.send(embed = embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions",
                description = "You are missing the **Moderator** permission level!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)

    #Ban
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def ban(self, ctx, member : discord.Member = None, *, reason = None):
        if member == None:
            embed = discord.Embed(
                title = "Ban Error",
                description = "Please specify a user!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        else:
            if member.id == ctx.message.author.id:
                embed = discord.Embed(
                    title = "Ban Error",
                    description = "You can't ban yourself!",
                    color = self.blurple
                )
                await ctx.send(embed = embed)
            else:
                if reason == None:
                    await member.ban(reason = f"Moderator - {ctx.message.author.name}#{ctx.message.author.discriminator}.\nReason - No Reason Provided.")
                    embed = discord.Embed(
                        title = "Ban",
                        description = f"{member.mention} has been banned by {ctx.message.author.mention}.",
                        color = self.blurple
                    )
                    modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
                    if modlog == None:
                        return
                    if modlog != None:
                        embed = discord.Embed(
                            title = "Ban",
                            description = f"{member.mention} has been banned by {ctx.message.author.mention}.",
                            color = self.blurple
                        )
                        await modlog.send(embed = embed)
                else:
                    await member.ban(reason = f"Moderator - {ctx.message.author.name}#{ctx.message.author.discriminator}.\nReason - {reason}")
                    embed = discord.Embed(
                        title = "Ban",
                        description = f"{member.mention} has been banned by {ctx.message.author.mention} for {reason}",
                        color = self.blurple
                    )
                    await ctx.send(embed = embed)
                    modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
                    if modlog == None:
                        return
                    if modlog != None:
                        embed = discord.Embed(
                            title = "Ban",
                            description = f"{member.mention} has been banned by {ctx.message.author.mention} in {ctx.message.channel.mention} for {reason}",
                            color = self.blurple
                        )
                        await modlog.send(embed = embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions",
                description = "You are missing the **Administrator** permission level!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)

    #Unban
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def unban(self, ctx, *, member : discord.User = None):
        if member == None:
            embed = discord.Embed(
                title = "Unban Error",
                description = "Please specify a user!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
        else:
            banned_users = await ctx.guild.bans()
            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member.name, member.discriminator):
                    embed = discord.Embed(
                        title = "Unban",
                        description = f"Unbanned {user.mention}",
                        color = self.blurple
                    )
                    await ctx.guild.unban(user)
                    await ctx.send(embed = embed)
                    modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
                    if modlog == None:
                        return
                    if modlog != None:
                        embed = discord.Embed(
                            title = "Ban",
                            description = f"{user.mention} has been unbanned by {ctx.message.author.mention} in {ctx.message.channel.mention}.",
                            color = self.blurple
                        )
                        await modlog.send(embed = embed)


    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions",
                description = "You are missing the **Administrator** permission level!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)

    #Mute
    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def mute(self, ctx, member : discord.Member = None, *, reason = None):
        if member == None:
            embed = discord.Embed(
                title = "Mute Error",
                description = "Please specify a user!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
        else:
            if member.id == ctx.message.author.id:
                embed = discord.Embed(
                    title = "Mute Error",
                    description = "You can't mute yourself!",
                    color = self.errorcolor
                )
                await ctx.send(embed = embed, delete_after = 5.0)
            else:
                if reason == None:
                    role = discord.utils.get(ctx.guild.roles, name = "Muted")
                    if role == None:
                        role = await ctx.guild.create_role(name = "Muted")
                        for channel in ctx.guild.text_channels:
                            await channel.set_permissions(role, send_messages = False)
                    await member.add_roles(role)
                    embed = discord.Embed(
                        title = "Mute",
                        description = f"{member.mention} has been muted by {ctx.message.author.mention}.",
                        color = self.blurple
                    )
                    await ctx.send(embed = embed)
                    modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
                    if modlog == None:
                        return
                    if modlog != None:
                        embed = discord.Embed(
                            title = "Mute",
                            description = f"{member.mention} has been muted by {ctx.message.author.mention} in {ctx.message.channel.mention}.",
                            color = self.blurple
                        )
                        await modlog.send(embed = embed)
                else:
                    role = discord.utils.get(ctx.guild.roles, name = "Muted")
                    if role == None:
                        role = await ctx.guild.create_role(name = "Muted")
                        for channel in ctx.guild.text_channels:
                            await channel.set_permissions(role, send_messages = False)
                    await member.add_roles(role)
                    embed = discord.Embed(
                        title = "Mute",
                        description = f"{member.mention} has been muted by {ctx.message.author.mention} for {reason}",
                        color = self.blurple
                    )
                    await ctx.send(embed = embed)
                    modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
                    if modlog == None:
                        return
                    if modlog != None:
                        embed = discord.Embed(
                            title = "Mute",
                            description = f"{member.mention} has been muted by {ctx.message.author.mention} in {ctx.message.channel.mention} for {reason}",
                            color = self.blurple
                        )
                        await modlog.send(embed = embed)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions!",
                description = "You are missing the **Moderator** permission level!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)

    #Unmute command
    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def unmute(self, ctx, member : discord.Member = None):
        if member == None:
            embed = discord.Embed(
                title = "Unmute Error",
                description = "Please specify a user!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
        else:
            role = discord.utils.get(ctx.guild.roles, name = "Muted")
            if role in member.roles:
                await member.remove_roles(role)
                embed = discord.Embed(
                    title = "Unmute",
                    description = f"{member.mention} has been unmuted by {ctx.message.author.mention}.",
                    color = self.blurple
                )
                await ctx.send(embed = embed)
                modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
                if modlog == None:
                    return
                if modlog != None:
                    embed = discord.Embed(
                        title = "Unmute",
                        description = f"{member.mention} has been unmuted by {ctx.message.author.mention} in {ctx.message.channel.mention}.",
                        color = self.blurple
                    )
                    await modlog.send(embed = embed)
            else:
                embed = discord.Embed(
                    title = "Unmute Error",
                    description = f"{member.mention} is not muted!",
                    color = self.errorcolor
                )
                await ctx.send(embed = embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions!",
                description = "You are missing the **Moderator** permission level!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)

    #TempMute
    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def tempmute(self, ctx, member : discord.Member = None, *, time:TimeConverter = None):
        """Mutes a member for the specified time- time in 2d 10h 3m 2s format ex:
        &mute @Someone 1d"""
        print(1)
        if time == None:
            embed = discord.Embed(
                title= "Error",
                description= "Please specify a time",
                color= 0xFF0000
            )
            await ctx.send(embed=embed)
            print(2)
        if member == None:
            embed = discord.Embed(
                title= "Error",
                description= "Please specify a member to mute",
                color= 0xFF0000
            )
            await ctx.send(embed=embed)
            print(3)
        else:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            if role == None:
                role = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.text_channels:
                    await channel.set_permissions(role, send_messages=False)
                await member.add_roles(role)
                embed = discord.Embed(
                    title= "Mute",
                    description= f"{member.mention} has been muted by {ctx.message.author.mention} for {time}s",
                    color=0x00FF00
                )
                await ctx.send(embed=embed)
                print(4)
                embed = discord.Embed(
                    title= "Muted",
                    description= f"You have been muted in {ctx.guiild.name} by {ctx.author.mention} for {time}",
                    color=0x06c9ff
                )
                await member.send(embed=embed)
                print(5)
            if time:
                await asyncio.sleep(time)
                await member.remove_roles(role)
                print(6)
             
    @tempmute.error
    async def tempmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Error",
                description="You do not have permissions to tempmute members!",
                color=0xFF0000
            )
            await ctx.send(embed=embed)
            
    #Softban
    @commands.command(aliases = ["lightban"])
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def softban(self, ctx, member : discord.Member = None, *, reason = None):
        if member == None:
            embed = discord.Embed(
                title = "Softban Error",
                description = "Please specify a user!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
        else:
            if member.id == ctx.message.author.id:
                embed = discord.Embed(
                    title = "Softban Error",
                    description = "You can't softban yourself!",
                    color = self.blurple
                )
                await ctx.send(embed = embed)
            else:
                if reason == None:
                    await member.ban(reason = f"Softban by {ctx.message.author.name}#{ctx.message.author.discriminator}.\nReason - No Reason Provided.")
                    await member.unban()
                    embed = discord.Embed(
                        title = "Softban",
                        description = f"{member.mention} has been softbanned by {ctx.message.author.mention}",
                        color = self.blurple
                    )
                    await ctx.send(embed = embed)
                    modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
                    if modlog == None:
                        return
                    if modlog != None:
                        embed = discord.Embed(
                            title = "Softban",
                            description = f"{member.mention} has been softbanned by {ctx.message.author.mention}.",
                            color = self.blurple
                        )
                        await modlog.send(embed = embed)
                else:
                    await member.ban(reason = f"Softban by {ctx.message.author.name}#{ctx.message.author.discriminator}.\nReason - {reason}.")
                    await member.unban()
                    embed = discord.Embed(
                        title = "Softban",
                        description = f"{member.mention} has been softbanned by {ctx.message.author.mention} for {reason}",
                        color = self.blurple
                    )
                    await ctx.send(embed = embed)
                    modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
                    if modlog == None:
                        return
                    if modlog != None:
                        embed = discord.Embed(
                            title = "Softban",
                            description = f"{member.mention} has been softbanned by {ctx.message.author.mention} for {reason}.",
                            color = self.blurple
                        )
                        await modlog.send(embed = embed)

    @softban.error
    async def softban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions!",
                description = "You are missing the **Administrator** permission level!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)

    #Nuke
    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def nuke(self, ctx):
        channel_position = ctx.channel.position
        new_channel = await ctx.channel.clone()
        await new_channel.edit(reason = f"Nuke by {ctx.message.author.name}#{ctx.message.author.discriminator}", position = channel_position)
        await ctx.channel.delete()
        embed = discord.Embed(
            title = "Nuke",
            description  = "This channel has been nuked!",
            color = self.blurple
        )
        embed.set_image(url = "https://cdn.discordapp.com/attachments/600843048724987925/600843407228928011/tenor.gif")
        await new_channel.send(embed = embed, delete_after = 30.0)
        modlog = discord.utils.get(ctx.guild.text_channels, name = "mod·logs")
        if modlog == None:
            pass
        if modlog != None:
            embed = discord.Embed(
                title = "Nuke",
                description = f"{ctx.message.author.mention} has nuked {new_channel.mention}.",
                color = self.blurple
            )
            await modlog.send(embed = embed)

    @nuke.error
    async def nuke_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions!",
                description = "You are missing the **Moderator** permission level!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Moderation(bot))
