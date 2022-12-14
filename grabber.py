from bs4 import BeautifulSoup as beauty


class Grabber:
    def grab(scraper) -> list:
        links = []
        for page_number in range(1, 2):
            url = f'https://list.am/ru/category/56/{page_number}/?pfreq=1&type=1&po=1'
            response = scraper.get(url)
            if (response.status_code != 200):
                print(response.status_code)
                break
            info = response.text
            soup = beauty(info, 'html.parser')
            basicLinks = soup.find(class_='gl').findChildren('a')
            for link in basicLinks:
                link = link.get('href')
                links.append(link)
        return links
