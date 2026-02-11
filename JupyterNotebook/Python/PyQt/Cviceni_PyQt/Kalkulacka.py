# import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QLineEdit, QPushButton,
#     QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy, QLabel
# )
# from PyQt5.QtGui import QFont, QRegularExpressionValidator, QPalette, QColor
# from PyQt5.QtCore import QRegularExpression, Qt

# app = QApplication([])

# hlavni_okno = QWidget()
# hlavni_okno.setWindowTitle("Kalkulačka")
# hlavni_okno.setFocusPolicy(Qt.StrongFocus)
# hlavni_okno.setStyleSheet("""
#     QPushButton {
#         font-size: 18px;
#         background-color: #f0f0f0;
#     }
#     QLineEdit {
#         font-size: 40px;
#     }
# """)



# vbox = QVBoxLayout()
# hbox = QHBoxLayout()

# napis= QtWidgets.QLineEdit()
# tl00 = QtWidgets.QPushButton("0")
# tl01 = QtWidgets.QPushButton("1")
# tl02 = QtWidgets.QPushButton("2")
# tl03 = QtWidgets.QPushButton("3")
# tl04 = QtWidgets.QPushButton("4")
# tl05 = QtWidgets.QPushButton("5")
# tl06 = QtWidgets.QPushButton("6")
# tl07 = QtWidgets.QPushButton("7")
# tl08 = QtWidgets.QPushButton("8")
# tl09 = QtWidgets.QPushButton("9")
# tlplus = QtWidgets.QPushButton("+")
# tldeleni = QtWidgets.QPushButton("/")
# tlminus = QtWidgets.QPushButton("-")
# tlkrat = QtWidgets.QPushButton("*")
# tlnum = QtWidgets.QPushButton("num")
# tltecka = QtWidgets.QPushButton(".")
# tlenter = QtWidgets.QPushButton("enter")


# vsechna_tlacitka = [
#     tl00, tl01, tl02, tl03, tl04, tl05, tl06, tl07, tl08, tl09,
#     tlplus, tlminus, tlkrat, tldeleni, tlnum, tltecka, tlenter, napis
# ]

# for btn in vsechna_tlacitka:
#     btn.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    
# regex = QRegularExpression(r"[0-9+\-*/\s]*")
# validator = QRegularExpressionValidator(regex)
# napis.setValidator(validator)

# layout = QtWidgets.QGridLayout()



# hlavni_okno.setLayout(layout)
# layout.addWidget(napis, 0, 0, 1, 4)
# layout.addWidget(tlnum, 1, 0)
# layout.addWidget(tldeleni, 1, 1)
# layout.addWidget(tlkrat, 1, 2)
# layout.addWidget(tlminus, 1, 3)
# layout.addWidget(tl07, 2, 0)
# layout.addWidget(tl08, 2, 1)
# layout.addWidget(tl09, 2, 2)
# layout.addWidget(tlplus, 2, 3, 2, 1)
# layout.addWidget(tl04, 3, 0)
# layout.addWidget(tl05, 3, 1)
# layout.addWidget(tl06, 3, 2)
# layout.addWidget(tl01, 4, 0)
# layout.addWidget(tl02, 4, 1)
# layout.addWidget(tl03, 4, 2)    
# layout.addWidget(tl00, 5, 0, 1, 2)
# layout.addWidget(tltecka, 5, 2)
# layout.addWidget(tlenter, 4, 3, 2, 1)




# # FUNKCE

# def pridat_znak(znak):
#     aktualni_text = napis.text()
#     napis.setText(aktualni_text + znak)



# def keyPressEvent(event):
#     key = event.key()

#     if Qt.Key_0 <= key <= Qt.Key_9:
#         pridat_znak(str(key - Qt.Key_0))

#     elif Qt.KeypadModifier and Qt.Key_0 <= key <= Qt.Key_9:
#         pridat_znak(str(key - Qt.Key_0))

#     elif key == Qt.Key_Plus:
#         pridat_znak("+")
#     elif key == Qt.Key_Minus:
#         pridat_znak("-")
#     elif key == Qt.Key_Asterisk:
#         pridat_znak("*")
#     elif key == Qt.Key_Slash:
#         pridat_znak("/")
#     elif key == Qt.Key_Period or key == Qt.Key_Comma:
#         pridat_znak(".")    

# tl00.clicked.connect(lambda: pridat_znak("0"))
# tl01.clicked.connect(lambda: pridat_znak("1"))
# tl02.clicked.connect(lambda: pridat_znak("2"))
# tl03.clicked.connect(lambda: pridat_znak("3"))
# tl04.clicked.connect(lambda: pridat_znak("4"))
# tl05.clicked.connect(lambda: pridat_znak("5"))
# tl06.clicked.connect(lambda: pridat_znak("6"))
# tl07.clicked.connect(lambda: pridat_znak("7"))
# tl08.clicked.connect(lambda: pridat_znak("8"))
# tl09.clicked.connect(lambda: pridat_znak("9"))
# tlplus.clicked.connect(lambda: pridat_znak("+"))
# tlminus.clicked.connect(lambda: pridat_znak("-"))
# tlkrat.clicked.connect(lambda: pridat_znak("*"))
# tldeleni.clicked.connect(lambda: pridat_znak("/"))
# tltecka.clicked.connect(lambda: pridat_znak("."))


# hlavni_okno.show()
# app.exec()



import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QGridLayout
)
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtCore import QRegularExpression, Qt


class Kalkulacka(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulačka")
        self.setFocusPolicy(Qt.StrongFocus)

        self.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                background-color: #f0f0f0;
            }
            QLineEdit {
                font-size: 40px;
            }
        """)

        self.napis = QLineEdit()

        regex = QRegularExpression(r"[0-9+\-*/\s]*")
        validator = QRegularExpressionValidator(regex)
        self.napis.setValidator(validator)


        self.tlacitka = {}
        for text in ["0","1","2","3","4","5","6","7","8","9",".",]:
            self.tlacitka[text] = QPushButton(text)
            self.tlacitka[text].setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)                    
            self.tlacitka[text].clicked.connect(lambda _, t=text: self.pridat_znak(t))

        self.tlacitka["Enter"] = QPushButton("Enter")
        self.tlacitka["Enter"].setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.tlacitka["Enter"].setStyleSheet("background-color: #d0d0d0;")
        # self.tlacitka["Enter"].clicked.connect(self.spocitat)

        self.tlacitka["Num"] = QPushButton("Num")
        self.tlacitka["Num"].setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.tlacitka["Num"].setStyleSheet("background-color: #d0d0d0;")

        for text in ["+","-","*","/",]:
            self.tlacitka[text] = QPushButton(text)
            self.tlacitka[text].setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)                    
            self.tlacitka[text].clicked.connect(lambda _, t=text: self.pridat_znak(t))
            # self.tlacitka[text].clicked.connect()
            self.tlacitka[text].setStyleSheet("background-color: #d0d0d0;")

        def debug(t):
            print("Debug: Kliknuto na tlačítko", t)

        for text in self.tlacitka:
            self.tlacitka[text].clicked.connect(lambda _, t=text: debug(t))
    


        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(self.napis, 0, 0, 1, 4)
        layout.addWidget(self.tlacitka["Num"], 1, 0)
        layout.addWidget(self.tlacitka["/"], 1, 1)
        layout.addWidget(self.tlacitka["*"], 1, 2)
        layout.addWidget(self.tlacitka["-"], 1, 3)
        layout.addWidget(self.tlacitka["7"], 2, 0)
        layout.addWidget(self.tlacitka["8"], 2, 1)
        layout.addWidget(self.tlacitka["9"], 2, 2)
        layout.addWidget(self.tlacitka["+"], 2, 3, 2, 1)
        layout.addWidget(self.tlacitka["4"], 3, 0)
        layout.addWidget(self.tlacitka["5"], 3, 1)
        layout.addWidget(self.tlacitka["6"], 3, 2)
        layout.addWidget(self.tlacitka["1"], 4, 0)
        layout.addWidget(self.tlacitka["2"], 4, 1)
        layout.addWidget(self.tlacitka["3"], 4, 2)    
        layout.addWidget(self.tlacitka["0"], 5, 0, 1, 2)
        layout.addWidget(self.tlacitka["."], 5, 2)
        layout.addWidget(self.tlacitka["Enter"], 4, 3, 2, 1)

    def pridat_znak(self, znak):
        self.napis.setText(self.napis.text() + znak)

    def keyPressEvent(self, event):
        key = event.key()

        if Qt.Key_0 <= key <= Qt.Key_9:
            cislo = str(key - Qt.Key_0)
            self.tlacitka[cislo].click()

        elif key == Qt.Key_Plus:
            self.tlacitka["+"].click()

        elif key == Qt.Key_Minus:
            self.tlacitka["-"].click()

        elif key == Qt.Key_Asterisk:
            self.tlacitka["*"].click()

        elif key == Qt.Key_Slash:
            self.tlacitka["/"].click()

        elif key in (Qt.Key_Period, Qt.Key_Comma):
            self.tlacitka["."].click()

        elif key in (Qt.Key_Enter, Qt.Key_Return):
            self.tlacitka["Enter"].click()

        else:
            super().keyPressEvent(event)


    # def spocitat(self):
    #     try:
    #         vyraz = self.napis.text()
    #         vysledek = eval(vyraz, {"__builtins__": None}, {})
    #         self.napis.setText(str(vysledek))
    #     except:
    #         self.napis.setText("Chyba")


    # def spocitat(self):

    #     vyraz = self.napis.text()
    #     if "-" in vyraz:
    #         operator.+


    # def spocitat(self):
    #     vyraz = self.napis.text()
    #     if "+" in vyraz:
    #         try:
    #             casti = vyraz.split("+")
                
    #             cislo1 = float(casti[0])
    #             cislo2 = float(casti[1])
    #             vysledek = cislo1 + cislo2 
    #             self.napis.setText(str(vysledek))
    #         except:
    #             self.napis.setText("Chyba")
    #     elif "-" in vyraz:
    #         try:
    #             casti = vyraz.split("-")
                
    #             cislo1 = float(casti[0])
    #             cislo2 = float(casti[1])
    #             vysledek = cislo1 - cislo2 
    #             self.napis.setText(str(vysledek))
    #         except:
    #             self.napis.setText("Chyba")






app = QApplication(sys.argv)
okno = Kalkulacka()
okno.show()
sys.exit(app.exec())
