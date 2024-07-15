#!/usr/bin/env python3

from peewee import SqliteDatabase

from config import DATABASE
from models import Tutor


if __name__ == '__main__':
    db = SqliteDatabase(DATABASE)
    db.connect()

    staff_number = (Tutor
                    .select()
                    .count())

    print(f'There {"is" if staff_number == 1 else "are"} {staff_number} tutor'
          f'{"s" if staff_number != 1 else ""} in the database.')
