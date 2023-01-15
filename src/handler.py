# This file contains all the API-related functions

# Imports
from util import get_time
from api.clans import fetch_clan_info, fetch_current_clan_war
from models.Clan import Clan
from models.Member import Member
from models.War import War
from typing import List

# Retrieves the war status of the clan from the clash of clans API
def get_war_status() -> str:
    current_war: War = fetch_current_clan_war()

    if current_war.status == "notInWar":
        return "We are currently not in a war."

    war_end_time = get_time(current_war.end_time)

    return (
        "We are currently in a war with "
        + current_war.oponent.name
        + ". "
        + "It will end in "
        + war_end_time
        + ". "
        + "The following members are drafted in the war: "
    )


# Retrieves the clan info from the clash of clans API
def generate_clan_info_text() -> str:
    clan: Clan = fetch_clan_info()

    win_rate: str = str(calculate_win_rate(clan.war_wins, clan.war_losses))

    clan_members: str = get_all_clan_members(clan.member_list)

    return (
        "Tag: "
        + clan.tag
        + "\n"
        + "Name: "
        + clan.name
        + "\n"
        + "War league: "
        + clan.war_league.name
        + "\n"
        + "Win rate: "
        + win_rate
        + "\n"
        + "Current winstreak: "
        + str(clan.war_win_streak)
        + "\n"
        + "Members: "
        + clan_members
    )


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
