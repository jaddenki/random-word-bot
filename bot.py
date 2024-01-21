# bot.py
import os
import random
import nltk
import discord
from nltk.corpus import words
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Download the words dataset if not already present
nltk.download('words')

# Create Intents
intents = discord.Intents.all()
intents.messages = True  # Enable MESSAGE_CONTENT intent

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f'Message: {message}')  # Print entire message object
    print(f'Message content: {message.content}')

    if message.content.startswith('/random'):
        # Fetch a random word from the NLTK words dataset
        whatToSay = words.words()
        response = random.choice(whatToSay)
        await message.channel.send(response)

client.run(TOKEN)
