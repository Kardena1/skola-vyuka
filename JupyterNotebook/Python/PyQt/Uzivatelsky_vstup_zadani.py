# Zpracování uživatelského vstupu
# Obvykle chceme, abychom mohli do aplikace také informace zadávat a následně zpracovat.
# Vytvoříme si tedy jednoduché okno s textem, textovým polem a tlačítkem.

# QLineEdit
# Pro zadání textových vstupních informací Můžeme využít Widget QLineEdit.
# Jako text můžeme samozřejmě zadat i číslice - jen před jejich použitím jako čísla nesmíme zapomenout a jejich přetypování - převedení na požadovaný datový typ.

# !!! pip install PyQt5 !!!

# Kromě QLineEdit přidáme funkci, která načte text z textového pole a změní nápis v okně na námi zadaný text. Funkci připojíme k akci kliknutí na tlačítko.


# from PyQt5 import QtWidgets

# app = QtWidgets.QApplication([])

# hlavni_okno = QtWidgets.QWidget()
# hlavni_okno.setWindowTitle('Můj supr program')

# usporadani = QtWidgets.QHBoxLayout()
# hlavni_okno.setLayout(usporadani)

# napis = QtWidgets.QLabel('Nějaký text...')
# usporadani.addWidget(napis)

# vstup = QtWidgets.QLineEdit()
# usporadani.addWidget(vstup)

# tlacitko = QtWidgets.QPushButton('Klikni na mě')
# usporadani.addWidget(tlacitko)

# def zmen_text():
#     vstupni_text = vstup.text() # do proměnné vstupni_text se uloží text z textového pole
#     napis.setText(f"Toto jsi napsal: {vstupni_text}") # Přiřazení textu
    
#     # vstup.setText("") 
#     # vstupnímu poli můžeme nastavit prázdný string jako text
#     # tím "smažeme" původní text a při dalším zadávání ho nemusíme ručně mazat

# tlacitko.clicked.connect(zmen_text) # připojení funkce zmen_text k tlačítku

# hlavni_okno.show()

# app.exec()

# aplikace pred zmenou textu: https://camo.githubusercontent.com/fd27a1c43b8f13bd7d4b3193f9fcde2ffa1add12009d43a4b2fe76b847157021/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f4a61726f736c6176486f6c6563656b2f5465616368696e672f6d61737465722f4a7570797465724e6f7465626f6f6b2f507951742f696d616765732f696d675f6f6b6e6f5f76737475702e706e67
# aplikace po zmene textu: https://camo.githubusercontent.com/34517aba6c13df204127c398cb4cbd1aae45ffdfe7befd4e90a1444a4da97d7a/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f4a61726f736c6176486f6c6563656b2f5465616368696e672f6d61737465722f4a7570797465724e6f7465626f6f6b2f507951742f696d616765732f696d675f6f6b6e6f5f76737475705f706f5f7a6d656e652e706e67

# Využití validátoru:
# Knihovna PyQt5 nabízí několik typů validátorů (celé číslo, desetinné číslo a regulární výraz - tím lze obecně popsat např. emailovou adresu, telefoní číslo apd.).
# Validátor zajistí, že neplatná hodnota nepůjde do vstupního pole vůbec zapsat.
# Použití si ukážeme na validátoru celých čísel:

# from PyQt5 import QtWidgets
# from PyQt5 import QtGui


# app = QtWidgets.QApplication([])

# hlavni_okno = QtWidgets.QWidget()
# hlavni_okno.setWindowTitle("Můj supr program")

# usporadani = QtWidgets.QHBoxLayout()
# hlavni_okno.setLayout(usporadani)

# napis = QtWidgets.QLabel("Nějaký text...")
# usporadani.addWidget(napis)

# validator_celych_cisel = QtGui.QIntValidator() # zde si vybereme konktrétní validátor
# vstup = QtWidgets.QLineEdit()
# vstup.setValidator(validator_celych_cisel) # zde aplikujeme námi zvolený validátor na textové pole
# usporadani.addWidget(vstup)
# # Nyní když spustíme aplikaci, tak do textového pole budeme moci zapsat pouze celá čísla

# tlacitko = QtWidgets.QPushButton("Klikni na mě")
# usporadani.addWidget(tlacitko)


# def zmen_text():
#     vstupni_text = vstup.text()
#     napis.setText(f"Toto jsi napsal: {vstupni_text}")
#     vstup.setText("")


# tlacitko.clicked.connect(zmen_text)

# hlavni_okno.show()

# app.exec()



# from PyQt5 import QtWidgets
# from PyQt5 import QtGui


# app = QtWidgets.QApplication([])

# hlavni_okno = QtWidgets.QWidget()
# hlavni_okno.setWindowTitle("Můj supr program")

# usporadani = QtWidgets.QHBoxLayout()
# hlavni_okno.setLayout(usporadani)

# napis = QtWidgets.QLabel("Nějaký text...")
# usporadani.addWidget(napis)

# vstup = QtWidgets.QLineEdit()
# usporadani.addWidget(vstup)

# tlacitko = QtWidgets.QPushButton("Klikni na mě")
# usporadani.addWidget(tlacitko)


# def soucet():
#     vstupni_text = vstup.text()  # přečte hodnotu na vstupu a uloží si ji jako string
#     pole_souctu = vstupni_text.split(" ") # string ze vstupu předěláme na pole, prvky pole jsou odděleny mezerou
#     vysledek = 0
#     try:
#         for prvek in pole_souctu: # pro každý prvek v poli
#             cislo = int(prvek) # převeď string na int
#             vysledek += cislo # přičti k výsledku

#     except ValueError: # pokud některý prvek nelze předělat na int, tzn. není číslo
#         vysledek = "Neumím počítat s písmenky" # chybová hláška

#     napis.setText(f"Součet je {vysledek}")


# tlacitko.clicked.connect(soucet)

# hlavni_okno.show()

# app.exec()


# Cvičení:
# Bude následovat jedno cvičení na procvičení tohoto tématu.

# Cvičení 1:
# Naprogramujte aplikaci, která podle zadaných vstupů buď sečte hodnoty, nebo je vynásobí.
# Výsledek může vypadat následovně (můžete však vytvořit jakýkoukoliv podobnou).

# from PyQt5 import QtWidgets
# from PyQt5 import QtGui
# from PyQt5.QtGui import QPalette, QColor
# from PyQt5.QtGui import QRegularExpressionValidator
# from PyQt5.QtCore import QRegularExpression


# def soucet():
#     operace = input2.text().strip()
#     if operace == "+" :
#         vstupni_text = " ".join(input1.text().split())
#         pole_souctu = vstupni_text.split(" ")
#         vysledek = 0
#         try: 
#             for prvek in pole_souctu:
#                 cislo = int(prvek)
#                 vysledek += cislo
#         except ValueError:
#             vysledek = "Neumim pocitat s pismenky"

#         napis.setText(f"soucet je: {vysledek}")
#     elif operace == "*" :
#         vstupni_text = " ".join(input1.text().split())
#         pole_souctu = vstupni_text.split(" ")
#         vysledek = 0
#         try: 
#             #cislo=[]
#             cislo = 1   
#             for prvek in pole_souctu:
#                 print(prvek)
#                 #cislo.append(int(prvek))
#                 cislo = cislo * int(prvek)
#             vysledek = cislo    
#         except ValueError:
#             vysledek = "Neumim pocitat s pismenky"


#         napis.setText(f"soucet je: {vysledek}")


    




# app = QtWidgets.QApplication([])

# hlavni_okno = QtWidgets.QWidget()
# hlavni_okno.setWindowTitle("Kalkulacka")
# hlavni_okno.setFixedSize(200,150)
# palette = hlavni_okno.palette()
# palette.setColor(QPalette.Window, QColor(100, 200, 200))
# hlavni_okno.setAutoFillBackground(True)
# hlavni_okno.setPalette(palette)


# regex = QRegularExpression(r"[+*]")
# validator = QRegularExpressionValidator(regex)
# regex_cisel = QRegularExpression(r"^-?\d+(?:\s+-?\d+)*$")
# validator_cisel = QRegularExpressionValidator(regex_cisel)


# usporadani = QtWidgets.QVBoxLayout()
# hlavni_okno.setLayout(usporadani)

# input1 = QtWidgets.QLineEdit()
# input1.setValidator(validator_cisel)
# usporadani.addWidget(input1)


# input2 = QtWidgets.QLineEdit()
# input2.setValidator(validator)
# input2.setMaxLength(1)
# usporadani.addWidget(input2)

# tlacitko = QtWidgets.QPushButton("Klikni na me")
# usporadani.addWidget(tlacitko)

# napis = QtWidgets.QLabel("Vysledek je:")
# usporadani.addWidget(napis)


# tlacitko.clicked.connect(soucet)




# hlavni_okno.show()

# app.exec()

