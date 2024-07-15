#!/usr/bin/env python3

from peewee import SqliteDatabase
from tabulate import tabulate


from config import DATABASE
from models import Tutor


if __name__ == '__main__':
    db = SqliteDatabase(DATABASE)
    db.connect()

    staff = (Tutor
             .select()
             .order_by(Tutor.name)
             )

    staff_list = [(s.name, s.faculty.name, s.room.number, s.room.building) for s in staff]

    print(tabulate(staff_list, headers=['Name', 'Faculty', 'Room', 'Building'], tablefmt='fancy_grid'))
    print()

