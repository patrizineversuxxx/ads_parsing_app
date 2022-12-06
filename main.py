import cloudscraper
from grabber import *
from data_parser import *

scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
ads_links = Grabber.grab(scraper)

ad_meta = get_ad_content(scraper, '/ru/item/18665272')
pass
