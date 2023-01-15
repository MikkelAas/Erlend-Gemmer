import requests
from models.Clan import Clan
from models.War import War
from requests import Response
from api.constants import base_url, version, clan_tag, headers


def fetch_clan_info() -> Clan:
    url = base_url + version + "/clans/%s" % clan_tag

    res: Response = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise ValueError

    data = res.json()

    clan = Clan(data)

    return clan


def fetch_current_clan_war() -> War:
    url = base_url + version + "/clans/%s" % clan_tag + "/currentwar"

    res: Response = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise ValueError

    data = res.json()

    war = War(data)

    return war
