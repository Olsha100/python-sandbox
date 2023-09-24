userNumber = int(input("Wpisz liczbę: "))
divider = int(input("Wpisz przez co miałaby być podzielna: "))

if userNumber % divider == 0:
    print('Liczba ' + str(userNumber) + ' jest podzielna przez ' + str(divider))
else:
    print('Liczba ' + str(userNumber) + ' nie jest podzielna przez ' + str(divider))