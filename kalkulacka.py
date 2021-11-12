vysledky = []

def pozdrav():
    print("Vítejte v kalkulačce!\n")

def pokracovani():
    pokracovat = input("Přejete si pokračovat v počítání? ano/ne\n")
    if pokracovat == "ano":
        kalkulacka()
    elif pokracovat == "ne":
        print("V tom případě děkuji za použití kalkulačky.")
        print (f"Všechny vaše výsledky: {vysledky}")
    else:
        print("Zadejte pouze ano nebo ne")
        pokracovani()



def kalkulacka():
    print("Vyberte si operaci:\n1 - sčítání\n2 - odečítání\n3 - násobení\n4 - dělení")
    operace = int(input())
    if operace == 1 or operace == 2 or operace == 3 or operace == 4:
        print("Nyní zadejte postupně dvě čísla:")
        
        kontrola()
        if operace == 1:
            vysledek = a + b  
        elif operace == 2:
            vysledek = a - b   
        elif operace == 3:
            vysledek = a * b
        elif operace == 4:
            vysledek = a / b
        else:
            print("Nevím jak se ti to podařilo, ale rozbils to")
        print(f"Výsledek: {vysledek}")
        vysledky.append(vysledek)
    else:
        print("Zadejte pouze číslo podporované operace!")
    pokracovani()

def kontrola():
    a = input("a = ")
    b = input("b = ")
    if a.isdigit == True and b.isdigit == True:
        a = float(a)
        b = float(b)
    else:
        print("Zadal jsi písmeno")
        kalkulacka()
    
        
pozdrav()
kalkulacka()