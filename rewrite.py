'''
The MIT License (MIT)
Copyright © 2022 tacolift

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import json
import os
import discord
from discord.ext import commands
with open("config.json") as f:
    configuration = json.load(f)

token = configuration.get("token")
prefix = configuration.get("prefix")

bot = commands.Bot(command_prefix=prefix, self_bot = True)
bot.remove_command('help')
#print(f"User Token: {token}")
#print(f"Bot Prefix: {prefix}")

print(''' __  ____   ___   _ _   _    _    _       ____  _____ _     _____ ____   ___ _____ 
 \ \/ /\ \ / / \ | | \ | |  / \  | |     / ___|| ____| |   |  ___| __ ) / _ \_   _|
  \  /  \ V /|  \| |  \| | / _ \ | |     \___ \|  _| | |   | |_  |  _ \| | | || |
  /  \   | | | |\  | |\  |/ ___ \| |___   ___) | |___| |___|  _| | |_) | |_| || |
 /_/\_\  |_| |_| \_|_| \_/_/   \_\_____| |____/|_____|_____|_|   |____/ \___/ |_|\n''')
print(f"[+] User Token: {token}")
print(f"[+] User Prefix: {prefix}\n")

# Extensions
for filename in os.listdir('./main/extensions'):
    if filename.endswith('.py'):
        bot.load_extension(f'main.extensions.{filename[:-3]}')
bot.run(token)
