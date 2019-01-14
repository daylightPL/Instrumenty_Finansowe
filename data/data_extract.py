import json
import pandas as pd
from pandas.io.json import json_normalize


#read data from json file and save to csv
def to_csv(valuable):

    #year data for gold
    if valuable == 'gold':
        try:
            with open('./data/data_store/year_data_gold.json') as data_file:
                data = json.load(data_file)
            df = pd.DataFrame(data)
            df = df[['data', 'cena']]
        except:
            print('Błąd przy odczycie danych dla kursu złota!')
            return None

    #year data for selected currency
    else:
        try:
            with open('./data/data_store/year_data_curr.json') as data_file:
                data = json.load(data_file)
            df = json_normalize(data, 'rates', ['code'])
            df = df.drop(['no', 'code'], axis=1)
            df = df.rename(index=str, columns={'effectiveDate': 'data', 'mid': 'cena'})
        except:
            print('Błąd przy odczycie danych dla kursu wybranej waluty!')
            return None

    #save in csv file
    try:
        with open('./data/data_store/selected_data.csv', 'w') as csv:
            df.to_csv(csv)
    except:
        print('Błąd przy zapisie pliku')


to_csv('gold')
