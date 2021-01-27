# Extract all the URLs from one web page
from bs4 import BeautifulSoup
import requests

# the link of the web page
url = "https://boston.craigslist.org/search/sof"

# get the web page, create response object
response = requests.get(url)

# verify the response code is 200
# print(response)

#extract the source code of the web page
data = response.text
print(data)

# pass the source code to BeautifulSoup to create BeautifulSoup object for it
# parse HTML text with the help of HTML parser
soup = BeautifulSoup(data, 'html.parser')
# find_all method for extracting all the 'a' tags into a list
tags = soup.find_all('a')

for tag in tags:
    print(tag.get('href'))
