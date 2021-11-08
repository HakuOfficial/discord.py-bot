import discord
from discord.ext import commands
from config import *


bot = commands.Bot(command_prefix=PREFIX, description="một con bot cho python discord.py")


@bot.event
async def on_ready():
    print("con bot đã chạy")


@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send('Hi, my prefix is !')

@bot.command(pass_context=True)
async def purge(ctx, amount:str):
    if amount == 'all':
        await ctx.channel.purge()
    else:
      await ctx.channel.purge(limit=(int(amount)+ 1))


bot.run(TOKEN, bot=True, reconnect=True)