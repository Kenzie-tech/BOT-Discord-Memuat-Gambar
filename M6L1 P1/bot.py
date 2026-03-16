import discord
from logic import ReveAPI
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

api = ReveAPI("papi.e5d0316e-ecda-4492-81b8-ef3eb2d67217.NGMZSBn8CyybBvHMhRIe21iStJGJe9rU")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$generate'):
        file_name = str(datetime.now())
        api.generate_reve_image(message.content, file_name=file_name)
        await message.channel.send(file=discord.file(file_name))

client.run('PUT TOKEN HERE')