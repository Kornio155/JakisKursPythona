"""
print("-----------------------------3.1.11----------------------------")
income = float(input("Wpsiz swoje dochody: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
elif income > 85528:
    tax = 14839.02 + (income - 85528) * 0.32

if tax <= 0:
    tax = 0.0

tax = round(tax, 0)
print("Podatek wynosi: ", tax)
"""

print("-----------------------------3.1.12----------------------------")
year = int(input("Wpsiz swoje dochody: "))

if year < 1582:
    print("Wtedy nie było jeszcze podziału na przestępny i nie.")
else:
    if year % 4 != 0:
        print("Rok", year, "nie jest przestępny")
    elif year % 100 != 0:
        print("Rok", year, "jest przestępny")
    elif year % 400 != 0:
        print("Rok", year, "nie jest przestępny")
    else:
        print("Rok ", year, "jest przestępny")
