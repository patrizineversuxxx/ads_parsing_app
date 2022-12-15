from dao.ad_info_dao import AdInfoDAO
from dao.apartment_info_dao import ApartmentInfoDAO
from dao.building_info_dao import BuildingInfoDAO
from dao.rules_dao import RulesDAO
from dto.ad_info import *
from dto.apartment_info import *
from dto.building_info import *
from dto.rules import *
from dao.dbclass import db


class RulesConverter:
    @staticmethod
    def to_dao(rules: Rules) -> RulesDAO:

        return RulesDAO(apart_capacity=rules.apart_capacity,
                        is_kids_allowed=rules.is_kids_allowed,
                        is_animals_allowed=rules.is_animals_allowed,
                        utility_payments=rules.utility_payments,
                        has_prepayment=rules.has_prepayment)

    @staticmethod
    def to_dto(rules_dao: RulesDAO) -> Rules:

        return Rules(rules_dao.apart_capacity,
                     rules_dao.is_kids_allowed,
                     rules_dao.is_animals_allowed,
                     rules_dao.utility_payments,
                     rules_dao.has_prepayment
                     )


class BuildingInfoConverter:
    @staticmethod
    def to_dao(building_info: BuildingInfo) -> BuildingInfoDAO:
        building_info = BuildingInfo(BuildingType.Brick, True, False, 4)

        return BuildingInfoDAO(building_type=building_info.building_type,
                               is_new_building=building_info.is_new_building,
                               has_elevator=building_info.has_elevator,
                               floor_number=building_info.floor_number
                               )

    @staticmethod
    def to_dto(building_info_dao: BuildingInfoDAO) -> BuildingInfo:
        building_info_dao = BuildingInfoDAO(building_type=3,
                                            is_new_building=True,
                                            has_elevator=True,
                                            floor_number=113)
        return BuildingInfo(building_info_dao.building_type,
                            building_info_dao.is_new_building,
                            building_info_dao.has_elevator,
                            building_info_dao.floor_number
                            )

