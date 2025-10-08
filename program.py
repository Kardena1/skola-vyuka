# tento kod poprosi uzivatele o zadani kterehokoliv poctu cisel, s mezerou a najde v nich nejvetsi cislo

cisla = input("Zadejte, kolik chcete cisel (oddelene mezerou):  ").split()

cisla = [float(x) for x in cisla]
nejvetsi = 0 # nejvetsi je nula, a potom se bude menit na to nejvetsi
for c in cisla:
    if c > nejvetsi:
        nejvetsi = c

print("nejvetsi cislo je: ", nejvetsi)

#Zadejte, kolik chcete cisel (oddelene mezerou):  15 23 12313 6 1
#nejvetsi cislo je:  12313.0
#Process finished with exit code 0


# tento kod poprosi uzivatele o zadani kterehokoliv poctu cisel, s mezerou a najde v nich nejmensi cislo

cisla = input("Zadejte, kolik chcete cisel (oddelene mezerou):  ").split()

cisla = [float(x) for x in cisla]
nejmensi = cisla[1] # dam prvni cislo jako nejmensi - a potom pujde srovnavani, ikdyz prvni cislo bude nejmensi 
for c in cisla:
    if c < nejmensi:
        nejmensi = c


print("nejmensi cislo je: ", nejmensi)

#Zadejte, kolik chcete cisel (oddelene mezerou):  1 2 5 8 
#nejmensi cislo je:  1.0
#Process finished with exit code 0
