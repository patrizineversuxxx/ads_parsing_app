import cloudscraper
from ads_grabber import *
from data_parser import *

scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
ads_links = Grabber.ads_grabber(scraper)

data = get_ad_content(scraper, '/ru/item/18599392')
ad_info = data[0]
building_info = data[1]
apartment_info = data[2]
print(0)