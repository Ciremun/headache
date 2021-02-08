import os
import psycopg2
import threading
from datetime import datetime
from typing import Callable, Any, List, Tuple

from .log import logger

conn = None
cursor = None
lock = threading.Lock()


def db_connect():
    global conn, cursor
    if conn is not None:
        conn.close()
    conn = psycopg2.connect(os.environ.get('DATABASE_URL'), sslmode='require')
    conn.autocommit = True
    cursor = conn.cursor()


def db(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        try:
            lock.acquire(True)
            return func(*args, **kwargs)
        except psycopg2.OperationalError:
            logger.info('try reconnect')
            db_connect()
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(e, exc_info=1)
        finally:
            lock.release()
    return wrapper


@db
def db_init() -> None:

    tables = [
        'create table if not exists notes (id serial primary key, d timestamp, points integer, med text)'
    ]

    for q in tables:
        cursor.execute(q)


@db
def add_note(date: datetime, points: int, med: str) -> None:
    cursor.execute(
        'insert into notes (d, points, med) values (%s, %s, %s)', (date, points, med))

@db
def get_notes() -> List[Tuple[datetime, int, str]]:
    cursor.execute('select d, points, med from notes')
    return cursor.fetchall()


@db
def delete_note(note_id: int) -> None:
    cursor.execute('delete from notes where id = %s', (note_id,))


@db
def get_max_note_id() -> Tuple[int]:
    cursor.execute('select max(id) from notes')
    return cursor.fetchone()


db_connect()
db_init()
