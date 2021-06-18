import discord
from discord.ext import commands
from datetime import date, datetime


class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
        day = datetime.today().isoweekday()
        genshinday = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
        }
        
        genshindrops = {
            0: "https://cdn.discordapp.com/attachments/815386324658814976/820723149413941369/Sunday.png",
            1: "https://cdn.discordapp.com/attachments/815386324658814976/854084085357871104/Monday.png",
            2: "https://cdn.discordapp.com/attachments/815386324658814976/846913736601894912/Tuesday.png",
            3: "https://cdn.discordapp.com/attachments/815386324658814976/847369307071316029/Wednesday.png",
            4: "https://cdn.discordapp.com/attachments/815386324658814976/852729859125018654/Thursday.png",
            5: "https://cdn.discordapp.com/attachments/815386324658814976/847671599669706762/Friday.png",
            6: "https://cdn.discordapp.com/attachments/815386324658814976/852729859125018654/Thursday.png",            
        }

        embed = discord.Embed(
            title=f"Today's Dailies ({genshinday[day]})", colour=discord.Colour(0xEABCBB)
        )
        embed.set_image(
            url=f"{genshindrops[day]}"
        )
        embed.set_footer(
            text="Dailies reset at 4AM. Check #server·status for a countdown."
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Daily(bot))
