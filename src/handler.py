# This file contains all the API-related functions

# Imports
from util import get_time
from api.clans import fetch_clan_info, fetch_current_clan_war
from models.Clan import Clan
from models.Member import Member
from models.War import War
from typing import List
from discord import Embed

# Retrieves the war status of the clan from the clash of clans API
def get_war_status() -> Embed:
    current_war: War = fetch_current_clan_war()

    embed = genereate_war_status_embed(current_war)

    return embed


# Retrieves the clan info from the clash of clans API
def get_clan_info() -> Embed:
    clan: Clan = fetch_clan_info()

    clan_info_embed = generate_clan_info_embed(clan)

    return clan_info_embed


# Retrieves all the members of a clan
def get_all_clan_members(clan_members: List[Member]) -> str:

    string: str = ""

    for member in clan_members:
        string += member.name + ", "

    return string[:-2]


# Calculates the average win rate
def calculate_win_rate(wins: int, losses: int) -> float:
    return round(
        wins / (wins + losses),
        2,
    )


def generate_clan_info_embed(clan: Clan) -> Embed:
    embed = Embed(title="Erlend Gemmer", description="General info")

    win_rate: str = str(calculate_win_rate(clan.war_wins, clan.war_losses))

    clan_members: str = get_all_clan_members(clan.member_list)

    embed.add_field(name="Clan tag", value=clan.tag)
    embed.add_field(name="Name", value=clan.name)
    embed.add_field(name="War league", value=clan.war_league.name)
    embed.add_field(name="Win rate", value=win_rate)
    embed.add_field(name="Win streak", value=clan.war_win_streak, inline=False)
    embed.add_field(name="Members", value=clan_members, inline=False)

    return embed


def genereate_war_status_embed(war: War) -> Embed:
    if war.status == "notInWar":
        return Embed(title="War status", description="We are currently not in a war.")

    war_end_time = get_time(war.end_time)

    embed = Embed(title="War state", description="We are currently in a war")

    embed.add_field(name="Oponent", value=war.oponent.name)
    embed.add_field(name="End date", value=war_end_time)

    return embed
