import Oponent
from dataclasses import dataclass
import sys
sys.path.append('./models/Oponent.py')


@dataclass
class War:
    state: str
    oponent: Oponent
