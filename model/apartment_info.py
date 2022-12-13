from enum import Enum


class RenovationType(Enum):
    WithoutRenovation = 1
    PartlyRenovated = 2
    Redecorated = 3
    EuroRenovation = 4
    DesignersRenovation = 5
    MajorOverhauled = 6


@staticmethod
def from_str(value: str) -> RenovationType:
    global map
    map = {
        'Без ремонта': RenovationType.WithoutRenovation,
        'Частичный ремонт': RenovationType.PartlyRenovated,
        'Косметический ремонт': RenovationType.Redecorated,
        'Евроремонт': RenovationType.EuroRenovation,
        'Дизайнерский ремонт': RenovationType.DesignersRenovation,
        'Капитальный ремонт': RenovationType.MajorOverhauled
    }

    assert value in map
    return map[value]


class ApartmentInfo:
    def __init__(self,
                 address: str,
                 square: int,
                 room_number: int,
                 smartin_number: int,
                 height: float,
                 floor: int,
                 has_balcony: bool,
                 is_furnitured: bool,
                 renovation_type: RenovationType,
                 features: str,
                 household_features: str
                 ):
        self._address = address
        self._square = square
        self._room_number = room_number
        self._smartin_number = smartin_number
        self._height = height
        self._floor = floor
        self._has_balcony = has_balcony
        self._is_furnitured = is_furnitured
        self._renovation_type = renovation_type
        self._features = features
        self._household_features = household_features

    @property
    def address(self) -> str:
        return self._address

    @property
    def square(self) -> int:
        return self._square

    @property
    def room_number(self) -> int:
        return self._room_number

    @property
    def smartin_number(self) -> int:
        return self._smartin_number

    @property
    def height(self) -> float:
        return self._height

    @property
    def floor(self) -> int:
        return self._floor

    @property
    def has_balcony(self) -> bool:
        return self._has_balcony

    @property
    def is_furnitured(self) -> bool:
        return self._is_furnitured

    @property
    def renovation_type(self) -> RenovationType:
        return self._renovation_type

    @property
    def features(self) -> str:
        return self._features

    @property
    def household_features(self) -> str:
        return self._household_features
