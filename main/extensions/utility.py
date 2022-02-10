import discord
from discord.ext import commands
import pyfiglet
import requests
import json
import os
import base64
import asyncio


class Utilities(commands.Cog):
    '''
       Hello, user that is reading this!
       In this class, you will find some nice commands that could help you.
    '''

    def __init__(self, bot):
        self.bot = bot

    # ASCII Converter
    @commands.command()
    async def ascii(self,ctx,*,l:str=None):
        if not l:
            await ctx.channel.send('no second arg included')
        else:
            r = pyfiglet.figlet_format(l)
            await ctx.message.delete()
            await ctx.channel.send(f"```{r}```")
    # IP Lookup (ipinfo.io)
    @commands.command()
    async def ip(self,ctx,*,l:str=None):
        if not l:
            await ctx.channel.send("i can't lookup an invisible ip uwu")
        else:
            try:
                with requests.session() as ses:
                    resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if'Wrong ip' in resp.text:
                    await ctx.channel.send('invalid ip!')
                else:
                    try:
                        j = resp.json()
                        country = j["country"]
                        city = j["city"]
                        hostname = j["hostname"]
                        region = j["region"]
                        cords = j["loc"]
                        zipcode = j["postal"]
                        await ctx.channel.send(f"IP Lookup\nCountry: {country}\nCity: {city}\nHostname: {hostname}\nRegion: {region}\nCords: {cords}\nZIP Code: {zipcode}")
                    except Exception as err:
                        print(f"{err}")
            except Exception as err:
                print(f"{err}")
    # Set nickname
    @commands.command()
    async def setnickname(self,ctx,*,l:str=None):
        if not l:
            await ctx.channel.send('no second arg')
        elif len(l) < 1:
            await ctx.channel.send("name needs to have at least 1 char!")
        else:
            try:
                await ctx.author.edit(nick=l)
            except Exception as err:
                    print(f"{err}")
    # Discord Invite "Bypass"
    @commands.command()
    async def invite(self,ctx,l:str=None):
        if not l:
            await ctx.channel.send('no second arg')
        else:
            await ctx.message.delete()
            await ctx.channel.send(f"https://canary.discordapp.com/abc/../../abc/../i%6Evite/{l}")
    # BASE64 Encoder
    @commands.command()
    async def encodebase64(self,ctx,*,l:str=None):
        if not l:
            await ctx.channel.send('no second arg')
        else:
            await ctx.message.delete()
            encodedbytes = base64.b64encode(l.encode("utf-8"))
            await ctx.channel.send(str(encodedbytes, "utf-8"))
    # Junk Generator
    @commands.command()
    async def junk(self,ctx):
        j = "⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔⌔"
        await ctx.channel.send(j)
        await asyncio.sleep(1)
        await ctx.channel.send(j)
    # LMGTFY
    @commands.command()
    async def lmgtfy(self,ctx,*,l:str=None):
        if not l:
            await ctx.channel.send("you must specify a link!")
        else:
            await ctx.channel.send("https://lmgtfy.com/?q={}".format(l.replace(" ", "+")))
    # Rage Quit (Leaves current server)
    @commands.command()
    async def ragequit(self,ctx,*,l):
        ctx.message.delete()
        guild = discord.utils.get(self.bot.guilds, name=l)
        if not guild:
            print('no guild found with that name')
        else:
            await guild.leave()

def setup(bot):
    bot.add_cog(Utilities(bot))
