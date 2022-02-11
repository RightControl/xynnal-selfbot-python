import discord
from discord.ext import commands
import requests
import random

class NSFW(commands.Cog):

    '''
       Hello, user that is reading this!
       In this class, you will find every fun command from our selfbot.
    '''

    def __init__(self, bot):
        self.bot = bot

    # Tits
    @commands.command()
    async def tits(self,ctx):
        try:
            with requests.session() as ses:
                search = ses.get('http://api.oboobs.ru/boobs/{}'.format(random.randint(0, 10219)))
                result = search.json()
                boob = random.choice(result)
                boob = "http://media.oboobs.ru/{}".format(boob["preview"])
                await ctx.message.delete()
                await ctx.channel.send("{}".format(boob))
        except Exception as err:
            print(f"couldn't get results {err}")
    # Hentai
    @commands.command()
    async def hentai(self,ctx):
        try:
            with requests.session() as ses:
                search = ses.get('https://nekos.life/api/v2/img/Random_hentai_gif')
                result = search.json()
                gif = result["url"]
                await ctx.message.delete()
                await ctx.channel.send("{}".format(gif))
        except Exception as err:
            print(f"{err}")
def setup(bot):
    bot.add_cog(NSFW(bot))
