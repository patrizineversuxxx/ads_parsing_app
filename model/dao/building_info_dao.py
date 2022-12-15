from peewee import *
from . import dbclass

class BuildingInfoDAO(Model):
    building_type = IntegerField()  # must be in range from 1 to 6
    is_new_building = BooleanField()
    has_elevator = BooleanField()
    floor_number = IntegerField()

    class Meta:
        database = dbclass.db
