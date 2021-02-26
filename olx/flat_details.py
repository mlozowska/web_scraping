from bs4 import BeautifulSoup
from requests import get

url = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/"


def parse_price(price):
    return price.replace(' ', '').replace('zl', '').replace(',', '.')


page = get(url)
bs = BeautifulSoup(page.content, 'html.parser')

for offer in bs.find_all('div', class_='offer-wrapper'):
    footer = offer.find('td', class_='bottom-cell')
    location = footer.find('small', class_='breadcrumb').get_text()
    title = offer.find('strong').get_text().strip()
    price = offer.find('p', class_='price').get_text().strip()

    print(location, title, price)
