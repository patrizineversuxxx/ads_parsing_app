import dbclass
from peewee import *


class AdInfo(Model):
    image_links = TextField()
    created = DateField()
    updated = DateField()
    prices = TextField()
    description = TextField()
    landlord_type = IntegerField() #1 to 2
    class Meta:
        database = dbclass.db
