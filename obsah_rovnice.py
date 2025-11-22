import math
import time

def obdelnik(a,b):
    print("pocitam")
    o = a+a+b+b
    s = a*b
    return o,s

def kruh(a):
    o = 2*math.pi*a
    s = math.pi*a**2
    return o,s

def trojuhelnik(zakladna, vyska, strana_a, strana_b, strana_c):
    s = (zakladna * vyska) / 2
    o = strana_a + strana_b + strana_c
    return o, s
    
def brzdna_draha(draha, metry,):
    vysledek = metry**2/(2*draha*9.81)
    return vysledek

def k():
    cislo1 = int(input("Vybral jste vypocet kruhu. Zadejte polomer:  "))
    o, s = kruh(cislo1)
    print("Obvod je :", o)
    print("Obsah je :", s)

def o():
    cislo1, cislo2 = map(int,input("Zadejte cisla oddelene mezerou: ").split())
    o, s = obdelnik(cislo1, cislo2)
    print("Obvod je :", o)
    print("Obsah je :", s)

def t():
    zakladna = float(input("Délka základny (a): "))
    vyska = float(input("Výška na základnu (vₐ): "))
    print("Zadejte délky všech tří stran trojúhelníku (a, b, c):")
    strana_a, strana_b, strana_c = map(float, input().split())

    o, s = trojuhelnik(zakladna, vyska, strana_a, strana_b, strana_c)
    print("Obvod trojúhelníku je:", o)
    print("Obsah trojúhelníku je:", s)

def b():
    
    lokace = str(input("Zadejte vasi silnici (Sucha, Mokra, Naledi): ").lower())
    if lokace == "sucha":
        draha = 0.8
    elif lokace == "mokra":
        draha = 0.5
    elif lokace == "naledi":
        draha = 0.1
    rychlost = float(input("Zadejte vasi rychlost (km/h) "))
    metry = rychlost/3.6
    vysledek = brzdna_draha(draha, metry)
    print("Vas vysledek je :",vysledek)
        
   

def start():
    while True:
        vyber = input("Zadejte co chcete pocitat (K = Kruh, O = Obdelnik. T = Trojuhelnik. B = Brzdna Draha. Ukoncit program: Q): ").lower()
        if vyber == "k":
            while True:
                k()                            
                vyb = input("Chcete vypocitat dalsi kruh? (Ano/Ne): ").lower()
                if vyb == "ne":
                    break
                elif vyb != "ano":
                    print("Zadejte pouze Ano nebo Ne.")
            
        elif vyber == "o":
            while True:
                o()                            
                vyb = input("Chcete vypocitat dalsi obdelnik? (Ano/Ne): ").lower()
                if vyb == "ne":
                    break
                elif vyb != "ano":
                    print("Zadejte pouze Ano nebo Ne.")
        
        elif vyber =="t":
            while True:
                t()                            
                vyb = input("Chcete vypocitat dalsi trojuhelnik? (Ano/Ne): ").lower()
                if vyb == "ne":
                    break
                elif vyb != "ano":
                    print("Zadejte pouze Ano nebo Ne.")
        elif vyber =="b":
            while True:
                b()                            
                vyb = input("Chcete vypocitat dalsi bzdnu drahu? (Ano/Ne): ").lower()
                if vyb == "ne":
                    break
                elif vyb != "ano":
                    print("Zadejte pouze Ano nebo Ne.")

            
        elif vyber == "q":
            print("Ukoncuju program...")
            time.sleep(3)
            quit()
        else:
            print("Neplatny vyber.")
start()


