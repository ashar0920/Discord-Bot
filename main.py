
import discord
import random
from discord.ext import commands


#client = discord.Client()
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
        await ctx.send("ooh tasty <a:DonutLicker:1053598213262815232>") 

@bot.command(name='test')
async def msg(ctx):
    if ctx.author == bot.user:
        return
    else:
        await ctx.send(":sob:")
        
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('!random'):
#         num = random.randint(1, 100)
#         await message.channel.send('Your random number is: {}'.format(num))

        

bot.run(TOKEN)
