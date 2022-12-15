from dao.ad_info_dao import AdInfoDAO
from dao.apartment_info_dao import ApartmentInfoDAO
from dao.building_info_dao import BuildingInfoDAO
from dao.rules_dao import RulesDAO
from dto.ad_info import *
from dto.apartment_info import *
from dto.building_info import *
from dto.rules import *


def price_parse(text: str) -> Prices:
    text = text.split(',')
    return Prices(int(text[0].replace('AMD: ', '')),
                  int(text[1].replace('USD: ', '')),
                  int(text[2].replace('RUB: ', '')))


class AdInfoConverter:
    @staticmethod
    def to_dao(ad_info: AdInfo) -> AdInfoDAO:
        return AdInfoDAO(image_links=ad_info.image_links,
                         created=ad_info.created,
                         updated=ad_info.updated,
                         prices=ad_info.prices.to_str(),
                         description=ad_info.description,
                         landlord_type=ad_info.landlord_type.value
                         )

    @staticmethod
    def to_dto(ad_info_dao: AdInfoDAO) -> AdInfo:
        return AdInfo(ad_info_dao.image_links.split(' '),
                      ad_info_dao.created,
                      ad_info_dao.updated,
                      price_parse(ad_info_dao.prices),
                      ad_info_dao.description,
                      LandLordType(ad_info_dao.landlord_type)
                      )


class ApartmentInfoConverter:
    @staticmethod
    def to_dao(apartment_info: ApartmentInfo) -> ApartmentInfoDAO:

        return ApartmentInfoDAO(address=apartment_info.address,
                                square=apartment_info.square,
                                room_number=apartment_info.room_number,
                                smartin_number=apartment_info.smartin_number,
                                height=apartment_info.height,
                                floor=apartment_info.floor,
                                has_balcony=apartment_info.has_balcony,
                                is_furnitured=apartment_info.is_furnitured,
                                renovation_type=apartment_info.renovation_type.value,
                                features=apartment_info.features,
                                household_features=apartment_info.household_features
                                )

    @staticmethod
    def to_dto(apartment_info_dao: ApartmentInfoDAO) -> ApartmentInfo:

        return ApartmentInfo(apartment_info_dao.address,
                             apartment_info_dao.square,
                             apartment_info_dao.room_number,
                             apartment_info_dao.smartin_number,
                             apartment_info_dao.height,
                             apartment_info_dao.floor,
                             apartment_info_dao.has_balcony,
                             apartment_info_dao.is_furnitured,
                             RenovationType(
                                 apartment_info_dao.renovation_type),
                             apartment_info_dao.features,
                             apartment_info_dao.household_features
                             )


class BuildingInfoConverter:
    @staticmethod
    def to_dao(building_info: BuildingInfo) -> BuildingInfoDAO:

        return BuildingInfoDAO(building_type=building_info.building_type.value,
                               is_new_building=building_info.is_new_building,
                               has_elevator=building_info.has_elevator,
                               floor_number=building_info.floor_number
                               )

    @staticmethod
    def to_dto(building_info_dao: BuildingInfoDAO) -> BuildingInfo:

        return BuildingInfo(BuildingType(building_info_dao.building_type),
                            building_info_dao.is_new_building,
                            building_info_dao.has_elevator,
                            building_info_dao.floor_number
                            )


class RulesConverter:
    @staticmethod
    def to_dao(rules: Rules) -> RulesDAO:

        return RulesDAO(apart_capacity=rules.apart_capacity,
                        is_kids_allowed=rules.is_kids_allowed.value,
                        is_animals_allowed=rules.is_animals_allowed.value,
                        utility_payments=rules.utility_payments,
                        has_prepayment=rules.has_prepayment
                        )

    @staticmethod
    def to_dto(rules_dao: RulesDAO) -> Rules:

        return Rules(rules_dao.apart_capacity,
                     rules_dao.is_kids_allowed,
                     Allowance(rules_dao.is_animals_allowed),
                     Allowance(rules_dao.utility_payments),
                     rules_dao.has_prepayment
                     )
