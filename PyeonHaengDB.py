import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
Token = os.environ.get('DiscordBotToken')
ChannelID = os.environ.get('DiscordBotChannelID')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    channel = bot.get_channel(int(ChannelID))
    await channel.send('everyone 서버가 죽었습니다.')


@ bot.command()
async def hello(message):
    await message.channel.send('Hi!')

bot.run(Token)
