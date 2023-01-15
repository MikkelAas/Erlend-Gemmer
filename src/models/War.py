from models.Oponent import Oponent
from dataclasses import dataclass


class War:
    def __init__(self, data: dict) -> None:
        self.status: str = data.get("state")
        self.end_time = data.get("endTime")
        self.oponent = Oponent(data.get("opponent"))
