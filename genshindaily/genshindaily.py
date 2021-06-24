import discord
from discord.ext import commands
from datetime import date, datetime
import pytz


class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx, region: str):
        """
        I'm Gay?
        """
        try:
            # default variables initialization 
            region = region.upper()
            reset_time = 4 
            
            genshinday = {
                0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday",
            }
            
            genshindrops = {
                0: "https://cdn.discordapp.com/attachments/815386324658814976/854084085357871104/Monday.png",
                1: "https://cdn.discordapp.com/attachments/815386324658814976/846913736601894912/Tuesday.png",
                2: "https://cdn.discordapp.com/attachments/815386324658814976/847369307071316029/Wednesday.png",
                3: "https://cdn.discordapp.com/attachments/815386324658814976/854084085357871104/Monday.png",
                4: "https://cdn.discordapp.com/attachments/815386324658814976/846913736601894912/Tuesday.png",
                5: "https://cdn.discordapp.com/attachments/815386324658814976/847369307071316029/Wednesday.png",            
                6: "https://cdn.discordapp.com/attachments/815386324658814976/820723149413941369/Sunday.png",
            }

            region_tz = {
                "NA":'America/Chicago',
                "EU":'Europe/Dublin',
                "ASIA":'Asia/Hong_Kong',
            }
            
            # find the weekday 
            ct = datetime.now(pytz.timezone(region_tz[region]))
            
            day = ct.weekday()

            if ct.hour < reset_time:
                if day == 0:
                    day = 6
                else:
                    day = day - 1

            # embed 
            embed = discord.Embed(
                title=f"Today's Dailies ({genshinday[day]}) for {region}", colour=discord.Colour(0xEABCBB)
            )
            embed.set_image(
                url=f"{genshindrops[day]}"
            )
            embed.set_footer(
                text="Dailies reset at 4AM. Check #server·status for a countdown."
            )
            await ctx.send(embed=embed)

        # doesn't work for no input or wrong region input
        except:
            embed = discord.Embed(
                title=f"Enter !daily <NA/EU/ASIA> \nWithout the angle brackets.\nAll Asian based servers have the same reset time.", colour=discord.Colour(0xEABCBB)
            )
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Daily(bot))
