from bs4 import BeautifulSoup as beauty
from building_info import *
from apartment_info import *
from ad_info import *
from datetime import date
import cloudscraper

scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 

def extract_attributes(data) -> dict:
    dict = {}
    for attribute in data.findChildren('div', class_= 'c'):
        (key, value) = add_parse_info(attribute)
        dict[key] = value
    return dict

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

    return Prices(result['AMD'], result['USD'], result['RUB'])

def parse_ads_description(data):
    description = data.find('div', class_ = 'body').text
    
    return description.replace('Переведено с армянского','')

def landlord_type_parse(data):
    landlord_type = data.find('span', class_ = 'clabel')

    if (landlord_type == None):
        return LandLordType('Частник')
    else:
        return LandLordType('Агентство')

def parse_datetime(string) -> date:
    string = string.split('.')
    year = int(string[2])
    month = int(string[1])
    day = int(string[0])

    return date(year, month, day)

def parse_dates(data):
    footer = data.find('div', class_ = 'footer')
    date_span_list = footer.select('span')
    created = 0
    updated = 0

    for date_span in date_span_list:
        if 'Размещено' in date_span.text:
            created = parse_datetime(date_span.text.split(' ')[1])
        if 'Обновлено' in date_span.text:
            updated = parse_datetime(date_span.text.split(' ')[1])

    return created, updated

def parse_address(data):
    location_div = data.find('div', class_ = 'loc')
    location = location_div.findChild('a').text
    return location

def get_ads_photos(data): #work in progress
    pics_div = data.find('div', class_ = 'p')
    pics_list = pics_div.findChildren('div')

    for pic_div in pics_list:
        print(pic_div.select_one('img').get('src'))
    return 0


def parse_building_info(data) -> BuildingInfo:
    dict = extract_attributes(data)

    building_type = BuildingType(dict['Тип здания'])
    is_new = dict['Новостройка'] == 'Да'
    has_elevator = dict['Лифт'] == 'Есть'
    floor_number = int(dict['Этажей в доме'])
    
    return BuildingInfo(building_type, is_new, has_elevator, floor_number)

def parse_apartment_info(data) -> ApartmentInfo:
    attributes = extract_attributes(data)

    square = int(attributes['Общая площадь'].split(' ')[0])
    room_number = int(attributes['Количество комнат']) 
    smartin_number = int(attributes['Количество санузлов'])
    height = float(attributes['Высота потолков'].split(' ')[0])
    floor = int(attributes['Этаж']) 
    has_balcony = attributes['Балкон'] != 'Нет'
    is_furnitured = attributes['Мебель'] != 'Нет'
    renovation_type = RenovationType(attributes['Ремонт'])
    features = attributes['Удобства']
    household_features = attributes['Бытовая техника']

    return ApartmentInfo(square, room_number, smartin_number, 
                         height, floor, has_balcony, is_furnitured, 
                        renovation_type, features, household_features)

def parse_ad_into(data):
    images_links = list
    address = parse_address(data)
    created = parse_dates(data)[0]
    updated = parse_dates(data)[1]
    prices = parse_prices(data)
    description = parse_ads_description(data)
    landlord_type = landlord_type_parse(data)

    return AdInfo(images_links, address, created, 
            updated, prices, description, 
            landlord_type)

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