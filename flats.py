from bs4 import BeautifulSoup
from requests import get
import sqlite3

# the function removes polish currency, extra spaces, changes string to float
def parse_price(price):
    return float(price.replace(' ', '').replace('zł', '').replace(',', '.'))

def parse_page(number):
    print(f'This is page {number}')
    page = get(f'{url}&page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')
    for offer in bs.find_all('div', class_='offer-wrapper'):
        footer = offer.find('td', class_='bottom-cell')
        location = footer.find('small', class_='breadcrumb').get_text().strip()
        title = offer.find('strong').get_text().strip()
        price = parse_price(offer.find('p', class_='price').get_text().strip())
        link = offer.find('a', class_='marginright5').get('href')

        cursor.execute('INSERT INTO offers VALUES (?,?,?)', (title, price, location))
        db.commit()

url = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/?search%5Bfilter_enum_rooms%5D%5B0%5D=two"


db = sqlite3.connect('data.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE offers (name TEXT, price REAL, city TEXT)''')

for page in range(1, 31):
    parse_page(page)

parse_page()
db.close()

