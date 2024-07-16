#!/usr/bin/env python3


from models import db
from models import Tutor, Faculty, Room


if __name__ == '__main__':

    db.create_tables([
        Tutor,
        Faculty,
        Room,
    ])
