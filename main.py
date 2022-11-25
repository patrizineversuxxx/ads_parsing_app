from bs4 import BeautifulSoup as beauty
from enum import Enum
import cloudscraper

scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 

def ads_grabber():
    for page_number in range (1, 251):    
        url = f'https://list.am/ru/category/56/{page_number}/?pfreq=1&type=1&po=1'
        response = scraper.get(url)
        if (response.status_code != 200):
            print (response.status_code)
            break
        info = response.text
        soup = beauty(info, 'html.parser')
        hotLinks = soup.find_all('a', class_='h')
        for link in hotLinks:
            link = link.get('href')
            print(link + ' hot')
        basicLinks = soup.find(class_ = 'gl').findChildren('a')
        for link in basicLinks:
            link = link.get('href')
            print(link + ' base')

def add_parse_info(data):
    key = data.findChild('div', class_ = 't').text
    value = data.findChild('div', class_ = 'i').text
    return (key, value)

def ads_parse(link):
    url = 'https://list.am/' + link
    response = scraper.get(url)
    if (response.status_code != 200):
        print (response.status_code)
        return
    info = response.text
    soup = beauty(info, 'html.parser')
    data = soup.find(id = 'pcontent')
    
    ad_property_set = data.find_all('div', class_ = 'attr g')
    ad_property_dict = {}
    get_ads_photos(soup)
    ad_property_dict['Расположение'] = parse_location(soup)
    ad_property_dict['Даты'] = parse_dates(soup)
    ad_property_dict['Цены'] = parse_prices(soup)
    ad_property_dict['Описание'] = parse_ads_description(soup)
    ad_property_dict['Арендодатель'] = landlord_type_parse(soup)
    for ad_property in ad_property_set:
        for ad_property_content in ad_property:
            (key, value) = add_parse_info(ad_property_content)
            ad_property_dict[key] = value
    return ad_property_dict

def parse_currency(text):
    if '$' in text:
        value = int(text[1:].split(' ')[0].replace(',', ''))
        return ('USD', value)
    elif '֏' in text:
        value = int(text.split(' ')[0].replace(',', ''))
        return ('AMD', value)
    elif '₽' in text:
        value = int(text.split(' ')[0].replace(',', ''))
        return ('RUB', value)
    else:
        raise Exception

def parse_prices(data):
    result = {}

    price_span = data.find('span', class_= 'xprice')
    price_text = price_span.select_one('span').text
    cur, amount = parse_currency(price_text)
    result[cur] = amount

    for ps in price_span.findChild('div').select('span'):
        cur, amount = parse_currency(ps.text)
        result[cur] = amount

    assert result['USD']
    assert result['AMD']
    assert result['RUB']

    return result

def parse_ads_description(data):
    description = data.find('div', class_ = 'body').text
    return description

def landlord_type_parse(data):
    landlord_type = data.find('span', class_ = 'clabel')
    if (landlord_type == None):
        return 'Частное лицо'
    else:
        return 'Риэлтор'

def parse_dates(data):
    footer = data.find('div', class_ = 'footer')
    date_span_list = footer.select('span')
    dates = {}
    for date_span in date_span_list:
        if 'Размещено' in date_span.text:
            dates['Дата размещения'] = date_span.text.split(' ')[1]
        if 'Обновлено' in date_span.text:
            dates ['Обновления'] = date_span.text.split(' ')[1]
    return dates

def parse_location(data):
    location_div = data.find('div', class_ = 'loc')
    location = location_div.findChild('a').text
    return location

def get_ads_photos(data): #work in progress
    pics_div = data.find('div', class_ = 'p')
    pics_list = pics_div.findChildren('div')
    for pic_div in pics_list:
        print(pic_div.select_one('img').get('src'))
    return 0

list = ads_parse('ru/item/18563494')
for key in list.keys():
    print(key)
for value in list.values():
    print(value)

class BuildingType(Enum):  
    Monolith = 'Монолит'
    Stone = 'Каменное'
    Panel = 'Панельное'
    Cassette = 'Кассетное'
    Wooden = 'Деревянное'
    Brick = 'Кирпичное'

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

class RenovationType(Enum):
    WithoutRenovation = 'Без ремонта'
    PartlyRenovated = 'Частичный ремонт'
    Redecorated = 'Косметический ремонт'
    EuroRenovation = 'Евроремонт'
    DesignersRenovation = 'Дизайнерский ремонт'
    MajorOverhauled = 'Капитальный ремонт'

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
