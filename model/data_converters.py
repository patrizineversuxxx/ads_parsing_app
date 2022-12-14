from dao.rules_dao import *
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
