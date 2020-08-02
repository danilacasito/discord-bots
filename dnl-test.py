


import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='dnlbot>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def suma(ctx, numOne: int, numtwo: int):
    await ctx.send(numOne + numtwo)
@bot.command()
async def resta(ctx, numOne: int, numtwo: int):
    await ctx.send(numOne - numtwo)
@bot.command()
async def multiplica(ctx, numOne: int, numtwo: int):
    await ctx.send(numOne * numtwo)
@bot.command()
async def divide(ctx, numone: int, numtwo: int):
    await ctx.send(numone / numtwo)
@bot.command()
async def random(ctx, numone: int, numtwo: int):
    await ctx.send(random.randint(numone, numtwo))


bot.run("NzM5NDA2MTExNjgxMDE5OTM1.XyZ_mg.zWfRegEy__lUM5fMzDSYxppk08w")
