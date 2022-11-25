import BuildingType 

class BuildingInfo:
    def __init__(self, 
            building_type: BuildingType, 
            is_new_building: bool, 
            has_elevator: bool, 
            floor_number: int
    ):
        self._building_type = building_type
        self._is_new_building = is_new_building
        self._has_elevator = has_elevator
        self._floor_number = floor_number

    @property
    def building_type(self) -> BuildingType: 
        return self._building_type

    @property
    def is_new_building(self) -> bool:
        return self._is_new_building

    @property
    def has_elevator(self) -> bool:
        return self._has_elevator

    @property
    def floor_number(self) -> int:
        return self._floor_number
