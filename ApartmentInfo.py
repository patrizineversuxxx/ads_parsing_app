import RenovationType

class ApartmentInfo:
    def __init__(self, 
            square : float, 
            rooms_count : int, 
            smartins_count : int, 
            apart_height : float, 
            apart_floor : int, 
            has_balcony : bool, 
            is_furnitured : bool, 
            renovation_type : RenovationType, 
            features : str, 
            household_features : str
    ):
        self._square = square
        self._rooms_count = rooms_count
        self._smartins_count = smartins_count
        self._apart_height = apart_height
        self._apart_floor = apart_floor
        self._has_balcony = has_balcony
        self._is_furnitured = is_furnitured
        self._renovation_type = renovation_type
        self._features = features
        self._household_features = household_features

    @property
    def square(self) -> float:
        return self._square

    @property
    def rooms_count(self) -> int:
        return self._rooms_count

    @property
    def smartins_count(self) -> int:
        return self._smartins_count

    @property
    def apart_height(self) -> float:
        return self._apart_height

    @property
    def apart_floor(self) -> int:
        return self._apart_floor

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
