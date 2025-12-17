a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
aCzyB = input("Która liczba ma byc odejmowana/przez ktora liczbe mamy dzielic? (Podaj a albo b): ")
dzialanie = input(" - Mnozenie - Pomnóż a razy b\n - Dzielenie - Podziel a przez b lub b przez a \n - Dodawanie - Dodaj obie licbzy do siebie \n - Odejmowanie - odejmij a od b albo b od a \nWybieram: ")

def mnozenie(a, b):
    print("Po pomnozeniu a razy b wychodzi: ", a * b)

def dzielenie(aCzyB, a, b):
    if aCzyB == "a":
        if b != 0:
            print("Po podzieleniu a przez b wychodzi: ", b / a)
        else:
            print("Nie dzielimy przez 0!")
    elif aCzyB == "b":
        if a != 0:
            print("Po podzieleniu b przez a wychodzi: ", a / b)
        else:
            print("Nie dzielimy przez 0!")
    else:
        print("Nalezy podac przez ktora z liczb chcesz podzielic")

def dodawanie(a, b):
    print("Po dodaniu liczb a oraz b wychodzi: ", a + b)

def odejmowanie(aCzyB, a, b):
    if aCzyB == "a":
        print("Po odjęciu b od a wychodzi: ", b - a)
    elif aCzyB == "b":
        print("Po odjęciu a od b wychodzi: ", a - b)
    else:
        print("Nalezy podac liczbe od ktorej odejmujemy")


if type(a) is int and type(b) is int and aCzyB is str:
    if aCzyB in ["a", "b"]:
        if dzialanie == "Dodawanie":
            dodawanie(a, b)
        elif dzialanie == "Odejmowanie":
            odejmowanie(aCzyB, a, b)
        elif dzialanie == "Mnozenie":
            mnozenie(a, b)
        elif dzialanie == "Dzielenie":
            dzielenie(aCzyB, a, b)
        else:
            print("Wybierz poprawne działanie")
    else:
        print("Masz tylko 2 liczby - a oraz b. Nie możesz wybrać innego symbolu.")
else:
    print("Liczba a albo b nie jest liczbą lub liczba odejmowana/przez ktora chcesz podzielic nie jest literka")

