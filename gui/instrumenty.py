from PyQt5 import QtWidgets, uic


app = QtWidgets.QApplication([])
dlg = uic.loadUi("instrumenty.ui")


def aktualny():
    dlg.lineEdit.setText(waluty[dlg.comboBox.currentText()])


waluty = {'złoto': 'gold', 'euro': 'EUR', 'funt szterling': 'GBP', 'dolar amerykański': 'USD', 'korona czeska': 'CZK', 'peso meksykańskie': 'MXN', 'rubel rosyjski': 'RUB'}


def prognozuj():
    dlg.lineEdit_2.setText("jupikajej")

dlg.comboBox.currentIndexChanged.connect(aktualny)
dlg.pushButton.clicked.connect(prognozuj)

dlg.show()
app.exec()