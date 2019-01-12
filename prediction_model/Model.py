from sklearn.linear_model import LinearRegression
import numpy
import time



# Todo 1.Train model
#Obrobka X
X = ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05', '2019-01-06', '2019-01-07']
#Format daty ktora trzeba przeksztalcic p = '%Y-%m-%d'
#Petla przeksztalcajaca X
for i in range(0, len(X)):
    #print(X[i])
    X[i] = int(time.mktime(time.strptime(X[i],'%Y-%m-%d')))
    #print(X[i])

X = numpy.array(X).reshape(-1, 1)

#obrobka wartosci y
y = [1,2,3,4,5,6,7]
y = numpy.array(y)

print(X)
print(y)

#Uczenie  modelu
model = LinearRegression()
model.fit(X, y)

# Todo 2. Predict using trained model.
new = ['2019-02-09']
Xnew = int(time.mktime(time.strptime(new[0],'%Y-%m-%d')))

Xnew = numpy.array(Xnew).reshape(-1, 1)
ynew = model.predict(Xnew)

# Todo 3. Return value
print("Cena w " + str(new) + " wynosi: " + str(ynew))