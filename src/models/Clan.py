from models.WarLeague import WarLeague
from models.Member import Member


class Clan:
    def __init__(self, data: dict) -> None:
        self.tag = data.get("tag")
        self.name = data.get("name")
        self.war_league = WarLeague(data.get("warLeague"))
        self.war_wins = data.get("warWins")
        self.war_losses = data.get("warLosses")
        self.war_win_streak = data.get("warWinStreak")
        self.member_list = [Member(item) for item in data.get("memberList")]
