from bs4 import BeautifulSoup as beauty
import cloudscraper

scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 

def ads_grabber():
    for i in range (1, 251):    
        url = f'https://list.am/ru/category/56/{i}/?pfreq=1&type=1&po=1'
        response = scraper.get(url).status_code
        if (response != 200):
            break
        info = scraper.get(url).text
        soup = beauty(info, "html.parser")
        hotLinks = soup.find_all('a', class_='h')
        for link in hotLinks:
            link = link.get('href')
            print(link + ' hot')
        basicLinks = soup.find(class_ = "gl").findChildren('a')
        for link in basicLinks:
            link = link.get('href')
            print(link + ' base')

def add_parse_info(data):
    key = data.findChild('div', class_ = 't').text
    value = data.findChild('div', class_ = 'i').text
    return (key, value)

def ads_parse(link):
    url = 'https://list.am/' + link
    info = scraper.get(url).text
    soup = beauty(info, 'html.parser')
    data = soup.find(id = 'pcontent')
    
    dataset = data.find_all('div', class_ = 'attr g')
    adsInfo = {}
    get_ads_photos(soup)
    adsInfo['Расположение'] = parse_location(soup)
    adsInfo['Даты'] = parse_dates(soup)
    adsInfo['Цены'] = parse_prices(soup)
    adsInfo['Описание'] = parse_ads_description(soup)
    adsInfo['Арендодатель'] = landlord_type_parse(soup)
    for i in dataset:
        for j in i:
            (key, value) = add_parse_info(j)
            adsInfo[key] = value
    return adsInfo

def parse_currency(text):
    if '$' in text:
        value = int(text[1:].split(" ")[0].replace(",", ""))
        return ("USD", value)
    elif '֏' in text:
        value = int(text.split(" ")[0].replace(",", ""))
        return ("AMD", value)
    elif '₽' in text:
        value = int(text.split(" ")[0].replace(",", ""))
        return ("RUB", value)
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
    spans_list = footer.select('span')
    result = {}
    for i in spans_list:
        if 'Размещено' in i.text:
            result['Дата размещения'] = i.text.split(' ')[1]
        if 'Обновлено' in i.text:
            result ['Обновления'] = i.text.split(' ')[1]
    return result

def parse_location(data):
    location_div = data.find('div', class_ = 'loc')
    location = location_div.findChild('a').text
    return location

def get_ads_photos(data):
    pics_div = data.find('div', class_ = 'p')
    pics_list = pics_div.findChildren('div')
    for pic_div in pics_list:
        print(pic_div.select_one('img').get('src'))
    return 0

list = ads_parse('ru/item/18563494')
for i in list.keys():
    print(i)
for i in list.values():
    print(i)
