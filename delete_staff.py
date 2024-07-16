#!/usr/bin/env python3


from models import Tutor


if __name__ == '__main__':

    tutor_id = int(input('Enter id to delete: '))

    try:
        tutor = Tutor.get(Tutor.id == tutor_id)
    except Tutor.DoesNotExist:
        print('Tutor not found.')
    else:
        tutor.delete_instance()
        print('Tutor deleted.')
