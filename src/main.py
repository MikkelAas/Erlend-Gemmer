# Imports
from handler import get_clan_info, get_war_status
import discord
import os
from dotenv import load_dotenv


intents = discord.Intents.all()
client = discord.Client(intents=intents)
load_dotenv(".env")
bot_token = str(os.getenv("BOT_TOKEN"))


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("$hello"):
        value = ""
        try:
            value = message.content.split("$hello ", 1)[1]
        except Exception:
            await message.channel.send("Hello!")

        if value != "":
            await message.channel.send("Hello " + value + "!")

    elif message.content.startswith("$status"):
        await message.channel.send(get_war_status())

    elif message.content.startswith("$info"):
        await message.channel.send(get_clan_info())


client.run(bot_token)
