import discord, os, sqlite3
from discord.ext import commands
import oil

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents().default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['TOKEN'])

bot = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.command(name='banned_words')
async def _banned_words(ctx, arg):
    pass


