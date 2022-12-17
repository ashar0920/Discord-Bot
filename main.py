
import discord
from discord.ext import commands

TOKEN=''
intents=discord.Intents.all()

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready to use!')

@bot.command(name='hello')
async def msg(ctx):
    if ctx.author == bot.user:
        return
    else:
        await ctx.send("Hey!")

bot.run(TOKEN)