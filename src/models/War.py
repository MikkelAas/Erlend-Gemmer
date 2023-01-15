from models.Oponent import Oponent
from dataclasses import dataclass


@dataclass
class War:
    state: str
    oponent: Oponent
