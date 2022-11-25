import RenovationType

class ApartmentInfo:
    def __init__(self, 
            square : float, 
            room_number : int, 
            smartins_count : int, 
            height : float, 
            floor : int, 
            has_balcony : bool, 
            is_furnitured : bool, 
            renovation_type : RenovationType, 
            features : str, 
            household_features : str
    ):
        self._square = square
        self._room_number = room_number
        self._smartins_count = smartins_count
        self._height = height
        self._floor = floor
        self._has_balcony = has_balcony
        self._is_furnitured = is_furnitured
        self._renovation_type = renovation_type
        self._features = features
        self._household_features = household_features

    @property
    def square(self) -> float:
        return self._square

    @property
    def room_number(self) -> int:
        return self._room_number

    @property
    def smartins_count(self) -> int:
        return self._smartins_count

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
