"""
Boilerplate taken from
https://realpython.com/how-to-make-a-discord-bot-python/#what-is-a-bot
"""

import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='test')
async def test_bot(messageBox):
    response = "This is a test."
    await messageBox.send(response)

bot.run(TOKEN)