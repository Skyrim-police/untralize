import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')



token = os.environ.get('Bot_token')
bot.run(str(token))
