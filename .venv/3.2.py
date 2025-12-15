# print("-----------------------------------3.2.4-----------------------------------------")
# secret_number = 777
#
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
#
# number = int(input())
#
# while number != secret_number:
#
#         print("Ha ha! utknąłeś w mojej pętli!")
#         number = int(input("Spróbuj jeszcze raz"))
#         if number == secret_number:
#             print("O nieee, zgadłeś, numerek to: ", secret_number)
#             break
#
#
#
# print("-----------------------------------3.2.7-----------------------------------------")
# import time
#
# for i in range(1, 6):
#     print(i, "Mississippi")
#     time.sleep(1)
# print("Gotowy czy nie - NADCHODZE")

# print("-----------------------------------3.2.9-----------------------------------------")
# slowo = input("Wpisz slowo: ")
#
# while slowo != "chupacabra":
#     print("Słowo niepoprawne")
#     slowo = input("Wpisz slowo: ")
#     if slowo == "chupacabra":
#         print("Brawo, zgadles")
#         break
#
# print("-----------------------------------3.2.10-----------------------------------------")
# slowo = input("Podaj slowo: ")
# slowo = slowo.upper()
#
# samogloski = ["A", "O", "E", "I", "U", "Y"]
#
# for letter in slowo:
#     if letter not in samogloski:
#         print(letter)
#         continue

# print("-----------------------------------3.2.11-----------------------------------------")
# slowo = input("Podaj slowo: ").upper()
# samogloski = ["A", "O", "E", "I", "U", "Y"]
# spolgloski = ""
#
# for letter in slowo:
#     if letter not in samogloski:
#         spolgloski += letter
#         continue
# print(spolgloski)

# print("-----------------------------------3.2.14-----------------------------------------")
# klocki = int(input("Podaj ilość klocków: "))
# wysokosc = 0
# zuzyte = 0
#
# while zuzyte + (wysokosc + 1) <= klocki:
#     wysokosc = wysokosc + 1
#     zuzyte += wysokosc
#
#
# print("Wysokość piramidy to: ", wysokosc)

# print("-----------------------------------3.2.14-----------------------------------------")
# liczba = int(input("Podaj liczbe calkowita dodatnia: "))
# counter = 0
#
# if liczba <=0:
#     print("Nie wlasciwa liczba")
# else:
#     while liczba != 1:
#         if liczba % 2 == 0:
#             liczba = liczba / 2
#             print(liczba)
#             counter += 1
#         else:
#             liczba = 3 * liczba + 1
#             print(liczba)
#             counter += 1
#
# print("Ilosc krokow: ", counter)

#print("Podsumowanie")
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# x = 1
# while x < 10:
#     x += 1
#     if(x % 2 == 0):
#         continue
#     else:
#         print(x)

