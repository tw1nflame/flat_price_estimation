from bs4 import BeautifulSoup
import requests
import pandas as pd
import pickle
import tqdm


flats = pd.read_csv('data/flats_final_with_cian_id.csv')
flats = flats.drop(['Unnamed: 0'], axis=1)

years = []
status = []

types = {
    'Вторичка': 1,
    'Новостройка': 0
}

failed_flats = []

for flat in tqdm.tqdm(flats.iloc, total=len(flats)):

    link = f'https://spb.cian.ru/sale/flat/{int(flat['cian_id'])}/'

    try:
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'lxml')

        if len(soup.select('div[data-name="ObjectFactoidsItem"] span')) == 0:
            print(soup.title)
            raise Exception('Nasrano')

        for obj in soup.select('div[data-name="ObjectFactoidsItem"] span'):
            if obj.text == 'Год постройки' or obj.text == 'Год сдачи':
                parent = obj.parent
                year = parent.contents[1].text
                years.append(year)

        for obj in soup.select('div[data-name="OfferSummaryInfoItem"] p'):
            if obj.text == 'Тип жилья':
                parent = obj.parent
                type_f = types[parent.contents[1].text]
                status.append(type_f)
                break
    except:
        print('поели говна')
        with open('data/years.pkl', 'wb') as file:
            pickle.dump(years, file)
        with open('data/status.pkl', 'wb') as file:
            pickle.dump(status, file)
        failed_flats.append(flat['cian_id'])

with open('data/years_pobeda.pkl', 'wb') as file:
    pickle.dump(years, file)
with open('data/status_pobeda.pkl', 'wb') as file:
    pickle.dump(status, file)
with open('data/flats_failed.pkl', 'wb') as file:
    pickle.dump(failed_flats, file)
