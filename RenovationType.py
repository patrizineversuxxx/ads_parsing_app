from enum import Enum 

class RenovationType(Enum):
    WithoutRenovation = 'Без ремонта'
    PartlyRenovated = 'Частичный ремонт'
    Redecorated = 'Косметический ремонт'
    EuroRenovation = 'Евроремонт'
    DesignersRenovation = 'Дизайнерский ремонт'
    MajorOverhauled = 'Капитальный ремонт'
