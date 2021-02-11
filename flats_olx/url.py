from bs4 import BeautifulSoup
import requests

url = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/"

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')

jobs = soup.find_all('div', {'class': 'offer-wrapper'})

for job in jobs:
    title = job.find('strong').text

    print(title)
