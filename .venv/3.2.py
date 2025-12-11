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

print("-----------------------------------3.2.9-----------------------------------------")
slowo = input("Wpisz slowo: ")

while slowo != "chupacabra":
    print("Słowo niepoprawne")
    slowo = input("Wpisz slowo: ")
    if slowo == "chupacabra":
        print("Brawo, zgadles")
        break