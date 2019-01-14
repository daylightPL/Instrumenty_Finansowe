from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from Modelgui import model_licz


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



def display_forecast():
    dlg.lineEdit_2.setText(model_licz(str(dlg.comboBox_2.currentText()), [str(dlg.lineEdit_4.text())]))

dlg.comboBox.currentIndexChanged.connect(aktualny)
dlg.pushButton.clicked.connect(display_forecast)
dlg.pushButton_2.clicked.connect(pobierz_dane)

dlg.show()
app.exec()