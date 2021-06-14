from discord.ext import commands
import discord

class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_message(message):
	if message.content == "ur gay":
		await message.channel.send("pies are better than cakes. change my mind.")

def setup(bot):
    bot.add_cog(FAQ(bot))
