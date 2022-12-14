from bs4 import BeautifulSoup as beauty
from model.ad_info import *
from model.ad_meta import AdMeta
from model.apartment_info import *
from model.building_info import *
from model.rules import *
import datetime


def get_key_value_pair(data) -> tuple:
    key = data.findChild('div', class_='t').text
    value = data.findChild('div', class_='i').text

    return (key, value)


def extract_attributes(data) -> tuple:
    dict = {}
    for attribute in data.findChildren('div', class_='c'):
        (key, value) = get_key_value_pair(attribute)
        dict[key] = value

    return dict


def parse_currency(text) -> tuple:
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


def parse_prices(data) -> Prices:
    result = {}

    price_span = data.find('span', class_='xprice')
    price_text = price_span.select_one('span').text
    cur, amount = parse_currency(price_text)
    result[cur] = amount

    for ps in price_span.findChild('div').select('span'):
        cur, amount = parse_currency(ps.text)
        result[cur] = amount

    assert result['USD']
    assert result['AMD']
    assert result['RUB']

    return Prices(result['AMD'], result['USD'], result['RUB'])


def parse_description(data) -> str:
    description = data.find('div', class_='body').text

    return description.replace('Переведено с армянского', '')


def parse_landlord_type(data) -> LandLordType:
    landlord_type = data.find('span', class_='clabel')

    if (landlord_type == None):
        return LandLordType.private
    else:
        return LandLordType.realtor


def parse_dates(data) -> date:
    footer = data.find('div', class_='footer')
    date_span_list = footer.select('span')
    created = 0
    updated = 0

    for date_span in date_span_list:
        if 'Размещено' in date_span.text:
            created = datetime.datetime.strptime(
                date_span.text.split(' ')[1].replace('.', '/'), '%d/%m/%Y')
        if 'Обновлено' in date_span.text:
            updated = datetime.datetime.strptime(
                date_span.text.split(' ')[1].replace('.', '/'), '%d/%m/%Y')

    return created, updated


def parse_address(data) -> str:
    location_div = data.find('div', class_='loc')
    location = location_div.findChild('a').text
    return location


def parse_images_list(data):  # work in progress
    pics_div = data.find('div', class_='p')
    pics_list = pics_div.findChildren('div')

    for pic_div in pics_list:
        print(pic_div.select_one('img').get('src'))

    return 0


def parse_building_info(attributes) -> BuildingInfo:
    building_type = BuildingType.from_str(attributes['Тип здания'])
    is_new = attributes['Новостройка'] == 'Да'
    has_elevator = attributes['Лифт'] == 'Есть'
    floor_number = int(attributes['Этажей в доме'])

    return BuildingInfo(building_type,
                        is_new,
                        has_elevator,
                        floor_number)


def parse_apartment_info(address, attributes) -> ApartmentInfo:
    square = int(attributes['Общая площадь'].split(' ')[0])
    room_number = int(attributes['Количество комнат'])
    smartin_number = int(attributes['Количество санузлов'])
    height = float(attributes['Высота потолков'].split(' ')[0])
    floor = int(attributes['Этаж'])
    has_balcony = attributes['Балкон'] != 'Нет'
    is_furnitured = attributes['Мебель'] != 'Нет'
    renovation_type = RenovationType.from_str(attributes['Ремонт'])
    features = attributes['Удобства']
    household_features = attributes['Бытовая техника']

    return ApartmentInfo(
        address,
        square,
        room_number,
        smartin_number,
        height,
        floor,
        has_balcony,
        is_furnitured,
        renovation_type,
        features,
        household_features)


def parse_ad_info(data) -> AdInfo:
    images_links = list
    dates = parse_dates(data)
    created = dates[0]
    updated = dates[1]
    prices = parse_prices(data)
    description = parse_description(data)
    landlord_type = parse_landlord_type(data)

    return AdInfo(images_links,
                  created,
                  updated,
                  prices,
                  description,
                  landlord_type)


def parse_rules(attributes) -> Rules:
    apart_capacity = int(attributes['Kоличество гостей'])
    is_kids_allowed = Allowance.from_str(attributes['Можно с детьми'])
    is_animals_allowed = Allowance.from_str(attributes['Можно с животными'])
    utility_payments = attributes['Коммунальные платежи']
    has_prepayment = attributes['Предоплата']

    return Rules(apart_capacity,
                 is_kids_allowed,
                 is_animals_allowed,
                 utility_payments,
                 has_prepayment)


def get_ad_content(scraper, link):
    url = 'https://list.am/' + link
    response = scraper.get(url)

    if (response.status_code != 200):
        print(response.status_code)
        return

    info = response.text
    soup = beauty(info, 'html.parser')
    data = soup.find(id='pcontent')

    attributes = extract_attributes(data)
    address = parse_address(data)
    ad_info = parse_ad_info(data)
    building_info = parse_building_info(attributes)
    apartment_info = parse_apartment_info(address, attributes)
    rules = parse_rules(attributes)
    return AdMeta(ad_info, apartment_info, building_info, rules)
