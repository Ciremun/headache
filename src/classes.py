from datetime import datetime
from typing import NamedTuple

class Note(NamedTuple):
    date: datetime
    points: int
    med: str
