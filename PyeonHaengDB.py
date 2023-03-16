import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
Token = os.environ.get('DiscordBotToken')
intents = discord.Intents.default()

game = discord.Game('감시 중')

bot = commands.Bot(command_prefix='!',
                   status=discord.Status.online, activity=game, intents=intents)

bot.run(Token)
