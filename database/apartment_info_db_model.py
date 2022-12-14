import dbclass
from peewee import *


class ApartmentInfoDb(Model):
    address = TextField()
    square = IntegerField()
    room_number = IntegerField()
    smartin_number = IntegerField()
    height = FloatField()
    floor = IntegerField()
    has_balcony = BooleanField()
    is_furnitured = BooleanField()
    renovation_type = IntegerField()  # from 1 to 6
    features = TextField()
    household_features = TextField()

    class Meta:
        database = dbclass.db
