import cloudscraper
from grabber import *
from data_parser import *
from model import data_converters
from model.dao.ad_meta_dao import AdMetaDAO
from model.dao.ad_info_dao import AdInfoDAO
from model.dao.apartment_info_dao import ApartmentInfoDAO
from model.dao.building_info_dao import BuildingInfoDAO
from model.dao.rules_dao import RulesDAO

AdMetaDAO.drop_table()
AdInfoDAO.drop_table()
ApartmentInfoDAO.drop_table()
BuildingInfoDAO.drop_table()
RulesDAO.drop_table()


AdInfoDAO.create_table()
ApartmentInfoDAO.create_table()
BuildingInfoDAO.create_table()
RulesDAO.create_table()
AdMetaDAO.create_table()

scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
ads_links = Grabber.grab(scraper)

for ad_link in ads_links:
    ad_meta_dto = get_ad_content(scraper, ad_link)
    ad_info_dao = data_converters.AdInfoConverter.to_dao(ad_meta_dto.ad_info)
    apartment_info_dao = data_converters.ApartmentInfoConverter.to_dao(
        ad_meta_dto.apartment_info)
    building_info_dao = data_converters.BuildingInfoConverter.to_dao(
        ad_meta_dto.building_info)
    rules_dao = data_converters.RulesConverter.to_dao(ad_meta_dto.rules)
    ad_info_dao.save()
    apartment_info_dao.save()
    building_info_dao.save()
    rules_dao.save()
    ad_meta_dao = AdMetaDAO(url=ad_link,
                            ad_info_id=ad_info_dao.get_id(),
                            apartment_info_id=apartment_info_dao.get_id(),
                            building_info_id=building_info_dao.get_id(),
                            rules_id=rules_dao.get_id())
    ad_meta_dao.save()

pass
