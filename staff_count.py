#!/usr/bin/env python3


from peewee import OperationalError

from models import Tutor


if __name__ == '__main__':

    try:
        staff_number = (Tutor
                        .select()
                        .count())

        print(f'There {"is" if staff_number == 1 else "are"} {staff_number} tutor'
              f'{"s" if staff_number != 1 else ""} in the database.')

    except OperationalError:
        print('Error: database is not available, or table does not exist.')
