import requests
from models.Clan import Clan
from models.War import War
from requests import Response
import os
from dotenv import load_dotenv

load_dotenv(".env")

base_url = "https://api.clashofclans.com/"
version = "v1"
clan_tag = "%232LUGVU89Q"

API_token: str = str(os.getenv("API_TOKEN"))
headers: object = {"Authorization": "Bearer " + API_token}


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
