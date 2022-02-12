import discord
from discord.ext import commands


class Useful(commands.Cog):

    '''
       Hello, user that is reading this!
       In this class, you will find every useful command from our selfbot.
    '''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self,ctx):
        await ctx.message.delete()
        await ctx.channel.send('''```
<prefix> - bot prefix
[] - must
() - optional 

<prefix> ask8ball [question] // Ask the 8ball a question.
<prefix> ascii [text] // Convert your message into ASCII!
<prefix> flood // Floods the chat with unicode characters.
<prefix> lenny // Sends a lenny face into the chat.
<prefix> rslur // Sends a random slur in the chat (invis unicode char)
<prefix> suntzu // Sends a random quote from Sun Tzu.
<prefix> hentai // Sends a hentai gif.
<prefix> tits // Sends boobies.
<prefix> covid // Sends COVID-19 stats.
<prefix> encodebase64 [text] // Encodes text into Base64.
<prefix> invite [invite] // Sends an invite with a sketchy link.
<prefix> ip [ip] // Tracks the given IP using an API.
<prefix> junk // Sends some unicode characters.
<prefix> lmgtfy [text] // Returns a lmgtfy link with the given text.
<prefix> ragequit // Leaves current server.
<prefix> setnickname [text] // Sets your nickname to the given text.
<prefix> bubblewrap // Copypasta.
<prefix> masturbate // Copypasta.
<prefix> discordmodgoodbye // Copypasta.
<prefix> discorddown // Copypasta.
<prefix> edate // Copypasta.
<prefix> imjustgoingtosayit // Copypasta.
<prefix> notgonnabeactive // Copypasta.
<prefix> senpai // Copypasta.
<prefix> yourmotherandi // Copypasta.
<prefix> zerotwo // Copypasta.
        ```''')

def setup(bot):
    bot.add_cog(Useful(bot))
