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

@bot.event
async def on_message(message):
    if (message.author == bot.user):
        return
    
    text = "This bot is stupid."

    if message.content:
        response = text
        await message.channel.send(response)

bot.run(TOKEN)