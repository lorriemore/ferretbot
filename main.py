import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

# list cogs here
extensions = [
    "cogs.init",
    "cogs.ferret",
    "cogs.lorrie"
]

# create client object
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot("$", intents=intents)

# load cogs
async def load_extensions():
    for x in extensions:
        try:
            await bot.load_extension(x)
        except Exception as e:
            raise Exception(f'{e}: failed to load extension {x}.')

# initialise bot
async def main():
    async with bot:
        await load_extensions()

        load_dotenv()
        await bot.start(os.getenv('FERRETBOT_TOKEN'))

asyncio.run(main())