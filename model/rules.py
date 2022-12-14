from enum import Enum


class Allowance(Enum):
    allowed = 1
    not_allowed = 2
    discussiable = 3

    @staticmethod
    def from_str(value: str):
        global map
        map = {
            'Да': Allowance.allowed,
            'Нет': Allowance.not_allowed,
            'По договоренности': Allowance.discussiable
        }

        assert value in map
        return map[value]


class Rules:
    def __init__(self, apart_capacity: int,
                 is_kids_allowed: Allowance,
                 is_animals_allowed: Allowance,
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
