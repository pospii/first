print("Vítejte v kalkulačce!\n")


while True:
    print("Vyberte si operaci:\n1 - sčítání\n2 - odečítání\n3 - násobení\n4 - dělení")
    operace = int(input())
    if operace == 1 or operace == 2 or operace == 3 or operace == 4:
        print("Nyní zadejte postupně dvě čísla:")
        a = int(input("a = "))
        b = int(input("b = "))
        if operace == 1:
            vysledek = a + b
            print(f"Výsledek: {vysledek}")
        elif operace == 2:
            vysledek = a - b
            print(f"Výsledek: {vysledek}")
        elif operace == 3:
            vysledek = a * b
            print(f"Výsledek: {vysledek}")
        elif operace == 4:
            vysledek = a / b
            print(f"Výsledek: {vysledek}")
        else:
            print("Nevím jak se ti to podařilo, ale rozbils to")
    else:
        print("Zadejte pouze číslo podporované operace!")
    break
    