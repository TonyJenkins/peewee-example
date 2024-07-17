#!/usr/bin/env python3


import peewee

from models import Tutor, Faculty, Room


if __name__ == '__main__':

    faculty = Faculty.create(name='Extreme Ironing', dean='Prof I Board')
    faculty.save()

    room = Room.create(number='42', building='The Answer Building')
    room.save()

    tutor = Tutor.create(name='Ivan Hotiron', faculty=faculty, room=room)
    tutor.save()
