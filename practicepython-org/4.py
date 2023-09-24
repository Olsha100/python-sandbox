# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input('Wpisz liczbę, której dzielniki chcesz znaleźć: '))

elements = range(2,num) # 1 jest dzielnikiem każdej liczby więc nie ma sensu jej sprawdzać

divisorsList = []

for el in elements:
    if num % el == 0:
        divisorsList.append(el)

print('Dzielniki liczby ' + str(num) + ' to: ', divisorsList)