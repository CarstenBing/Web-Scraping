import requests
# from prettyprinter import pprint
from bs4 import BeautifulSoup

URL = 'https://www.finn.no/job/fulltime/search.html?filters=&occupation=0.20&occupation=1.20.10000'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

job_elems = results.find_all('section', class_= 'ads ads--list')

for job_elem in job_elems:
    # print(job_elem, end = '\n'*2)
    title_elem = job_elem.find('div', class_='ads__unit__content__keys')
    company_elem = job_elem.find('div', class_='ads__unit__content__list')
    location_elem = job_elem.find('div', class_='ads__unit__link')
    if None in (title_elem, company_elem, location_elem):
        
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()