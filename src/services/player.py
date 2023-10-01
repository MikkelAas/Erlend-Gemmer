from database.userRepository import get_member_tag, fetch_and_store
from api.players import fetch_player_info
from models.Player import Player
from discord import Embed
from embeds.player import generate_player_info_embed
from embeds.error import generate_error_embed


def get_player_info(name: str, count: int) -> Embed:
    player_tag = get_member_tag(name)

    if count >= 1:
        embed = generate_error_embed("Error")

        return embed

    if (player_tag == None):
        count += 1
        
        fetch_and_store()

        get_player_info(name, count)
        
        return

    player: Player = fetch_player_info(player_tag)

    embed = generate_player_info_embed(player)

    return embed
