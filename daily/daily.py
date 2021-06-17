from discord.ext import commands
from datetime import date, datetime
import discord


class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @staticmethod
    def natime():
        """Get time left for daily in NA till 4am their time."""
        now = datetime.datetime.now(pytz.timezone("America/Chicago"))
        utc_time_for_tz_loop: datetime.datetime = (
            datetime.datetime.combine(
                now.date() + datetime.timedelta(days=1), datetime.time(hour=4)
            )
            - now.utcoffset()
        )
        delta = utc_time_for_tz_loop - datetime.datetime.utcnow()
        return humanize.time.precisedelta(delta, minimum_unit="minutes", format="%0.f")

    @commands.command()
    async def daily(self, ctx):
        if datetime.today().isoweekday() == 0:
            # it is Sunday
            embed = discord.Embed(
                title="Today's Dailies (Sunday)", colour=discord.Colour(0xEABCBB)
            )
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/815386324658814976/820723149413941369/Sunday.png"
            )
            embed.set_footer(
                text="Dailies reset at 4AM. Check #server·status for a countdown."
            )
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 1:
            # it is Monday
            embed = discord.Embed(
                title="Today's Dailies (Monday)", colour=discord.Colour(0xEABCBB)
            )
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/815386324658814976/854084085357871104/Monday.png"
            )
            embed.set_footer(
                text="Dailies reset at 4AM. Check #server·status for a countdown."
            )
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 2:
            # it is Tuesday
            embed = discord.Embed(
                title="Today's Dailies (Tuesday)", colour=discord.Colour(0xEABCBB)
            )
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/815386324658814976/846913736601894912/Tuesday.png"
            )
            embed.set_footer(
                text="Dailies reset at 4AM. Check #server·status for a countdown."
            )
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 3:
            # it is Wednesday
            embed = discord.Embed(
                title="Today's Dailies (Wednesday)", colour=discord.Colour(0xEABCBB)
            )
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/815386324658814976/847369307071316029/Wednesday.png"
            )
            embed.set_footer(
                text="Dailies reset at 4AM. Check #server·status for a countdown."
            )
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 4:
            # it is Thursday
            embed = discord.Embed(
                title="Today's Dailies (Thursday)", colour=discord.Colour(0xEABCBB)
            )
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/815386324658814976/852729859125018654/Thursday.png"
            )
            embed.set_footer(
                text="Dailies reset at 4AM. Check #server·status for a countdown.",
            )
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 5:
            # it is Friday
            embed = discord.Embed(
                title="Today's Dailies (Friday)", colour=discord.Colour(0xEABCBB)
            )
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/815386324658814976/847671599669706762/Friday.png"
            )
            embed.set_footer(
                text="Dailies reset at 4AM. Check #server·status for a countdown."
            )
            await ctx.send(embed=embed)
        if datetime.today().isoweekday() == 6:
            # it is Saturday
            embed = discord.Embed(
                title="Today's Dailies (Saturday)", colour=discord.Colour(0xEABCBB)
            )
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/815386324658814976/852729859125018654/Thursday.png"
            )
            embed.set_footer(
                text="Dailies reset at 4AM. Check #server·status for a countdown."
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Daily(bot))
