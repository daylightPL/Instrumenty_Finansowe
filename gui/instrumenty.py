from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

app = QtWidgets.QApplication([])
dlg = uic.loadUi("instrumenty.ui")

def show_message(title='Test', message='Test'):
    QMessageBox.information(None, title, message)

def pobierz_dane():
    show_message('Info', "Dane zostały pobrane")

def aktualny():
    dlg.lineEdit.setText(waluty[dlg.comboBox.currentText()])
    dlg.lineEdit_3.setText('tu trzeba podpiąć aktualną datę')


waluty = {'złoto': 'gold', 'euro': 'EUR', 'funt szterling': 'GBP', 'dolar amerykański': 'USD', 'korona czeska': 'CZK', 'peso meksykańskie': 'MXN', 'rubel rosyjski': 'RUB'}


def forecast(currency, period, date):
    wynik = str(currency) + str(period) + str(date)
    return wynik


def display_forecast():

    dlg.lineEdit_2.setText(forecast(dlg.comboBox.currentText(), dlg.comboBox_2.currentText(), dlg.lineEdit_4.text()))

dlg.comboBox.currentIndexChanged.connect(aktualny)
dlg.pushButton.clicked.connect(display_forecast)
dlg.pushButton_2.clicked.connect(pobierz_dane)

dlg.show()
app.exec()