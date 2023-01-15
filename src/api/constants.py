from dotenv import load_dotenv
import os

load_dotenv(".env")

API_token: str = str(os.getenv("API_TOKEN"))
headers: object = {"Authorization": "Bearer " + API_token}

base_url = "https://api.clashofclans.com/"
version = "v1"
clan_tag = "%232LUGVU89Q"