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
def talent_traveler(element):
    #setting default values to anemo traveler
    book1 = "Freedom"
    book2 = "Resistance"
    book3 = "Ballad"
    Common1 = "Divining Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    name = "Anemo Traveler"
    boss = "Dvalin's Sigh"
    color = discord.Colour.green()
    description = "Talent materials for Traveler's Normal/charged attack and Anemo Traveler's Elemental skill and Elemental Burst."
    #creathing this function allows for easily adding in information and code when Traveler unlocks more elements
    if(element == 'geo'):
        name = "Geo Traveler"
        Common1 = "Firm Arrowhead"
        Common2 = "Sharp Arrowhead"
        Common3 = "Weathered Arrowhead"
        book1 = "Prosperity"
        book2 = "Dilligence"
        book3 = "Gold"
        boss = "Tail of Boreas"
        description ="Talent materials for Geo Traveler's Element skill and Elemental Burst. Refer to anemo traveler for Normal/charged attack."
        color = discord.Colour.gold()

    embed = discord.Embed(title= f"{name} Talent Materials",colour = color,description = description)
    embed.set_thumbnail(url = "https://static.wikia.nocookie.net/gensin-impact/images/c/cb/Character_Traveler_Introduction.png")
    embed.add_field(name = "Talent level 2",value = f'6x {Common1}, 3x Teachings of "{book1}", 12,500 Mora',inline = False)
    embed.add_field(name = "Talent level 3",value = f'3x {Common2}, 2x Guide to "{book2}", 17,500 Mora',inline = False)
    embed.add_field(name = "Talent level 4",value = f'4x {Common2}, 4x Guide to "{book3}", 25,000 Mora',inline = False)
    embed.add_field(name = "Talent level 5",value = f'6x {Common2}, 6x Guide to "{book1}", 30,000 Mora',inline = False)
    embed.add_field(name = "Talent level 6",value = f'9x {Common2}, 9x Guide to "{book2}", 37,500 Mora',inline = False)
    embed.add_field(name = "Talent level 7",value = f'4x {Common3}, 4x Philosophies of "{book3}", 1x {boss}, 120,000 Mora',inline = False)
    embed.add_field(name = "Talent level 8",value = f'6x {Common3}, 6x Philosophies of "{book1}", 1x {boss}, 260,000 Mora',inline = False)
    embed.add_field(name = "Talent level 9",value = f'9x {Common3}, 12x Philosophies of "{book2}", 2x {boss}, 450,000 Mora',inline = False)
    embed.add_field(name = "Talent level 10",value = f'12x {Common3}, 16x Philosophies of "{book3}", 2x {boss}, 1x Crown of Insight, 700,000 Mora',inline = False)          
    return embed
@commands.command(name='qiqi',help ="Displays ascension materials for Qiqi. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
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

@commands.command(name ='albedo',help ="Displays ascension materials for Albedo. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def albedo(ctx, flags: str=None):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Cecilia"
    Common1 = "Divining Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/f/f8/Character_Albedo_Card.png"
    name = "Albedo"
    book = "Ballad"
    weekly_boss = "Tusk of Monoceros Caeli"
    color = discord.Colour.gold()
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name ='amber',help = "Displays ascension materials for Amber. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def amber(ctx, flags: str=None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Small Lamp Grass"
    Common1 = "Firm Arrowhead"
    Common2 = "Sharp Arrowhead"
    Common3 = "Weathered Arrowhead"
    name = "Amber"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/2/26/Character_Amber_Card.jpg"
    weekly_boss = "Dvalin's Sigh"
    book = "Freedom"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name ='barbara',help = "Displays ascension materials for Barbara. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def barbara(ctx, flags: str = None):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Philanemo Mushroom"
    Common1 = "Divining Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    name = "Barbara"
    color = discord.Colour.blue()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/9/93/Character_Barbara_Card.jpg"
    weekly_boss = "Ring of Boreas"
    book = "Freedom"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'beidou',help ="Displays ascension materials for Beidou. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def beidou(ctx, flags: str= None):
    gem = "Varjada Amethust"
    boss = "Lightning Prism"
    Local ="Noctilucous Jade"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Insignia"
    Common3 = "Golden Raven Insignia"
    name = "Beidou"
    color = discord.Colour.purple()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/8/84/Character_Beidou_Card.jpg"
    weekly_boss = "Dvalin's Sigh"
    book = "Gold"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)

@commands.command(name ='bennett',help = "Displays ascension materials for Bennett. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def bennett(ctx, flags: str=None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Windwheel Aster"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Insignia"
    Common3 = "Golden Raven Insignia"
    name = "Bennett"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/7/7f/Character_Bennett_Card.jpg"
    weekly_boss = "Dvalin's Plume"
    book = "Resistance"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'chongyun',aliases = ['chong'],help ="Displays ascension materials for chongyun. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def chong(ctx, flags:str = None):
    gem = "Shivada Jade"
    boss = "Hoarfrost Core"
    Local ="Cor Lapis"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    name = "Chongyun"
    color = discord.Colour.teal()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/f/fa/Character_Chongyun_Card.jpg"
    weekly_boss = "Dvalin's Sigh"
    book = "Dilligence"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name ='diluc',help = "Displays ascension materials for Diluc. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def diluc(ctx,flags: str = None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Small Lamp Grass"
    Common1 = "Recruit's Insignia"
    Common2 = "Seargent's Insignia"
    Common3 = "Lieutenant's Insignia"
    name = "Diluc"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/45/Character_Diluc_Card.jpg"
    weekly_boss = "Dvalin's Plume"
    book = "Resistance"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name ='diona',help = "Displays ascension materials for Diona. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def diona(ctx,  flags: str = None):
    gem = "Shivada Jade"
    boss = "Hoarfrost Core"
    Local ="Calla Lily"
    Common1 = "Firm Arrowhead"
    Common2 = "Sharp Arrowhead"
    Common3 = "Weathered Arrowhead"
    name = "Diona"
    color = discord.Colour.teal()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/0/08/Character_Diona_Card.png"
    weekly_boss = "Shard of a Foul Legacy"
    book = "Freedom"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name ='fischl', aliases =['oz','amy'],help = "Displays ascension materials for Fischl. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def fischl(ctx, flags: str = None):
    gem = "Varjada Amethyst"
    boss = "Lightning Prism"
    Local ="Small Lamp Grass"
    Common1 = "Firm Arrowhead"
    Common2 = "Sharp Arrowhead"
    Common3 = "Weathered Arrowhead"
    name = "Fischl"
    color = discord.Colour.purple()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/48/Character_Fischl_Card.jpg"
    weekly_boss = "Spirit Locket of Boreas"
    book = "Ballad"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name ='Ganyu', aliases =['cocogoat'],help = "Displays ascension materials for Ganyu. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def fischl(ctx, flags: str = None):
    gem = "Shivada Jade"
    boss = "Hoarfrost Core"
    Local ="Qingxin"
    Common1 = "Whopperflower Nectar"
    Common2 = "Shimmering Nectar"
    Common3 = "Energy Nectar"
    name = "Ganyu"
    color = discord.Colour.teal()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/8/8d/Character_Ganyu_Card.png"
    weekly_boss = "Shadow of the Warrior"
    book = "Dilligence"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name ='jean',help = "Displays ascension materials for Jean. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def Jean(ctx, flags: str = None):
    gem = "Vayuda Turquoise"
    boss = "Hurrican Seed"
    Local ="Dandelion Seed"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    name = "Jean"
    color = discord.Colour.green()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/0/0e/Character_Jean_Card.jpg"
    weekly_boss = "Dvalin's Plume"
    book = "Resistance"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name ='kaeya',help = "Displays ascension materials for Kaeya. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def kaeya(ctx, flags: str = None):
    gem = "Shivada Jade"
    boss = "Hoarfrost Core"
    Local ="Calla Lily"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Isnigia"
    Common3 = "Golden Raven Insignia"
    name = "Kaeya"
    color = discord.Colour.teal()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/6/64/Character_Kaeya_Card.jpg"
    weekly_boss = "Spirit Locket of Boreas"
    book = "Ballad"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name ='keqing',help = "Displays ascension materials for Keqing. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def keqing(ctx, flags: str = None):
    gem = "Vayuda Turquoise"
    boss = "Lightning Prism"
    Local ="Cor Lapis"
    Common1 = "Whopperflower Nectar"
    Common2 = "Shimmering Nectar"
    Common3 = "Energy Nectar"
    name = "Keqing"
    color = discord.Colour.dark_purple()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/f/f4/Character_Keqing_Card.jpg"
    weekly_boss = "Ring of Boreas"
    book = "Prosperity"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'klee',help = "Displays ascension materials for Klee. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def klee(ctx, flags: str = None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Philanemo Mushroom"
    Common1 = "Diving Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    name = "Klee"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/7/78/Character_Klee_Card.jpg"
    weekly_boss = "Ring of Boreas"
    book = "Freedom"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'lisa',help = "Displays ascension materials for lisa. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def lisa(ctx, flags: str = None):
    gem = "Vajrada Amethyst"
    boss = "Lightning Prism"
    Local ="Valberry"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    name = "Lisa"
    color = discord.Colour.dark_purple()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/d/dc/Character_Lisa_Card.jpg"
    weekly_boss = "Dvalin's Claw"
    book = "Ballad"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'mona',help = "Displays ascension materials for Mona. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def mona(ctx, flags: str = None):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Philanemo Mushroom"
    Common1 = "Whopperflower Nectar"
    Common2 = "Shimmering Nectar"
    Common3 = "Energy Nectar"
    name = "Mona"
    color = discord.Colour.blue()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/6/69/Character_Mona_Card.jpg"
    weekly_boss = "Ring of Boreas"
    book = "Resistance"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'ningguang', aliases =['ning'],help = "Displays asecnsion materials for Ningguang. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def ningguang(ctx, flags: str = None):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Gaze Lily"
    Common1 = "Recruit's Insignia"
    Common2 = "Seargent's Insignia"
    Common3 = "Lieutenant's Insignia"
    name = "Ningguang"
    color = discord.Colour.gold()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/3/3e/Character_Ningguang_Card.jpg"
    weekly_boss = "Spirit Locket of Boreas"
    book = "Prosperity"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'noelle', aliases =['noel'],help = "Displays asecnsion materials for Noelle. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def noelle(ctx, flags: str = None):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Valberry"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    name = "Noelle"
    color = discord.Colour.gold()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/9/92/Character_Noelle_Card.jpg"
    weekly_boss = "Dvalin's Claw"
    book = "Resistance"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'razor', aliases =['wolf'],help = "Displays asecnsion materials for Razor. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def razor(ctx, flags: str = None):
    gem = "Vajrada Amethyst"
    boss = "Lightning Prism"
    Local ="Wolfhook"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    name = "Razor"
    color = discord.Colour.purple()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/6/68/Character_Razor_Card.jpg"
    weekly_boss = "Dvalin's Claw"
    book = "Resistance"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'sucrose',help = "Displays ascension materials for Sucrose. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def sucrose(ctx, flags: str = None):
    gem = "Vayuda Turquoise"
    boss = "Hurricane Seed"
    Local ="Windwheel Aster"
    Common1 = "Whopperflower Nectar"
    Common2 = "Shimmering Nectar"
    Common3 = "Energy Nectar"
    name = "Sucrose"
    color = discord.Colour.green()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/2/22/Character_Sucrose_Card.jpg"
    weekly_boss = "Spirit Locket of Boreas"
    book = "Freedom"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'tartaglia', aliases =['childe','ajax'],help = "Displays asecnsion materials for Tartaglia. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def childe(ctx, flags: str = None):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Starconch"
    Common1 = "Recruit's Insignia"
    Common2 = "Sergeant's Insignia"
    Common3 = "Lieutenatn's Insignia"
    name = "Tartaglia"
    color = discord.Colour.blue()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/4c/Character_Tartaglia_Card.png"
    weekly_boss = "Shard of a Foul Legacy"
    book = "Freedom"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
#Traveler is a nasty case for talents. Based on which element he's resonated with, it changes the materials needed.
#Traveler also doesn't have a local boss material so.... can't use ascension() and talent() on them
#The specific helper function talent_traveler() is desinged so that when the traveler unlocks more elements, they can be quickly integrated into the code
@commands.command(name = 'traveler', aliases =['mc','Aether','Lumine'],help = "Displays ascension materials for the Traveler. Replace [flags] with 'talentgeo' to see talent materials for Geo Traveler instead or 'talentanemo' to see talent materials for Anemo Traveler.")
async def traveler(ctx,  flags: str = None):
    
    gem = "Brilliant Diamond"
    Local ="Windwheel Aster"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talentgeo'):
            embed = talent_traveler("geo")
            await ctx.send(embed=embed)
        if(lowercase == 'talentanemo'):
            embed = talent_traveler("anemo")
            await ctx.send(embed=embed)   
    else:
        embed_asc = discord.Embed(title="Traveler",colour = discord.Colour.dark_gold())
        embed_asc.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/c/cb/Character_Traveler_Introduction.png") 
        embed_asc.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
        embed_asc.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
        embed_asc.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
        embed_asc.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
        embed_asc.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
        embed_asc.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)
        await ctx.send(embed=embed_asc)
@commands.command(name = 'venti',aliases = ['barabatos'],help = "Displays ascension materials for Venti. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def venti(ctx,  flags: str = None):
    gem = "Vayuda Turquoise"
    boss = "Hurricane Seed"
    Local ="Cecilia"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    name = "Venti"
    color = discord.Colour.green()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/7/76/Character_Venti_Card.jpg"
    weekly_boss = "Tail of Boreas"
    book = "Ballad"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'xiangling', aliases = ['gouba'],help ="Displays ascension materials for Xiangling. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def gouba(ctx,  flags: str = None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Jueyun Chili"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    name = "Xiangling"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/f/f1/Character_Xiangling_Card.jpg"
    weekly_boss = "Dvalin's Claw"
    book = "Dilligence"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
#Not completed because Xiao did not get released yet. Will update this in the coming days as 1.3 release is really soon
@commands.command(name ='Xiao', aliases =['Alatus'],help = "Displays ascension materials for Xiao")
async def fischl(ctx, flags: str = None):
    gem = "Vayuda Turquoise"
    boss = "Hurricane Seed"
    Local ="Qingxin"
    Common1 = "Firm Arrowhead"
    Common2 = "Sharp Arrowhead"
    Common3 = "Weathered Arrowhead"
    name = "Xiao"
    color = discord.Colour.green()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/8/88/Character_Xiao_Card.jpg"
    #weekly_boss = "Shadow of the Warrior" To update upon Xiao release
    #book = "Dilligence"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            #embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink) uncomment once he's released
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            #embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            #await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'xingqiu',help = "Displays ascension materials for Xingqiu. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def xingiqu(ctx,  flags: str = None):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Silk Flower"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    name = "Xingqiu"
    color = discord.Colour.blue()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/c/c2/Character_Xingqiu_Card.jpg"
    weekly_boss = "Tail of Boreas"
    book = "Gold"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'xinyan',help = "Displays ascension materials for Xinyan. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def xingyan(ctx, flags: str = None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Violetgrass"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Isnigia"
    Common3 = "Golden Raven Insignia"
    name = "Xinyan"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/4c/Character_Xinyan_Card.jpeg"
    weekly_boss = "Tusk of Monoceros Caeli"
    book = "Gold"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@commands.command(name = 'zhongli',aliases = ['rex lapis','morax'], help = "Displays ascension materials for Zhongli. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def zhongli(ctx, flags: str = None):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Cor Lapis"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    name = "Zhongli"
    color = discord.Colour.gold()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/7/79/Character_Zhongli_Card.png"
    weekly_boss = "Tusk of Monoceros Caeli"
    book = "Gold"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
#End of characters
#in the case of weapons, the material amount depends on the rarity of the weapon. The weapon acsension specific material (the one obtainalbe from domains)
#Could possibly expand as new regions are included and don't follow a similar naming pattern for characters. Will require its own helper funciton.
def get_weapon_asc(name):
    #returns ascension material names in the form of a list
    #since this is a helper function and I'm manually putting in the parameter, I don't have to worry about name being mispelt or lowercase
    if(name == "decarabian"):
       return ["Tile of Decarabian's Tower","Debris of Decarabian's City","Fragment of Decarabian's Epic","Scattered Piece of Decarabian's Dream"]
    elif(name == "boreal"):
        return ["Boreal Wolf's Milk Tooth","Boreal Wolf's Cracked Tooth","Boreal Wolf's Broken Fang","Boreal Wolf's Nostalgia"]
    elif(name == "dandelion" or name == "gladiator"):
        return ["Fetters of the Dandelion Gladiator","Chains of the Dandelion Gladiator","Shackles of the Dandelion Gladiator","Dream of the Dandelion Gladiator"]
    elif(name == "gunyun"):
        return ["Luminous Sands from Guyun","Lustrous Stone from Guyun","Relic from Guyun","Divine Body from Guyun"]
    elif(name == "mist" or name == "veiled"):
        return ["Mist Veiled Lead Elixir","Mist Veiled Mercury Elixir","Mist Veiled Gold Elixir","Mist Veiled Primo Elixir"]
    elif(name == "aerosiderite"):
        return ["Grain of Aerosiderite","Piece of Aerosiderite","Bit of Aerosiderite","Chunk of Aerosiderite"]
    else: 
        #Decrarbian by default
        return ["Tile of Decarabian's Tower","Debris of Decarabian's City","Fragment of Decarabian's Epic","Scattered Piece of Decarabian's Dream"]

def get_weapon_onestar(ascension,name,common1,common2,common4,common5,imagelink):
    ascensionlist = get_weapon_asc(ascension)
    embed = discord.Embed(title= f"{name} Ascension Materials",colour = discord.Colour.light_grey(),description = "Weapon Effect: None")
    embed.set_thumbnail(url =imagelink)
    embed.add_field(name ="Ascesnion 1",value =f"1x {ascensionlist[0]}, 1x {common1}, 1x {common4}, 0 mora", inline =False)
    embed.add_field(name ="Ascesnion 2",value =f"1x {ascensionlist[1]}, 4x {common1}, 2x {common4}, 5,000 mora", inline =False)
    embed.add_field(name ="Ascesnion 3",value =f"2x {ascensionlist[1]}, 2x {common2}, 2x {common5}, 5,000 mora", inline =False)
    embed.add_field(name ="Ascesnion 4",value =f"1x {ascensionlist[2]}, 4x {common2}, 3x {common5}, 10,000 mora", inline =False)
    return embed

def get_weapon_twostar(ascension,name,common1,common2,common4,common5,imagelink):
    ascensionlist = get_weapon_asc(ascension)
    embed = discord.Embed(title= f"{name} Ascension Materials",colour = discord.Colour.green(),description = "Weapon Effect: None")
    embed.set_thumbnail(url =imagelink)
    embed.add_field(name ="Ascesnion 1",value =f"1x {ascensionlist[0]}, 1x {common1}, 1x {common4}, 5,000 mora", inline =False)
    embed.add_field(name ="Ascesnion 2",value =f"1x {ascensionlist[1]}, 5x {common1}, 4x {common4}, 5,000 mora", inline =False)
    embed.add_field(name ="Ascesnion 3",value =f"3x {ascensionlist[1]}, 3x {common2}, 3x {common5}, 10,000 mora", inline =False)
    embed.add_field(name ="Ascesnion 4",value =f"1x {ascensionlist[2]}, 5x {common2}, 4x {common5}, 15,000 mora", inline =False)
    return embed

def get_weapon_threestar(ascension,name,common1,common2,common3,common4,common5,common6,imagelink,weapon_effect):
    ascensionlist = get_weapon_asc(ascension)
    embed = discord.Embed(title= f"{name} Ascension Materials",colour = discord.Colour.teal(),description = f"Weapon Effect: {weapon_effect}")
    embed.set_thumbnail(url =imagelink)
    embed.add_field(name ="Ascesnion 1",value =f"2x {ascensionlist[0]}, 2x {common1}, 1x {common4}, 5,000 mora", inline =False)
    embed.add_field(name ="Ascesnion 2",value =f"2x {ascensionlist[1]}, 8x {common1}, 5x {common4}, 10,000 mora", inline =False)
    embed.add_field(name ="Ascesnion 3",value =f"4x {ascensionlist[1]}, 4x {common2}, 4x {common5}, 15,000 mora", inline =False)
    embed.add_field(name ="Ascesnion 4",value =f"2x {ascensionlist[2]}, 8x {common2}, 6x {common5}, 20,000 mora", inline =False)
    embed.add_field(name ="Ascesnion 5",value =f"4x {ascensionlist[2]}, 6x {common3}, 4x {common6}, 25,000 mora", inline =False)
    embed.add_field(name ="Ascesnion 6",value =f"3x {ascensionlist[3]}, 12x {common3}, 8x {common6}, 30,000 mora", inline =False)
    return embed
#design decision: make the command one word instead of oneword and an argument e.g "dullblade" vs "dull blade"
#if I wanted the user to input "!genshin dull blade" I'd have to do something like "@bot.command(name = "dull")" with an argument
#async def dull_blade(ctx, arg:str) and check that arg == "blade". This can work for even the skyward weapon series but, I've decided
#to keep it one word so that I can declare easily that punctuation is not included e.g Wolf's Gravestone becomes wolfsgravestone
#to begin with, the first set of weapons are swords
@commands.command(name = "dullblade", aliases =["1starsword"], help ="Displays weapon ascension materials for the weapon 'Dull Blade'")
async def dull_blade(ctx):
    common1 = "Heavy Horn"
    common2 = "Black Bronze Horn"
    common4 = "Firm Arrowhead"
    common5 = "Sharp Arrowhead"
    name = "Dull Blade"
    ascension = "decarabian"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/9/90/Weapon_Dull_Blade_3D.png"
    embed = get_weapon_onestar(ascension,name,common1,common2,common4,common5,imagelink)
    await ctx.send(embed=embed)
@commands.command(name = "silversword", help ="Displays weapon ascension materials for the weapon 'Silver Sword'")
async def silver_blade(ctx):
    common1 = "Heavy Horn"
    common2 = "Black Bronze Horn"
    common4 = "Firm Arrowhead"
    common5 = "Sharp Arrowhead"
    name = "Dull Blade"
    ascension = "decarabian"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/40/Weapon_Silver_Sword_3D.png"
    embed = get_weapon_twostar(ascension,name,common1,common2,common4,common5,imagelink)
    await ctx.send(embed=embed)
@commands.command(name = "filletblade", aliases = ["fillet"], help = "Displays weapon ascension materials for the weapon 'Fillet Blade'")
async def fillet_blade(ctx):
    common1 = "Mist Grass Pollen"
    common2 = "Mist Grass"
    common3 = "Mist Grass Wick"
    common4 = "Treasure Hoarder Insignia"
    common5 = "Silver Raven Insignia"
    common6 = "Golden Raven Insignia"
    name = "Fillet Blade"
    ascension = "mist"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/c/cc/Weapon_Fillet_Blade_3D.png"
    weapon_effect = "On hit, has 50% chance to deal 240~400% ATK DMG to a single enemy. Can only occur once every 15~11s." 
    #this string goes against python rules with %, but it looks fine on discord. vscode highlights the '% C' of the string
    embed = get_weapon_threestar(ascension,name,common1,common2,common3,common4,common5,common6,imagelink,weapon_effect)
    await ctx.send(embed=embed)
@commands.command(name = "skyridersword", aliases = ["skyrider"], help = "Displays weapon ascension materials for the weapon 'Skyrider Sword'")
async def skyrider_blade(ctx):
    common1 = "Fragile Bone Shard"
    common2 = "Sturdy Bone Shard"
    common3 = "Fossilized Bone Shard"
    common4 = "Recruit's Insignia"
    common5 = "Sergeant's Insignia"
    common6 = "Lieutenant's Insignia"
    name = "Skyrider Sword"
    ascension = "aerosiderite"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/45/Weapon_Skyrider_Sword_3D.png"
    weapon_effect = "Using an Elemental Burst grants a 12~24% increase in ATK and Movement SPD for 15s." 
    embed = get_weapon_threestar(ascension,name,common1,common2,common3,common4,common5,common6,imagelink,weapon_effect)
    await ctx.send(embed=embed)
@commands.command(name = "harbigerofdawn", aliases = ["harbinger"], help = "Displays weapon ascension materials for the weapon 'Harbinger of Dawn'")
async def harbinger_blade(ctx):
    common1 = "Dead Ley Line Branch"
    common2 = "Dead Ley Line Leaves"
    common3 = "Ley Line Sprouts"
    common4 = "Slime Condensate"
    common5 = "Slime Secretions"
    common6 = "Slime Concentrate"
    name = "Harbinger of Dawn"
    ascension = "boreal"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/2/23/Weapon_Harbinger_of_Dawn_3D.png"
    weapon_effect = "When HP is above 90%, increases CRIT Rate by 14~28%." 
    embed = get_weapon_threestar(ascension,name,common1,common2,common3,common4,common5,common6,imagelink,weapon_effect)
    await ctx.send(embed=embed)
@commands.command(name = "travelershandysword", aliases = ["handysword","travelerhandysword"], help = "Displays weapon ascension materials for the weapon 'Traveler's Handy Sword'")
async def traveler_blade(ctx):
    common1 = "Chaos Device"
    common2 = "Chaos Circuit"
    common3 = "Chaos Core"
    common4 = "Divining Scroll"
    common5 = "Sealed Scroll"
    common6 = "Forbidden Curse Scroll"
    name = "Traveler's Handy Sword"
    ascension = "dandelion"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/b/bb/Weapon_Traveler%27s_Handy_Sword_3D.png"
    weapon_effect = "Each Elemental Orb or Particle collected restores 1~2% HP." 
    embed = get_weapon_threestar(ascension,name,common1,common2,common3,common4,common5,common6,imagelink,weapon_effect)
    await ctx.send(embed=embed)
@commands.command(name = "darkironsowrd", aliases = ["darkiron"], help = "Displays weapon ascension materials for the weapon 'Dark Iron sword")
async def iron_blade(ctx):
    common1 = "Hunter's Sacrificial Knife"
    common2 = "Agent's Sacrificial Knife"
    common3 = "Inspector's Sacrificial Knife"
    common4 = "Damaged Mask"
    common5 = "Stained Mask"
    common6 = "Ominous Mask"
    name = "Dark Iron Sword"
    ascension = "guyun"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/44/Weapon_Dark_Iron_Sword_3D.png"
    weapon_effect = "Upon causing an Overloaded, Superconduct, Electro-Charged, or an Electro-infused Swirl reaction, ATK is increased by 20~40% for 12s." 
    embed = get_weapon_threestar(ascension,name,common1,common2,common3,common4,common5,common6,imagelink,weapon_effect)
    await ctx.send(embed=embed)
@commands.command(name = "coolsteel",help = "Displays weapon ascension materials for the weapon 'Cool Steel")
async def cold_blade(ctx):
    common1 = "Heavy Horn"
    common2 = "Black Bronze Horn"
    common3 = "Black Crystal Horn"
    common4 = "Firm Arrowhead"
    common5 = "Sharp Arrowhead"
    common6 = "Weathered Arrowhead"
    name = "Cool Steel"
    ascension = "decarabian"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/40/Weapon_Cool_Steel_3D.png"
    weapon_effect = "Increases DMG against opponents affected by Hydro or Cryo by 12~24%." 
    embed = get_weapon_threestar(ascension,name,common1,common2,common3,common4,common5,common6,imagelink,weapon_effect)
    await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Genshin(bot))
