import json
import pandas as pd


# return actual values
def get_actual_value(valuable, df):
    # get data from file
    #df = read_act_file(valuable)
    try:
        # check value for gold
        if valuable == 'gold':
            val = df.iloc[0]['cena']
        # check value for selected currency
        else:
            df = df.iloc[0]['rates']
            df = pd.DataFrame(df)
            val = df.loc[df.code == valuable, 'mid'].values[0]
        return val
    except:
        print('Nie można uzyskać informacji o aktualnym kursie!')
        return 'Brak danych'


# return actual date
def get_actual_date(valuable, df):
    # get data from file
    #df = read_act_file(valuable)
    try:
        # check date in file for gold
        if valuable == 'gold':
            date_act = df.iloc[0]['data']
        # check date in file for selected currency
        else:
            date_act = df.loc[0]['effectiveDate']
        return date_act
    except:
        print('Nie można uzyskać informacji o dniu aktualizacji kursu!')
        return 'Brak danych'


# read data from json files for actual data
def read_act_file(valuable):
    # read gold file
    if valuable == 'gold':
        try:
            with open('./data/data_store/act_data_gold.json') as data_file:
                data = json.load(data_file)
        except:
            print('Nie można pobrać danych o kursie złota!')
            return None
    else:
        # read currency file
        try:
            with open('./data/data_store/act_data_curr.json') as data_file:
                data = json.load(data_file)
        except:
            print('Nie można pobrać danych o kursie wybranej waluty!')
            return None
    # returns data from json file
    df = pd.DataFrame(data)
    return df

"""
Test outputs
print(read_act_file('EUR'))
print(get_actual_value('EUR', read_act_file('EUR')))
print(get_actual_date('EUR', read_act_file('EUR')))
print(get_actual_value('gold', read_act_file('gold')))
print(get_actual_date('gold', read_act_file('gold')))
"""
