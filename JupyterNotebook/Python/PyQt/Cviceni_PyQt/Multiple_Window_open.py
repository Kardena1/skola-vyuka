from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPalette, QColor
import sys
app = QtWidgets.QApplication([])

hlavni_okno = QtWidgets.QWidget()
hlavni_okno.setWindowTitle("Test")
hlavni_okno.setFixedSize(400,400)


palette = hlavni_okno.palette()
palette.setColor(QPalette.Window, QColor(255, 200, 200))
hlavni_okno.setAutoFillBackground(True)
hlavni_okno.setPalette(palette)



vedlejsi_okno = QtWidgets.QWidget()
vedlejsi_okno.setWindowTitle("Vedlejsi okno")
vedlejsi_okno.setFixedSize(400,400)

usporadani = QtWidgets.QHBoxLayout()
hlavni_okno.setLayout(usporadani)

def ukaz_okno():
    vedlejsi_okno.show()

tlacitko = QtWidgets.QPushButton("Zmackni me")
usporadani.addWidget(tlacitko)

tlacitko.clicked.connect(ukaz_okno)



hlavni_okno.show()

app.exec()




