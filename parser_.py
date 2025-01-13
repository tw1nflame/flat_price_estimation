from bs4 import BeautifulSoup
import requests

url = 'https://spb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=2&room1=1&room2=1&room3=1&room4=1&room9=1'

req = requests.get(url)

soup = BeautifulSoup(req.text, 'lxml')

flats = set()

for a in soup.select("a"):
    if 'href' in a.attrs.keys():
        link = a.attrs['href']
        if 'https://spb.cian.ru/sale/flat' in link:
            flats.add(link)

with open('links.txt', 'w') as file:
    for flat in flats:
        file.write(flat + '\n')
