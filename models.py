#!/usr/bin/env python3


from peewee import *


from config import DATABASE


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase(DATABASE)


class Faculty(BaseModel):
    name = CharField(max_length=64)
    dean = CharField(max_length=64)


class Room(BaseModel):
    number = CharField(max_length=16)
    building = CharField(max_length=32)


class Tutor(BaseModel):
    name = CharField(max_length=64)
    faculty = ForeignKeyField(Faculty, backref='members')
    room = ForeignKeyField(Room, backref='occupants')
