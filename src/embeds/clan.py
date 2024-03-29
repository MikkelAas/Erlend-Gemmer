from typing import List
from models.War import War
from models.Clan import Clan
from models.Member import Member
from discord import Embed, Colour
from utils.date_util import get_time


def genereate_war_status_embed(war: War) -> Embed:
    if war.status == "notInWar":
        return Embed(
            title="War status",
            description="We are currently not in a war.",
            colour=Colour.red(),
        )

    war_end_time = get_time(war.end_time)

    embed = Embed(
        title="War state", description="We are currently in a war", color=Colour.green()
    )

    embed.add_field(name="Oponent", value=war.oponent.name)
    embed.add_field(name="End date", value=war_end_time)

    return embed


def generate_clan_info_embed(clan: Clan) -> Embed:
    embed = Embed(
        title="Erlend Gemmer", description="General info", colour=Colour.blue()
    )

    win_rate: str = str(calculate_win_rate(clan.war_wins, clan.war_losses))

    clan_members: str = get_all_clan_members(clan.member_list)

    embed.add_field(name="Clan tag", value=clan.tag)
    embed.add_field(name="Name", value=clan.name)
    embed.add_field(name="War league", value=clan.war_league.name)
    embed.add_field(name="Win rate", value=win_rate)
    embed.add_field(name="Win streak", value=clan.war_win_streak, inline=False)
    embed.add_field(name="Members", value=clan_members, inline=False)

    return embed


def get_all_clan_members(clan_members: List[Member]) -> str:
    """
    Retrieves all the members of a clan.
    """

    string: str = ""

    for member in clan_members:
        string += member.name + ", "

    return string[:-2]


def calculate_win_rate(wins: int, losses: int) -> float:
    """
    Calculates the average win rate
    """
    return round(
        wins / (wins + losses),
        2,
    )
