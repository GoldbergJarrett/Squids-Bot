import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

#Oauth

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@bot.command()
async def plex(ctx, *, movie: str):

    exists = False

    with open('C:/Users/goldb/Desktop/new.txt', 'r') as newFile:
        for line in newFile:
            if movie in line:
                exists = True
                await ctx.send("Movie is already on the list to be added to the Plex!")

    with open('C:/Users/goldb/Desktop/plex.txt', 'r') as plexFile:
        for line in plexFile:
            if movie in line:
                exists = True
                await ctx.send("Movie is already on the Plex!")

    if exists is False:
        with open('C:/Users/goldb/Desktop/new.txt', 'a') as newF:
            newF.write(movie + '\n')
            await ctx.send("Movie added to list! :ura:")

@bot.command()
async def test(ctx, *, movie: str):
    await ctx.send(movie)
