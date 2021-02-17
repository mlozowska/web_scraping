from bs4 import BeautifulSoup
from requests import get

url = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/"

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')

jobs = soup.find_all('div', {'class': 'content'})

for job in jobs:
    title = job.find('strong')
    # location = job.find('span', {'data_icon':'location-filled'}).text
    link = job.find('span').get('href')
    date = job.find('span', {'data-icon':'clock'}).text

    print(title, link)

