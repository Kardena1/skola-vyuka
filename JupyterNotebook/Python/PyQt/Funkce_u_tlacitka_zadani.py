# Funkce u tlačítek
# Nyní již víme jak vytvořit grafické okno a přidat do něj text a tlačítko, ukážeme si jak přiřadit tlačítku funkci - tedy se po jeho stisknutí "něco stane".

# ! pip install PyQt5

# Vytvoříme jednoduché okno s textem a tlačítkem.

# from PyQt5 import QtWidgets

# app = QtWidgets.QApplication([])  # inicializace aplikace

# hlavni_okno = QtWidgets.QWidget()  # vytvoření objektu hlavního okna
# hlavni_okno.setWindowTitle('Můj supr program')  # název okna

# usporadani = QtWidgets.QHBoxLayout()  # vytvoření Layout managera typu "vedle sebe"
# hlavni_okno.setLayout(usporadani)  # nastavení Layout managera našemu hlavnímu oknu

# napis = QtWidgets.QLabel('Nějaký text...')  # samotný text
# usporadani.addWidget(napis)  # přiřazení nápisu k zvolenému uspořádání

# tlacitko = QtWidgets.QPushButton('Klikni na mě')  # tlačítko
# usporadani.addWidget(tlacitko)  # přiřazení tlačítka k zvolenému uspořádání

# hlavni_okno.show()  # okno bude viditelné

# app.exec() # spuštění aplikace

#vysledek : https://camo.githubusercontent.com/9157ab52f9251ca435388474d49a2cf7a9696324320c12d2b6da631ea7b26940/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f4a61726f736c6176486f6c6563656b2f5465616368696e672f6d61737465722f4a7570797465724e6f7465626f6f6b2f507951742f696d616765732f696d675f6f6b6e6f5f746c616369746b6f5f746578745f707265645f7a6d656e6f752e504e47

# from PyQt5 import QtWidgets

# app = QtWidgets.QApplication([])

# hlavni_okno = QtWidgets.QWidget()
# hlavni_okno.setWindowTitle("Můj supr program")

# usporadani = QtWidgets.QHBoxLayout()
# hlavni_okno.setLayout(usporadani)

# napis = QtWidgets.QLabel("Nějaký text...")
# usporadani.addWidget(napis)

# tlacitko = QtWidgets.QPushButton("Klikni na mě")
# usporadani.addWidget(tlacitko)

# tlacitko2 = QtWidgets.QPushButton("Na toto muzes taky kliknout")
# usporadani.addWidget(tlacitko2)

# napis2 = QtWidgets.QLabel("Taky nejaky text")
# usporadani.addWidget(napis2)

# # Funkce, která je zodpovědná za změnu textu
# def zmen_text():
#     novy_text = "Změnil jsem text"  # Text, který se zobrazí místo stávajícího
#     napis.setText(novy_text)  # Přiřazení textu
# def zmen_napis2():
#     novy_text = "taky muzu menit text"
#     napis2.setText(novy_text)



# tlacitko.clicked.connect(zmen_text)  # připojení funkce zmen_text k tlačítku
# tlacitko2.clicked.connect(zmen_napis2)
# Vsimněte si, že funkci zmen_text() vkládáme do connect() bez závorek
# 1) Zkuste odhadnout proč
# 2) Zkuste si spustit:
# print(novy_text()) # se závorkami
# print(novy_text) # bez závorek

# hlavni_okno.show()

# app.exec()


# Cvičení:
# Bude následovat pár cvičení na procvičení tohoto tématu.

# Cvičení 1:
# Za pomocí knihovny PyQt5 vytvořte program jehož výstupem bude tato aplikace.

# Pred kliknutim: https://camo.githubusercontent.com/e21b2714ae862112042459297095d7523f75224acf57aa63efb029debcd35952/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f4a61726f736c6176486f6c6563656b2f5465616368696e672f6d61737465722f4a7570797465724e6f7465626f6f6b2f507951742f696d616765732f696d675f6f6b6e6f5f746c616369746b6f5f707265645f7a6d656e6f755f6e6164706973752e504e47

# Po kliknuti: https://camo.githubusercontent.com/710904913d6e75e7f07fe710e7683347f5e5f2ff97c5df69a907e10f768d999a/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f4a61726f736c6176486f6c6563656b2f5465616368696e672f6d61737465722f4a7570797465724e6f7465626f6f6b2f507951742f696d616765732f696d675f6f6b6e6f5f746c616369746b6f5f706f5f7a6d656e655f6e6164706973752e504e47

# from PyQt5 import QtWidgets

# def zmackni_button():
#     novy_nazev = "Novy nazev okna"
#     hlavni_okno.setWindowTitle(novy_nazev)

# app = QtWidgets.QApplication([])

# hlavni_okno = QtWidgets.QWidget()
# hlavni_okno.setWindowTitle('Muj supr program')
# hlavni_okno.setFixedSize(800,600)

# usporadani = QtWidgets.QHBoxLayout()
# hlavni_okno.setLayout(usporadani)


# tlacitko = QtWidgets.QPushButton("klikni na me")
# usporadani.addWidget(tlacitko)

# tlacitko.clicked.connect(zmackni_button)


# hlavni_okno.show()
# app.exec()

# TODO: Zde přijde váš kód ^


# Cvičení 2:
# Upravte kód tak, aby se při stisknutí tlačítka změnil text na jeden náhodně vybraný z 5 textů (texty si vymyslete Vy).

# Pro náhodný výběr použijte funkci choice z knihovny random


# from PyQt5 import QtWidgets
# import random

# slov_list = ['ahoj','cau','dobry den','zdravim','hello']

# app = QtWidgets.QApplication([])

# hlavni_okno = QtWidgets.QWidget()
# hlavni_okno.setWindowTitle("Můj supr program")

# usporadani = QtWidgets.QHBoxLayout()
# hlavni_okno.setLayout(usporadani)

# napis = QtWidgets.QLabel("Nějaký text...")
# usporadani.addWidget(napis)

# tlacitko = QtWidgets.QPushButton("Klikni na mě")
# usporadani.addWidget(tlacitko)

# def zmen_text():
#     nove_slovo = random.choice(slov_list)
#     napis.setText(nove_slovo)

# tlacitko.clicked.connect(zmen_text)

# hlavni_okno.show()

# app.exec()
     
