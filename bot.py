import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

#test command
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.command()
async def plex(ctx, *, movie: str):
#command to add movies to a plex movie server list. Use it by doing "!plex 'movie name'". It will add 'movie name' to the list of movies.

    exists = False
    
    #check to see if the file is already on the list of movies to be added to the plex.
    with open('new.txt', 'r') as newFile:
        for line in newFile:
            if movie in line:
                exists = True
                await ctx.send("Movie is already on the list to be added to the Plex!")
                
    #check to see if the movie is already on the plex
    with open('plex.txt', 'r') as plexFile:
        for line in plexFile:
            if movie in line:
                exists = True
                await ctx.send("Movie is already on the Plex!")
                
    #adds movie to the list of plex movies to be added.
    if exists is False:
        with open('new.txt', 'a') as newF:
            newF.write(movie + '\n')
            await ctx.send("Movie added to list! <:ura:390954421942484992>")
    
bot.run('')
