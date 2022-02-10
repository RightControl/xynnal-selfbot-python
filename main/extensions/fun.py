import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

    '''
       Hello, user that is reading this!
       In this class, you will find every fun command from our selfbot.
    '''

    def __init__(self, bot):
        self.bot = bot

    # Lenny Face
    @commands.command()
    async def lenny(self,ctx):
        await ctx.message.delete()
        await ctx.channel.send(' ͡° ͜ʖ ͡°')
    # Sun Tzu
    @commands.command()
    async def suntzu(self,ctx):
        quotes = ["If you know the enemy and know yourself, you need not fear the result of a hundred battles. If you know yourself but not the enemy, for every victory gained you will also suffer a defeat. If you know neither the enemy nor yourself, you will succumb in every battle.", "The supreme art of war is to subdue the enemy without fighting.", "Appear weak when you are strong, and strong when you are weak.", "Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt.", "Supreme excellence consists of breaking the enemy's resistance without fighting.", "All warfare is based on deception. Hence, when we are able to attack, we must seem unable; when using our forces, we must appear inactive; when we are near, we must make the enemy believe we are far away; when far away, we must make him believe we are near.", "In the midst of chaos, there is also opportunity", "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win", "If your enemy is secure at all points, be prepared for him. If he is in superior strength, evade him. If your opponent is temperamental, seek to irritate him. Pretend to be weak, that he may grow arrogant. If he is taking his ease, give him no rest. If his forces are united, separate them. If sovereign and subject are in accord, put division between them. Attack him where he is unprepared, appear where you are not expected.", "The greatest victory is that which requires no battle.", "To know your Enemy, you must become your Enemy.", "Engage people with what they expect; it is what they are able to discern and confirms their projections. It settles them into predictable patterns of response, occupying their minds while you wait for the extraordinary moment — that which they cannot anticipate.", "There is no instance of a nation benefitting from prolonged warfare.", "Treat your men as you would your own beloved sons. And they will follow you into the deepest valley."]
        randomQuote = random.choice(quotes)
        await ctx.message.delete()
        await ctx.channel.send(randomQuote)
    # 8ball
    @commands.command()
    async def ask8ball(ctx,*,l:str=None):
        if not l:
            await ctx.channel.send('no question provided')
        else:
            answers = ["Yeah", "Nope", "Def not", "Doubt it", "I agree", "Surely", "Def", "Yuh"]
            await ctx.channel.send('``'+random.choice(answers)+'``')

def setup(bot):
    bot.add_cog(Fun(bot))