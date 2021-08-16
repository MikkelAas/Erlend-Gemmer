# This file contains all the API-related functions

# Imports
import requests
import json
import os
from dotenv import load_dotenv
from util import get_time

# Loads the environment file
load_dotenv('.env')

# Stores the API token that is kept in the .env file
API_token = str(os.getenv('API_TOKEN'))
headers = {"Authorization": "Bearer " + API_token}

# The API URLs
clanInfoURL = "https://api.clashofclans.com/v1/clans/%232LUGVU89Q"
currentWarURL = "https://api.clashofclans.com/v1/clans/%232LUGVU89Q/currentwar"


# Retrieves the war status of the clan from the clash of clans API
def get_war_status():
    res = requests.get(currentWarURL, headers=headers)
    json_data = json.loads(res.text)
    if json_data['state'] == 'notInWar':
        return "We are currently not in a war."
    else:
        return ("We are currently in a war with " + json_data['opponent']['name'] + ". " + "It will end in " + get_time(json_data[
            'endTime']) + ". " + "The following members are drafted in the war: ")


# Retrieves the clan info from the clash of clans API
def get_clan_info():
    res = requests.get(clanInfoURL, headers=headers)
    json_data = json.loads(res.text)
    return "Tag: " + json_data['tag']
