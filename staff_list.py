#!/usr/bin/env python3


from peewee import OperationalError
from tabulate import tabulate

from models import Tutor


if __name__ == '__main__':

    try:
        staff = (Tutor
                 .select()
                 .order_by(Tutor.name)
                 )

        staff_list = [(s.name, s.faculty.name, s.room.number, s.room.building) for s in staff]

    except OperationalError:
        print('Error: database is not available, or table does not exist.')

    else:
        print(tabulate(staff_list, headers=['Name', 'Faculty', 'Room', 'Building'], tablefmt='fancy_grid'))
        print()

