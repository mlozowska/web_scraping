from bs4 import BeautifulSoup
import requests

url = "https://boston.craigslist.org/search/sof"

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data,'html.parser')

jobs = soup.find_all('div',{'class':'result-info'})


for job in jobs:
    title = job.find('a',{'class':'result-title'}).text
    location_tag = job.find('span',{'class':'result-hood'})
    # added [2:-1] to remove the brackets, some job positions do not have location -> added loop
    location = location_tag.text[2:-1] if location_tag else "N/A"
    dates = job.find('time',{'class':'result-date'}).text
    link = job.find('a',{'class':'result-title'}).get('href')
    job_response = requests.get(link)
    job_data = job_response.text
    job_soup = BeautifulSoup(job_data, 'html.parser')
    job_description = job_soup.find('section', {'id':'postingbody'}).text
    job_attributes_tag = job_soup.find('p', {'class': 'attrgroup'})
    job_attributes = job_attributes_tag.text if job_attributes_tag else 'N/A'
    print("Job Title:", title, "\nLocation:", location, "\nDates:", dates, "\nLink:",
          link, "\n", job_attributes, "\nJob Description:", job_description)


