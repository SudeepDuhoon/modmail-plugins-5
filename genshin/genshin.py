import os
import discord
from discord.ext import commands

class Genshin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#images of the characters were taken from the genshin wiki site: https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki
#Will try to keep the list of commands in the following order except for qiqi because she was the first one I wrote:
#Characters (alphabetical), Daily Talent/Weapons materials, Weapons (by type of weapon)

    def ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink):
    embed = discord.Embed(title= f"{name} Ascension Materials",colour = color)
    embed.set_thumbnail(url =imagelink) 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)
    return embed

    def talent(name,book,boss,Common1,Common2,Common3,color,imagelink):
    embed = discord.Embed(title= f"{name} Talent Materials",colour = color)
    embed.set_thumbnail(url = imagelink)
    embed.add_field(name = "Talent level 2",value = f'6x {Common1}, 3x Teachings of "{book}", 12,500 Mora',inline = False)
    embed.add_field(name = "Talent level 3",value = f'3x {Common2}, 2x Guide to "{book}", 17,500 Mora',inline = False)
    embed.add_field(name = "Talent level 4",value = f'4x {Common2}, 4x Guide to "{book}", 25,000 Mora',inline = False)
    embed.add_field(name = "Talent level 5",value = f'6x {Common2}, 6x Guide to "{book}", 30,000 Mora',inline = False)
    embed.add_field(name = "Talent level 6",value = f'9x {Common2}, 9x Guide to "{book}", 37,500 Mora',inline = False)
    embed.add_field(name = "Talent level 7",value = f'4x {Common3}, 4x Philosophies of "{book}", 1x {boss}, 120,000 Mora',inline = False)
    embed.add_field(name = "Talent level 8",value = f'6x {Common3}, 6x Philosophies of "{book}", 1x {boss}, 260,000 Mora',inline = False)
    embed.add_field(name = "Talent level 9",value = f'9x {Common3}, 12x Philosophies of "{book}", 2x {boss}, 450,000 Mora',inline = False)
    embed.add_field(name = "Talent level 10",value = f'12x {Common3}, 16x Philosophies of "{book}", 2x {boss}, 1x Crown of Insight, 700,000 Mora',inline = False)          
    return embed

@commands.command()
async def qiqi(ctx,flags:str=None):
    Common1 = "Divining Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/b/b9/Character_Qiqi_Card.jpg"
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent("Qiqi","Prosperity","Tail of Boreas",Common1,Common2,Common3,discord.Colour.teal(),imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension("Qiqi","Shivada Jade","Hoarfrost Core","Violetgrass",Common1,Common2,Common3,discord.Colour.teal(),imagelink)
            await ctx.send(embed=embed)
            embed = talent("Qiqi","Prosperity","Tail of Boreas",Common1,Common2,Common3,discord.Colour.teal(),imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension("Qiqi","Shivada Jade","Hoarfrost Core","Violetgrass",Common1,Common2,Common3,discord.Colour.teal(),imagelink)
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Genshin(bot))
