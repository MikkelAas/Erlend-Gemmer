from api.clans import fetch_clan_info, fetch_current_clan_war
from models.Clan import Clan
from models.War import War
from discord import Embed
from embeds.clan import genereate_war_status_embed, generate_clan_info_embed


def get_war_status() -> Embed:
    """
    Retrieves the war status of the clan from the clash of clans API
    """
    current_war: War = fetch_current_clan_war()

    embed = genereate_war_status_embed(current_war)

    return embed


def get_clan_info() -> Embed:
    """
    Retrieves the clan info from the clash of clans API
    """
    clan: Clan = fetch_clan_info()

    clan_info_embed = generate_clan_info_embed(clan)

    return clan_info_embed
