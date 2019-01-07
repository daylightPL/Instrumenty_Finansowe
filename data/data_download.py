import urllib
import xml.etree.ElementTree as ET
import os


def download(valuable, start_date, end_date):
    url = "http://api.nbp.pl/api/"
    if valuable == 'gold':
        url = url + 'cenyzlota/' + start_date + '/' + end_date
    else:
        url = url + 'exchangerates/rates/A/' + valuable + '/' + start_date + '/' + end_date
    url =  url + '?format=xml'
    with urllib.request.urlopen(url) as response:
        data = response.read()
    dirname = os.path.dirname(__file__)
    filename = dirname + '/data_store/data.xml'
    with open(filename, 'w+') as file:
        file.write(str(data))
        #TODO Plik nie tworzy drzewa. Czy to jest ok?
    return data

def choose_data(start_date):
    tree = ET.parse('country_data.xml')
    root = tree.getroot()
    return root

print(download('USD','2018-12-01','2018-12-05'))
