#!/usr/bin/env python3


from peewee import SqliteDatabase


from config import DATABASE
from models import Tutor, Faculty, Room


if __name__ == '__main__':

    db = SqliteDatabase(DATABASE)

    db.connect()
    db.create_tables([
        Tutor,
        Faculty,
        Room,
    ])

