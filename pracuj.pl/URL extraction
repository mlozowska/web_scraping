from bs4 import BeautifulSoup
import requests

url = "https://www.pracuj.pl/praca/tester%20oprogramowania;kw?rd=30"

response = requests.get(url)
# print(response)
data = response.text
# print(data)
soup = BeautifulSoup(data, 'html.parser')
tags = soup.find_all('a')

for tag in tags:
    print(tag.get('href'))
