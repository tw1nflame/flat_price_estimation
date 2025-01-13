from bs4 import BeautifulSoup
import requests

import pandas as pd
import time


categories = {
    'Тип жилья': 'flat_type',
    'Общая площадь': 'all_square',
    'Жилая площадь': 'living_square',
    'Площадь кухни': 'kitchen_square',
    'Санузел': 'toilet',
    'Балкон/лоджия': 'balcony',
    'Ремонт': 'repair',
    'Год постройки': 'construction_year',
    'Строительная серия': 'construction_seria',
    'Мусоропровод': 'garbage',
    'Тип дома': 'building_type',
    'Тип перекрытий': 'type_of_floors',
    'Подъезды': 'entrances',
    'Отопление': 'heating',
    'Аварийность': 'accident_rate',
    'Высота потолков': 'height',
    'Отделка': 'finishing',
    'Парковка': 'parking',
    'Количество лифтов': 'count_of_elevators',
    'Газоснабжение': 'gas',
    'Вид из окон': 'view'
}

flats = []

with open('links.txt', 'r') as file:
    for line in file.readlines():
        flats.append(line)

parsed_info = []

new_keys = set()

for flat in flats:
    req = requests.get(flat)
    soup = BeautifulSoup(req.text, 'lxml')

    print(flat)
    print(soup.title)
    # id = int(flat.split('/')[-2])

    # try:
    #     num_rooms = soup.select(
    #         'div[data-name="OfferTitleNew"]')[0].contents[0].text
    # except:
    #     try:
    #         num_rooms = soup.select(
    #             'div[data-name="OfferTitleNew"]').contents[0].text
    #     except:
    #         print(flat)
    #         num_rooms = soup.select(
    #             'div[data-name="OfferTitleNew"]')
    # print(num_rooms)
    # divs = soup.select('div[data-name="OfferSummaryInfoItem"]')

    # price = int(soup.select(
    #     'div[data-testid="price-amount"]')[0].contents[0].text.replace('\xa0', '')[:-1])

    # info = {
    #     'id': id,
    #     'num_rooms': num_rooms,
    #     'price': price
    # }

    # for div in divs:
    #     key = div.contents[0].text
    #     value = div.contents[1].text

    #     # translate
    #     try:
    #         key = categories[key]
    #         info[key] = value
    #     except:
    #         new_keys.add(key)

    # parsed_info.append(info)

print(new_keys)

df = pd.DataFrame(parsed_info)
print(df.shape)
