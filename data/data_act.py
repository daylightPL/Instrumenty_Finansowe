import json
import pandas as pd


#read data from json files and return values
def get_actual_value(valuable):

    #retunt actual gold value
    if valuable == 'gold':
        try:
            with open('./data_store/act_data_gold.json') as data_file:
                data = json.load(data_file)
            df = pd.DataFrame(data)
            val = df.iloc[0]['cena']
            return val
        except:
            print('Nie można pobrać danych o kursie złota!')
            return None

    #return value for selected currency
    else:
        try:
            with open('./data_store/act_data_curr.json') as data_file:
                data = json.load(data_file)
            df = pd.DataFrame(data)
            df = df.iloc[0]['rates']
            df = pd.DataFrame(df)
            val = df.loc[df.code == valuable, 'mid'].values[0]
            return val
        except:
            print('Nie można pobrać danych o kursie wybranej waluty!')
            return None

print(get_actual_value('EUR'))