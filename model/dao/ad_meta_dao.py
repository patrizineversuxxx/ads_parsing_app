from peewee import *
from . import dbclass
from . import *

class AdMetaDAO(Model):
    url = CharField()
    ad_info_id = IntegerField()
    apartment_info_id = IntegerField()
    building_info_id = IntegerField()
    rules_id = IntegerField()
    class Meta():
        database = dbclass.db