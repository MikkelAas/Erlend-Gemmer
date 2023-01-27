from tinydb import TinyDB, Query
from models.Member import Member
from api.clans import fetch_clan_members
import sqlite3


PATH_TO_DB = "src/database/database.db"


def init():
    connection = sqlite3.connect(PATH_TO_DB)

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user(
            username VARCHAR,
            tag VARCHAR
        )
    """
    )

    cursor.close()
    connection.close()


def insert_members(members: list[Member]):
    connection = sqlite3.connect(PATH_TO_DB)

    cursor = connection.cursor()

    members_as_tuples = [(member.name, member.tag) for member in members]

    cursor.executemany(
        """
        INSERT INTO user VALUES(?,?)
    """,
        members_as_tuples,
    )

    cursor.close()
    connection.close()


def get_member_tag(name: str) -> str:
    connection = sqlite3.connect(PATH_TO_DB)

    cursor = connection.cursor()

    result = cursor.execute(
        f"""
        SELECT tag 
        FROM user 
        WHERE username = '{name}'
    """
    ).fetchall()

    tag = result[0]

    cursor.close()
    connection.close()

    return tag


def fetch_and_store():
    members = fetch_clan_members()

    insert_members(members)


init()

fetch_and_store()