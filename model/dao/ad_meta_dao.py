from peewee import *
from . import dbclass
from .ad_info_dao import AdInfoDAO
from .apartment_info_dao import ApartmentInfoDAO
from .building_info_dao import BuildingInfoDAO
from .rules_dao import RulesDAO


class AdMetaDAO(Model):
    url = CharField()
    ad_info_id = ForeignKeyField(AdInfoDAO)
    apartment_info_id = ForeignKeyField(ApartmentInfoDAO)
    building_info_id = ForeignKeyField(BuildingInfoDAO)
    rules_id = ForeignKeyField(RulesDAO)

    class Meta():
        database = dbclass.db
