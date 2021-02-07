import sqlite3
import threading
from datetime import datetime
from typing import Callable, Any, List, Tuple

from .log import logger

conn = sqlite3.connect('headache.db', isolation_level=None, check_same_thread=False, detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()
lock = threading.Lock()


def db(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        try:
            lock.acquire(True)
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
        finally:
            lock.release()
    return wrapper


@db
def db_init() -> None:

    tables = [
        'create table if not exists notes (id integer primary key, d timestamp, points integer, med text)'
    ]

    for q in tables:
        cursor.execute(q)


@db
def add_note(date: datetime, points: int, med: str) -> None:
    cursor.execute(
        'insert into notes (d, points, med) values (?, ?, ?)', (date, points, med))

@db
def get_notes() -> List[Tuple[datetime, int, str]]:
    cursor.execute('select d, points, med from notes')
    return cursor.fetchall()

db_init()
