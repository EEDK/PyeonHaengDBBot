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
    # await channel.send('!!!')


@bot.command()
async def hello(message):
    await message.channel.send('Hi!')


async def send_shutdown_message():
    channel = bot.get_channel(int(ChannelID))
    await channel.send('프로그램이 종료됩니다.')


def run():
    bot.run(Token)


run()
