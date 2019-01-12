import json
import pandas as pd
from pandas.io.json import json_normalize

csv_file = './data_store/selected_data.csv'

#read data from json file and save to csv
def to_csv():
    with open('./data_store/data.json') as data_file:
        data = json.load(data_file)

    df = json_normalize(data, 'rates', ['code'])
    df = df.drop('no', axis=1)
    df.to_csv(csv_file)

#choose currency data based on selection - to do
def select():
    df = pd.read_csv(csv_file)
    print(df)

#to_csv()
select()