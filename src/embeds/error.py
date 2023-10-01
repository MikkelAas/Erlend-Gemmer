from discord import Embed, Color


def generate_error_embed(message: str):
    embed = Embed(title="Error", description="An error has occured", color=Color.red())

    embed.add_field(name="Message", value=message)

    return embed
