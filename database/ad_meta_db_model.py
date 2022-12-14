from model.ad_info import *
from model.apartment_info import *
from model.building_info import *
from model.rules import *


class AdMeta:
    def __init__(self,
                 ad_info: AdInfo,
                 apartment_info: ApartmentInfo,
                 building_info: BuildingInfo,
                 rules: Rules):
        self._ad_info = ad_info
        self._apartment_info = apartment_info
        self._building_info = building_info
        self._rules = rules

    @property
    def ad_info(self) -> AdInfo:
        return self._ad_info

    @property
    def apartment_info(self) -> ApartmentInfo:
        return self._apartment_info

    @property
    def building_info(self):
        return self._building_info

    @property
    def rules(self):
        return self._rules
