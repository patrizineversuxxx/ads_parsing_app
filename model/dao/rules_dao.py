from . import dbclass
from peewee import *


class RulesDAO(Model):
    apart_capacity = IntegerField()
    is_kids_allowed = IntegerField()
    is_animals_allowed = IntegerField()
    utility_payments = TextField()
    has_prepayment = TextField()

    class Meta:
        database = dbclass.db
