import cloudscraper
from grabber import *
from data_parser import *

scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
#ads_links = Grabber.grab(scraper)

data = get_ad_content(scraper, '/ru/item/18665272')
ad_info = data[0]
building_info = data[1]
apartment_info = data[2]
rules = data[3]
pass
