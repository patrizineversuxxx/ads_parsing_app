from bs4 import BeautifulSoup as beauty
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
