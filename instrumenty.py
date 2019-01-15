from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from Modelgui import model_licz
from data.data_act import *
from data.data_download import *
from data.data_extract import *

app = QtWidgets.QApplication([])
dlg = uic.loadUi("Instrumenty.ui")

download_actual_gold()
download_actual_currency()

def show_message(title='Test', message='Test'):
    QMessageBox.information(None, title, message)

def pobierz_dane():
    show_message('Info', dlg.comboBox.currentText())
    if dlg.comboBox.currentText() == 'gold':
        download_last_year_gold()
    else:
        download_last_year_curr(dlg.comboBox.currentText())
    to_csv(dlg.comboBox.currentText())
    show_message('Info', "Dane zostały pobrane")

def aktualny():
    #dlg.lineEdit.setText(waluty[dlg.comboBox.currentText()])
    dlg.lineEdit.setText(str(get_actual_value(dlg.comboBox.currentText(), read_act_file(dlg.comboBox.currentText()))))
    dlg.lineEdit_3.setText(str(get_actual_date(dlg.comboBox.currentText(), read_act_file(dlg.comboBox.currentText()))))

waluty = {'złoto': 'gold', 'euro': 'EUR', 'funt szterling': 'GBP', 'dolar amerykański': 'USD', 'korona czeska': 'CZK', 'peso meksykańskie': 'MXN', 'rubel rosyjski': 'RUB'}



def display_forecast():
    dlg.lineEdit_2.setText(model_licz(str(dlg.comboBox_2.currentText()), [str(dlg.lineEdit_4.text())]))

dlg.comboBox.currentIndexChanged.connect(aktualny)
dlg.pushButton.clicked.connect(display_forecast)
dlg.pushButton_2.clicked.connect(pobierz_dane)


#print(get_actual_value('gold', read_act_file('gold')))

dlg.show()
app.exec()