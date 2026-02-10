import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy, QLabel
)
from PyQt5.QtGui import QFont, QRegularExpressionValidator, QPalette, QColor
from PyQt5.QtCore import QRegularExpression, Qt

app = QApplication([])

hlavni_okno = QWidget()
hlavni_okno.setWindowTitle("Kalkulačka")
hlavni_okno.setStyleSheet("""
    QPushButton {
        font-size: 18px;
        background-color: #f0f0f0;
    }
    QLineEdit {
        font-size: 40px;
    }
""")



vbox = QVBoxLayout()
hbox = QHBoxLayout()

napis= QtWidgets.QLineEdit()
tl00 = QtWidgets.QPushButton("0")
tl01 = QtWidgets.QPushButton("1")
tl02 = QtWidgets.QPushButton("2")
tl03 = QtWidgets.QPushButton("3")
tl04 = QtWidgets.QPushButton("4")
tl05 = QtWidgets.QPushButton("5")
tl06 = QtWidgets.QPushButton("6")
tl07 = QtWidgets.QPushButton("7")
tl08 = QtWidgets.QPushButton("8")
tl09 = QtWidgets.QPushButton("9")
tlplus = QtWidgets.QPushButton("+")
tldeleni = QtWidgets.QPushButton("/")
tlminus = QtWidgets.QPushButton("-")
tlkrat = QtWidgets.QPushButton("*")
tlnum = QtWidgets.QPushButton("num")
tltecka = QtWidgets.QPushButton(".")
tlenter = QtWidgets.QPushButton("enter")


vsechna_tlacitka = [
    tl00, tl01, tl02, tl03, tl04, tl05, tl06, tl07, tl08, tl09,
    tlplus, tlminus, tlkrat, tldeleni, tlnum, tltecka, tlenter, napis
]

for btn in vsechna_tlacitka:
    btn.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    
regex = QRegularExpression(r"[0-9+\-*/\s]*")
validator = QRegularExpressionValidator(regex)
napis.setValidator(validator)

usporadani = QtWidgets.QGridLayout()



hlavni_okno.setLayout(usporadani)
usporadani.addWidget(napis, 0, 0, 1, 4)
usporadani.addWidget(tlnum, 1, 0)
usporadani.addWidget(tldeleni, 1, 1)
usporadani.addWidget(tlkrat, 1, 2)
usporadani.addWidget(tlminus, 1, 3)
usporadani.addWidget(tl07, 2, 0)
usporadani.addWidget(tl08, 2, 1)
usporadani.addWidget(tl09, 2, 2)
usporadani.addWidget(tlplus, 2, 3, 2, 1)
usporadani.addWidget(tl04, 3, 0)
usporadani.addWidget(tl05, 3, 1)
usporadani.addWidget(tl06, 3, 2)
usporadani.addWidget(tl01, 4, 0)
usporadani.addWidget(tl02, 4, 1)
usporadani.addWidget(tl03, 4, 2)    
usporadani.addWidget(tl00, 5, 0, 1, 2)
usporadani.addWidget(tltecka, 5, 2)
usporadani.addWidget(tlenter, 4, 3, 2, 1)





hlavni_okno.show()
app.exec()
