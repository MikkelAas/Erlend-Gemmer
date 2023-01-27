class Player:
    def __init__(self, data: dict) -> None:
        self.name: str = data["name"]
        self.attack_wins: int = data["attackWins"]
        self.defense_wins: int = data["defenseWins"]
        self.town_hall_level: int = data["attackWins"]
        self.town_hall_weapon_level: int = data["townHallWeaponLevel"]
        self.versus_battle_wins: int = data["versusBattleWins"]
        self.donations: int = data["donations"]
        self.donations_recieved: int = data["donationsReceived"]
        self.clan_capital_contributions: int = data["clanCapitalContributions"]
