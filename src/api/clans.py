import requests
from models.Clan import Clan
from models.War import War
from models.Member import Member
from requests import Response
from api.constants import base_url, version, clan_tag, headers


def fetch_clan_info() -> Clan:
    url = f"{base_url}{version}/clans/{clan_tag}"

    res: Response = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise ValueError

    data = res.json()

    clan = Clan(data)

    return clan


def fetch_current_clan_war() -> War:
    url = f"{base_url}{version}/clans/{clan_tag}/currentwar"

    res: Response = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise ValueError

    data = res.json()

    war = War(data)

    return war


def fetch_clan_members() -> list[Member]:
    url = f"{base_url}{version}/clans/{clan_tag}/members"

    res: Response = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise ValueError

    data = res.json()

    members = [Member(item) for item in data.get("items")]

    return members
