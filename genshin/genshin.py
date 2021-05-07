import discord
import json
import requests
from discord.ext import commands

class Genshin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = self.bot.main_color
        
@commands.command(name="weapon",aliases=["wpn"])
async def _weapon(ctx, *, arg=None): 
    if arg == None:
      def listToString(wl):  
        str1 = "\n" 
        return (str1.join(wl))  
      wplist = requests.get('https://api.genshin.dev/weapons').text
      wl = json.loads(wplist)  
      embed = discord.Embed(title="Weapon List", description=listToString(wl).title().replace("-", " "))
      await ctx.send(embed=embeded)

      ## # Same as artifact, but Weapons hold to many data, so it only shown a part of it
      # for i in wl:
      #   response = requests.get(wp.format(i)).text
      #   data = json.loads(response)
      #   embeded.add_field(name=i.title().replace("-", " "), value="Type: {}".format(data['type']), inline=True)
      # await ctx.send(embed=embeded)

    elif arg != None:
      arg = arg.replace(" ", "-").lower()
      wplist = requests.get('https://api.genshin.dev/weapons').text
      wl = json.loads(wplist)  
      if arg in wl:
        response = requests.get(wp.format(arg)).text
        data = json.loads(response)
        embed = discord.Embed(title=data['name'])
        print(data['name'])
        embed.set_thumbnail(url=imgw.format(data['name'].replace(" ", "_")))
        embed.add_field(name="Type", value=data['type'], inline=True)
        embed.add_field(name="Base ATK", value=data['baseAttack'], inline=True) 
        rrt = int(data['rarity'])
        strg = "".join([" :star: ".format(x, x*2) for x in range(rrt)])
        embed.add_field(name="Rarity", value=strg, inline=True)
        embed.add_field(name="Sub Stat", value=data['subStat'], inline=True)
        embed.add_field(name="Where to Get", value=data['location'], inline=True)
        embed.add_field(name="Passive: {}".format(data['passiveName']), value=data['passiveDesc'], inline=False)
        await ctx.send(embed=embed)
      else:
        await ctx.send("{} not Found!".format(arg).title().replace("-", " "))
       
                
    @commands.command(name="yuri3",aliases=["gaytime3"])
    async def _gaytime(self, ctx):
        """
        Retrieves a random photo of Yae Sakura and Kallen Kaslana.
        """
        embed = discord.Embed(color=15383739, title='GI Bot', description="Currently we only provide Character's Brief Details. Feel free to support us with idea in [Github](https://github.com/rizkidn17/GenshinDiscordBot) or [Website](https://rizkidn17.github.io/GenshinDiscordBot/)")
        embed.set_footer(text='Disclaimer: This bot only for personal use and not related with Official Genshin Impact and Mihoyo')
        await ctx.send(embed=embed)
        
    
def setup(bot):
    bot.add_cog(Genshin(bot))
