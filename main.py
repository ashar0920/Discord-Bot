
import discord
import random
import os
import asyncio
import dotenv
import sys
from dotenv import load_dotenv
from discord.ext import commands
#pycord

#client = discord.Client()
#TOKEN = 'MTA1MzU0MjM5MDY1NDMwODQyNA.GnQGs6.iptJpqgN-5IjKVLBuIYEb_3MlqQ2hPc7D9MM1w'
intents = discord.Intents.all()

bot = commands.Bot()
#bot = discord.Bot(intents=discord.Intents.discord())
##client = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot is ready to use!")

@bot.slash_command(name="hello",description="says hello to the user")
async def msg(ctx):
        await ctx.respond("Hey!")

# @bot.command(name='vacuum')
# async def msg(ctx):
#     if ctx.author == bot.user:
#         return
#     else: 
#         await ctx.send("ooh tasty <a:DonutLicker:1053598213262815232>") 

# @bot.command(name='test')
# async def msg(ctx):
#     if ctx.author == bot.user:
#         return
#     else:
#         await ctx.send(":sob:")

# @bot.command(name='test1')
# async def msg(ctx):
#     if ctx.author == bot.user:
#         return
#     else:
#         await ctx.send("Hey!")
        
#peensize command
    
@bot.slash_command(name="peensize",description="a random peensize command")
async def msg(ctx):
    peensize = random.randint(0,9)
    await ctx.respond(f"your peen is {peensize} inches")
    
bot.run(os.getenv('DISCORD_TOKEN'))
