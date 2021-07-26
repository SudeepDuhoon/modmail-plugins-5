from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
	if message.content.upper().startswith(".BANLIST"):
            ban_list = await client.get_bans(message.server)
            if not ban_list:
                await client.send_message(message.channel, "This server doesn't have anyone banned (yet)")
            else:
                userid = [user.id for user in ban_list]
                name = [user.name for user in ban_list]
                discriminator = [user.discriminator for user in ban_list]
                bot = [user.bot for user in ban_list]

                print(bot)

                newlist = []
                for item in bot:
                    if item:
                        item = "<:bottag:473742770671058964>"
                    else:
                        item = ""
                    newlist.append(item)
                bot = newlist

                print(bot)

                total = list((zip(userid, name, discriminator, bot)))
                print(total)

                # Thanks to happypetsy on stackoverflow for helping me with this!
                pretty_list = set()
                for details in total:
                    data = "•<@{}>{} ({}#{}) ".format(details[0], details[3], details[1], details[2])
                    pretty_list.add(data)

                await client.send_message(message.channel, "**Ban list:** \n{}".format("\n".join(pretty_list)))

def setup(bot):
    bot.add_cog(Hello(bot))
