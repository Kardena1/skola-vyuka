# Vytvoření okna a zobrazení textu
# Základní práce s knihovnou PyQt je velmi přímočará.

# Vytvoříme objekt, který si bude pamatovat všechny informace o běžící aplikaci - zda je aktivní, zmenšená na lištu, překrytá jinou aplikací, ...
# Vytvoříme hlavní okno aplikace
# Na hlavní okno navážeme všechny ostatní prvky
# Označíme, že má být hlavní okno viditelné
# Spustíme aplikaci

# from PyQt5 import QtWidgets

# app = QtWidgets.QApplication([]) # inicializace aplikace

# hlavni_okno = QtWidgets.QWidget()  # vytvoření objektu hlavního okna
# hlavni_okno.setWindowTitle("Můj supr program")  # název okna

# hlavni_okno.show() # okno bude viditelné

# app.exec() # spuštění aplikace

# vysledek: https://raw.githubusercontent.com/JaroslavHolecek/Teaching/master/JupyterNotebook/PyQt/images/img_okno_prazdne.PNG

# Vložení prvků do okna - text

# from PyQt5 import QtWidgets
# from PyQt5.QtGui import QIcon # import QIcon

# app = QtWidgets.QApplication([])
# hlavni_okno = QtWidgets.QWidget()
# hlavni_okno.setWindowTitle('Můj supr program')
# hlavni_okno.setWindowIcon(QIcon(r"D:\Users\solomchm\Downloads\OIP.jpg"))       # pouzite pro set iconu programu

# usporadani = QtWidgets.QHBoxLayout() # vytvoření Layout managera typu "vedle sebe"
# hlavni_okno.setLayout(usporadani) # nastavení Layout managera našemu hlavnímu oknu

# napis = QtWidgets.QLabel('Nějaký text....')  # vytvoření objektu pro zobrazení textu
# usporadani.addWidget(napis) # vložení nápisu (objektu, který zobrazuje nápis) do Layout managera

# napis2 = QtWidgets.QLabel('Toto je text.')  # vytvoření objektu pro zobrazení textu
# usporadani.addWidget(napis2) # vložení nápisu (objektu, který zobrazuje nápis) do Layout managera

# hlavni_okno.show() 
# app.exec()
# vysledek: https://raw.githubusercontent.com/JaroslavHolecek/Teaching/master/JupyterNotebook/PyQt/images/img_okno_text.PNG


# Tlacitko
# from PyQt5 import QtWidgets

# app = QtWidgets.QApplication([])

# hlavni_okno = QtWidgets.QWidget()
# hlavni_okno.setWindowTitle('Můj supr program')

# usporadani = QtWidgets.QHBoxLayout()
# hlavni_okno.setLayout(usporadani)

# napis = QtWidgets.QLabel('Nějaký text...')
# usporadani.addWidget(napis)

# tlacitko = QtWidgets.QPushButton('Klikni na mě')  # vytvoření objektu tlačítko
# usporadani.addWidget(tlacitko)  # vložení tlačítka do Layout managera

# hlavni_okno.show()
# app.exec()

# vysledek: https://raw.githubusercontent.com/JaroslavHolecek/Teaching/master/JupyterNotebook/PyQt/images/img_okno_text_tlacitko.PNG


# Cvičení:
# Cvičení 1:
# Za pomocí knihovny PyQt5 vytvořte program jehož výstupem bude tato aplikace.
# Výstup: https://raw.githubusercontent.com/JaroslavHolecek/Teaching/master/JupyterNotebook/PyQt/images/img_okno_cviceni_tlacitko_text.PNG

from PyQt5 import QtWidgets
app = QtWidgets.QApplication([])

hlavni_okno = QtWidgets.QWidget()
hlavni_okno.setWindowTitle('Cviceni')
hlavni_okno.setFixedSize(8W00,600)

usporadani = QtWidgets.QHBoxLayout()
hlavni_okno.setLayout(usporadani)

tlacitko = QtWidgets.QPushButton('Zpracovat')
usporadani.addWidget(tlacitko)

napis = QtWidgets.QLabel('Popisek')
usporadani.addWidget(napis)
hlavni_okno.show()
app.exec()
# TODO: Zde přijde váš kód ->