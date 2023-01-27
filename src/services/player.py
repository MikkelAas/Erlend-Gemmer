from database.database import get_member_tag
from api.players import fetch_player_info
from models.Player import Player
from discord import Embed
from embeds.player import generate_player_info_embed


def get_player_info(name: str) -> Embed:
    player_tag = get_member_tag(name)

    player: Player = fetch_player_info(player_tag)

    embed = generate_player_info_embed(player)

    return embed
