import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio


class Mod(commands.Cog):
    '''
       Hello, user that is reading this!
       In this class, you will find our moderation commands.
    '''

    def __init__(self, bot):
        self.bot = bot

    # Kick user
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self,ctx,l:discord.Member,*,reason:str=None):
        await ctx.message.delete()
        if not l:
            await ctx.channel.send('no second arg included')
            await asyncio.sleep(1)
            await ctx.message.delete()
        else:
            if not reason:
                await l.kick(reason=None)
                print(f"{l} has been kicked")
            else:
                await l.kick(reason=reason)
                print(f"{l} has been kicked")

    @kick.error
    async def kick_error(ctx,err):
        if isinstance(err, commands.MissingPermissions):
            print('no perms sorry bro')
    # Ban user
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self,ctx,l:discord.Member,*,reason:str=None):
        await ctx.message.delete()
        if not l:
            await ctx.channel.send('no second arg included')
            await asyncio.sleep(1)
            await ctx.message.delete()
        else:
            if not reason:
                await l.ban(reason=None)
                print(f"{l} has been kicked")
            else:
                await l.kick(reason=reason)
                print(f"{l} has been kicked")
    @ban.error
    async def ban_error(ctx,err):
        if isinstance(err, commands.MissingPermissions):
            print("no perms sorry bro")


def setup(bot):
    bot.add_cog(Mod(bot))