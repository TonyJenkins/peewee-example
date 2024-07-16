#!/usr/bin/env python3

from tabulate import tabulate

from models import Tutor


if __name__ == '__main__':

    staff = (Tutor
             .select()
             .order_by(Tutor.name)
             )

    staff_list = [(s.name, s.faculty.name, s.room.number, s.room.building) for s in staff]

    print(tabulate(staff_list, headers=['Name', 'Faculty', 'Room', 'Building'], tablefmt='fancy_grid'))
    print()

