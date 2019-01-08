import urllib.request

#valuable = 'gold' if we try to check for gold, currency code for other
def download(valuable, start_date, end_date):
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
    filename = './data_store/data.json'
    with open(filename, 'w+') as file:
        file.write(str(data))
    return data

def download_actual_gold():
    url = 'http://api.nbp.pl/api/cenyzlota'
    url = url + '?format=json'
    with urllib.request.urlopen(url) as response:
        data = response.read()
    data = data.decode("utf-8")
    filename = './data_store/act_data_gold.json'
    with open(filename, 'w+') as file:
        file.write(str(data))
    return data

def download_actual_currency():
    url = 'http://api.nbp.pl/api/exchangerates/tables/A/'
    url =  url + '?format=json'
    with urllib.request.urlopen(url) as response:
        data = response.read()
    data = data.decode("utf-8")
    filename = './data_store/act_data_curr.json'
    with open(filename, 'w+') as file:
        file.write(str(data))
    return data



print(download('USD','2018-01-07','2019-01-07'))
print(download_actual_gold())
print(download_actual_currency())
