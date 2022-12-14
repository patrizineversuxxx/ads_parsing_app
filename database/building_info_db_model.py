from peewee import *
from dbclass import db


class BuildingInfoDb(Model):
    building_type_db = IntegerField()  # must be in range from 1 to 6
    is_new_building_db = BooleanField()
    has_elevator_db = BooleanField()
    floor_number_db = IntegerField()

    class Meta:
        database = db

