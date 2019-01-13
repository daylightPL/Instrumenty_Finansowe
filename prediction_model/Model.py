from sklearn.linear_model import LinearRegression
import numpy
import time
import pandas
import datetime
import dateutil.relativedelta

def Prediction (date_list_x, value_list_y, date_for_prediction):
    #Obrobka dat (Lista X)
    train_list_x = date_list_x
    train_list_y = value_list_y
    for i in range(0, len(train_list_x)):
        train_list_x[i] = int(time.mktime(time.strptime(train_list_x[i], '%Y-%m-%d')))


    train_list_x = numpy.array(train_list_x).reshape(-1, 1)

    #Obrobka wartosci (Lista y)
    train_list_y = numpy.array(train_list_y)

    #Uczenie Modelu
    model = LinearRegression()
    model.fit(train_list_x, train_list_y)

    #Obrobka daty dla predykcji
    date_for_prediction = int(time.mktime(time.strptime(date_for_prediction[0], '%Y-%m-%d')))
    date_for_prediction = numpy.array(date_for_prediction).reshape(-1, 1)

    #Predykcja
    predicted_value = model.predict(date_for_prediction)

    #Zwrocenie wartosci
    return float(predicted_value)


def Select_Data(duration, date_today):
    #Switch zaleznie od zakresu danych
    if duration == 'year':
        #Wczytaj dane z pliku
        csv_file = '../data/data_store/selected_data.csv'
        df = pandas.read_csv(csv_file)
        #Wykorzystuje wszystko wczytane - nie ma potrzeby filtracji
        #Utworz listy i je zwroc
        x = df.effectiveDate.tolist()
        y = df.mid.tolist()
        return x, y
    elif duration == 'month':
        #Wczytaj dane z pliku
        csv_file = '../data/data_store/selected_data.csv'
        df = pandas.read_csv(csv_file)
        #Filtracja
        targettime = datetime.datetime.strptime(date_today, '%Y-%m-%d')
        targettime = targettime - dateutil.relativedelta.relativedelta(months=1)
        targettime = str(targettime)
        #print(date_today)
        #print(targettime)
        df = df[(df.effectiveDate > targettime)]
        #print(df)
        #Utworz listy i je zwroc
        x = df.effectiveDate.tolist()
        y = df.mid.tolist()
        return x, y
    elif duration == 'week':
        #Wczytaj dane z pliku
        csv_file = '../data/data_store/selected_data.csv'
        df = pandas.read_csv(csv_file)
        #Filtracja
        targettime = datetime.datetime.strptime(date_today, '%Y-%m-%d')
        targettime = targettime - dateutil.relativedelta.relativedelta(days=7)
        targettime = str(targettime)
        #print(date_today)
        #print(targettime)
        df = df[(df.effectiveDate > targettime)]
        #print(df)
        #Utworz listy i je zwroc
        x = df.effectiveDate.tolist()
        y = df.mid.tolist()
        return x, y

#Ponizej przykład zastosowania obu funkcji
#Funkcja zwraca dwuwymiarową listę - trzeba rozbić na x i y
#data = Select_Data('year', '2018-01-13')
#data = Select_Data('month', '2019-01-13')
data = Select_Data('week', '2019-01-13')
x = data[0]
y = data[1]
predict_for = ['2019-01-13']
prediction = Prediction(x, y, predict_for)
print(predict_for)
print(prediction)


#Ponizej przykład zastosowania samej funkcji predict
#Inicjalizacja danych
#x = ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05']
#print(x)
#y = [1, 2, 3, 4, 5]
#predict_for = ['2019-01-30']

#Wywolanie funkcji
#prediction = Prediction(x, y, predict_for)

#Wyswietlenie danych i wyniku
#print(x)
#print(y)
#print(predict_for)
#print(prediction)


