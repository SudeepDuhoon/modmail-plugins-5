import logging
from enum import Enum
from random import randint,choice
import discord
from discord.ext import commands
from core import checks
import box
import json
import string
from core.models import PermissionLevel

Cog = getattr(commands, "Cog", object)

logger = logging.getLogger("Modmail")

class Yuri(Cog):
    """
    Commands that Sage has made for the server.
    """
  
    image = [
        "https://cdn.discordapp.com/attachments/799069920402341893/833069759120801842/maxresdefault-2.png",
        "https://img3.gelbooru.com//samples/01/f6/sample_01f6d4f8538db12cba435f84f5f35bea.jpg",
        "https://cdn.discordapp.com/attachments/799069920402341893/833967051433312306/yae_sakura_kallen_kaslana_yae_sakura_kallen_kaslana_and_yae_kasumi_honkai_and_1_more__8e3f2dc73ee909.png",
        "https://img3.gelbooru.com//samples/ab/fc/sample_abfc6631bf22bb6c50eb253b6199abdf.jpg",
        "https://img3.gelbooru.com//samples/2f/b9/sample_2fb9ad159221fb7171d469e08a607856.jpg",
        "https://img3.gelbooru.com//samples/96/5f/sample_965fb7297114b36af690cb67f3bbc4b1.jpg",
        "https://64.media.tumblr.com/c38c0f2ebb7b887062be31170f41bce3/tumblr_ph9fwsnQYF1qey13zo1_1280.png",
        "https://64.media.tumblr.com/227d5caeb3ab546838cdea43f3e2da1f/tumblr_pks5xn0JSD1tkxb7uo2_r2_1280.png",
        "https://64.media.tumblr.com/5b5cc8c05f94de0c1f440ee76d74bae2/tumblr_pks5xn0JSD1tkxb7uo1_r2_1280.png",
        "https://64.media.tumblr.com/47ef3db2c483cecd2e3f8db32552df02/8d549bf6c4c0b29e-40/s1280x1920/774013fc276e7ff276f9744ef024ceaabdd67244.png",
        "https://64.media.tumblr.com/f692d1c84dcd0438522df65beee25428/8d549bf6c4c0b29e-e1/s1280x1920/966082fd3f043ef5d93ca33163be171a769da452.png",
        "https://cdn.discordapp.com/attachments/799009843452313640/833501542778667038/EdHbNRKXkAAs6nA.jpg",
        "https://64.media.tumblr.com/3454a7fcd5289110d6f049eaeae873ae/1833996a65d53586-0c/s1280x1920/0b3f54cb9cd15acdde68305b495ef37e8c76c48b.jpg",
        "https://64.media.tumblr.com/24240d8213608eb4c540ea2f5eb8c8dd/tumblr_phnk164ob41trpsq8_1280.png",
        "https://64.media.tumblr.com/c4798b8373780457068297c0ec9e2313/392d268c3e6fa066-6e/s1280x1920/9308136aa1c215391c91784f6d2df6e255e370cf.png",
        "https://64.media.tumblr.com/2d2fc05a4d1723f40af7671d8fc83a69/tumblr_per9lkHwj91rwcs8fo6_1280.jpg",
        "https://64.media.tumblr.com/aa2fe7e50f1e3fc150f9adf46174ad14/tumblr_per9lkHwj91rwcs8fo5_1280.jpg",
        "https://64.media.tumblr.com/ad50c9aa4e42e66c0ef61e30b787ed74/ee70362d6603625b-35/s1280x1920/79e0db2e48cd11d5c5a195631173571e8dc63514.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_kallen_kaslana_and_kallen_kaslana_honkai_and_1_more_drawn_by_jiaming_liu__sample-d00bec3dc082f2bc705889df58048f9b.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_kallen_kaslana_and_yae_sakura_honkai_and_1_more_drawn_by_senseofexistenc__sample-83be79afd99977c58e9c3f907d65178f.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_and_kallen_kaslana_honkai_and_1_more_drawn_by_dokun7__sample-cb80d9b720205b45455536be100ad891.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_theresa_apocalypse_seele_vollerei_yae_sakura_and_otto_apocalypse_honkai_and_1_more_drawn_by_tsubasa_tsubasa__sample-38f6f7b6b14d4673e131dab1e662ba42.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_kallen_kaslana_and_yae_sakura_honkai_and_1_more_drawn_by_791_meiyuewudi__sample-ccdc08bc9c6d103c9d249714b931d081.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_and_kallen_kaslana_honkai_and_2_more_drawn_by_shibanme_tekikumo__sample-a521bdadc742caeb1bf8f60315143011.jpg",
        "https://safebooru.org//samples/3024/sample_b820a529526c890d5da3786ff121c8fc30e61e97.jpg?3148813"
    ]
    
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
        #self.db = bot.plugin_db.get_partition(self)
  
    @commands.command(name="yuri",aliases=["gaytime"])
    async def _gaytime(self, ctx):
        """
        Retrieves a random photo of Yae Sakura and Kallen Kaslana.
        """
        embed = discord.Embed(color=15383739)
        embed.set_image(url=choice(self.image))
        await ctx.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Yuri(bot))
