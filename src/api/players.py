import requests
from models.Player import Player
from requests import Response
from api.constants import base_url, version, headers
import urllib.parse


def fetch_player_info(tag: str) -> Player:

    tag = urllib.parse.quote(tag)

    url = f"{base_url}{version}/players/{tag}"

    res: Response = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise ValueError

    data = res.json()

    player = Player(data)

    return player
