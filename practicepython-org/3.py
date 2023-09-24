array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for element in array:
#     if element > 5:
#         print(element)


### Rozwiązanie gdzie użytkownik sam wskazuje liczbę graniczną
# userNumber = int(input('Wpisz liczbę graniczną do sprawdzenia  w tablicy: '))

# for el in array:
#     if el > userNumber:
#         print(el)


### Rozwiązanie w którym tworzony jest oddzielna lista na podstawie warunku 

newArray = []

for el in array:
    if el > 5:
        newArray.append(el)

print(newArray)