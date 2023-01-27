# Imports
from services.clan import get_clan_info, get_war_status
from services.player import get_player_info
from database.database import get_member_tag
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
        await message.channel.send(embed=get_war_status())

    elif message.content.startswith("$info"):
        await message.channel.send(embed=get_clan_info())

    elif message.content.startswith("$player"):
        name = message.content.split("$player ", 1)[1]
        await message.channel.send(embed=get_player_info(name))

get_member_tag("Haspetre")

client.run(bot_token)
