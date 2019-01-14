import urllib.request
import datetime

#valuable = 'gold' if we try to check for gold, currency code for other
def download(valuable, start_date, end_date, filename = 'data'):
    url = "http://api.nbp.pl/api/"
    if valuable == 'gold':
        url = url + 'cenyzlota/' + start_date + '/' + end_date
    else:
        url = url + 'exchangerates/rates/A/' + valuable + '/' + start_date + '/' + end_date
    url =  url + '?format=json'
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            data = data.decode("utf-8")
    except urllib.request.HTTPError as err:
        print("HTTP Error: {0}".format(err))
    except Exception as err:
        with open("error.log", 'a') as fh:
            fh.write("{0}: {1}\n".format(datetime.datetime.now(), str(err)))
    filename = './data/data_store/{0}.json'.format(filename)
    with open(filename, 'w+') as file:
        file.write(str(data))
    return data

def download_last_year_gold():
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(364)
    try:
        download('gold',str(start_date),str(end_date),'year_data_gold')
    except:
        print('Błąd przy pobieraniu kursu złota za ostatni rok!')


def download_last_year_curr(currency):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(364)
    try:
        download(currency,str(start_date),str(end_date),'year_data_curr')
    except:
        print('Błąd przy pobieraniu kursu waluty: {0} za ostatni rok!'.format(currency))



#this function save actual rate for gold to file act_data_gold
def download_actual_gold():
    url = 'http://api.nbp.pl/api/cenyzlota'
    url = url + '?format=json'
    with urllib.request.urlopen(url) as response:
        data = response.read()
    data = data.decode("utf-8")
    filename = './data/data_store/act_data_gold.json'
    with open(filename, 'w+') as file:
        file.write(str(data))


#this function save actual rates for currencies to file act_data_curr
def download_actual_currency():
    url = 'http://api.nbp.pl/api/exchangerates/tables/A/'
    url =  url + '?format=json'
    with urllib.request.urlopen(url) as response:
        data = response.read()
    data = data.decode("utf-8")
    filename = './data/data_store/act_data_curr.json'
    with open(filename, 'w+') as file:
        file.write(str(data))




print(download('USD','2018-01-07','2019-01-07'))
#print(download_actual_gold())
#print(download_actual_currency())
download_last_year_gold()
download_last_year_curr('GBP')
