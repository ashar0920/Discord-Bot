
import discord
from discord.ext import commands

TOKEN = 'MTA1MzU0MjM5MDY1NDMwODQyNA.GnQGs6.iptJpqgN-5IjKVLBuIYEb_3MlqQ2hPc7D9MM1w'
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
        
@bot.command(name='vacuum')
async def msg(ctx):
    if ctx.author == bot.user:
        return
    else:
        await ctx.send("ooh tasty :yum: ")

@bot.command(name='test')
async def msg(ctx):
    if ctx.author == bot.user:
        return
    else:
        await ctx.send(":sob:")
bot.run(TOKEN)
