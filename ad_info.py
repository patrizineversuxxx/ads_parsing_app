from enum import Enum
import datetime

class LandLordType(Enum):
    realtor = "Агентство"
    private = "Частное"

class Prices:
    def __init__(self, amd : int, usd : int, rub : int):
            self._amd = amd
            self._usd = usd
            self._rub = rub

    @property
    def amd(self) -> int:
        return self._amd

    @property
    def usd(self) -> int:
        return self._usd

    @property
    def rub(self) -> int:
        return self._rub


class AdInfo:
    def __init__(self,
            image_links : list,
            address : str, 
            created : datetime,
            updated : datetime,
            prices : Prices, 
            description : str, 
            landlord_type : LandLordType         
    ):
        self._image_links = image_links
        self._address = address
        self._created = created
        self._updated = updated
        self._prices = prices
        self._description = description
        self._landlord_type = landlord_type

    @property
    def image_links(self) -> list:
        return self._image_links

    @property
    def address(self) -> str:
        return self._address

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def updated(self) -> datetime:
        return self._updated

    @property
    def prices(self) -> Prices:
        return self._prices

    @property
    def description(self) -> str:
        return self._description

    @property
    def landlord_type(self) -> LandLordType:
        return self._landlord_type