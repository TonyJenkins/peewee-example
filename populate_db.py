#!/usr/bin/env python3


import peewee

from models import db, Tutor, Faculty, Room

global underwater_needlework, basket_weaving
global turing101, turing102, turing103, turing104, turing105, turing106
global lovelace201, lovelace202, lovelace203, lovelace204


def create_rooms():

    global turing101, turing102, turing103, turing104, turing105, turing106
    global lovelace201, lovelace202, lovelace203, lovelace204

    turing101 = Room.create(number='TU101', building='Turing')
    turing102 = Room.create(number='TU102', building='Turing')
    turing103 = Room.create(number='TU103', building='Turing')
    turing104 = Room.create(number='TU104', building='Turing')
    turing105 = Room.create(number='TU105', building='Turing')
    turing106 = Room.create(number='TU106', building='Turing')

    lovelace201 = Room.create(number='LO201', building='Lovelace')
    lovelace202 = Room.create(number='LO202', building='Lovelace')
    lovelace203 = Room.create(number='LO203', building='Lovelace')
    lovelace204 = Room.create(number='LO204', building='Lovelace')

    turing101.save()
    turing102.save()
    turing103.save()
    turing104.save()
    turing105.save()
    turing106.save()

    lovelace201.save()
    lovelace202.save()
    lovelace203.save()
    lovelace204.save()


def create_faculties():

    global underwater_needlework, basket_weaving

    underwater_needlework = Faculty.create(name='Underwater Needlework', dean='Prof John Jones')
    basket_weaving = Faculty.create(name='Extreme Basket Weaving', dean='Dr Jane Smith')

    underwater_needlework.save()
    basket_weaving.save()


def create_tutors():

        alice = Tutor.create(name='Alice Smith', faculty=underwater_needlework, room=turing101)
        bob = Tutor.create(name='Bob Jackson', faculty=underwater_needlework, room=turing102)
        charlie = Tutor.create(name='Charlie Brown', faculty=underwater_needlework, room=turing103)
        diana = Tutor.create(name='Diana Windows', faculty=underwater_needlework, room=turing104)
        eve = Tutor.create(name='Eve Lawrence', faculty=underwater_needlework, room=turing105)
        fred = Tutor.create(name='Fred Davies', faculty=underwater_needlework, room=turing106)

        george = Tutor.create(name='George Williams', faculty=basket_weaving, room=lovelace201)
        harry = Tutor.create(name='Harry Brown', faculty=basket_weaving, room=lovelace202)
        isabel = Tutor.create(name='Isabel Khan', faculty=basket_weaving, room=lovelace203)
        jack = Tutor.create(name='Jack Osbourne', faculty=basket_weaving, room=lovelace204)
        kate = Tutor.create(name='Kate Vickers', faculty=basket_weaving, room=lovelace204)
        larry = Tutor.create(name='Larry Lamb', faculty=basket_weaving, room=lovelace204)

        alice.save()
        bob.save()
        charlie.save()
        diana.save()
        eve.save()
        fred.save()

        george.save()
        harry.save()
        isabel.save()
        jack.save()
        kate.save()
        larry.save()


if __name__ == '__main__':

    try:
        create_rooms()
        create_faculties()
        create_tutors()
    except peewee.OperationalError:
        print('Error populating database tables. Most likely the database does not exist, or tables are missing.')
