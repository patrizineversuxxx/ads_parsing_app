from enum import Enum


class RulesValues(Enum):
    allowed = "Да"
    not_allowed = 'Нет'
    discussiable = 'По договоренности'


class Rules:
    def __init__(self, apart_capacity: int,
                 is_kids_allowed: RulesValues,
                 is_animals_allowed: RulesValues,
                 utility_payments: str,
                 has_prepayment: str
                 ):
        self._apart_capacity = apart_capacity
        self._is_kids_allowed = is_kids_allowed
        self._is_animals_allowed = is_animals_allowed
        self._utility_payments = utility_payments
        self._has_prepayment = has_prepayment

    @property
    def apart_capacity(self):
        return self._apart_capacity

    @property
    def is_kids_allowed(self):
        return self._is_kids_allowed

    @property
    def is_animals_allowed(self):
        return self._is_animals_allowed

    @property
    def utility_payments(self):
        return self._utility_payments

    @property
    def has_prepayment(self):
        return self._utility_payments
