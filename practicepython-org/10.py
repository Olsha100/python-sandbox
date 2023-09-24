import random 

# Wybierz liczby od 1 do 1000. Będą to długości list.
listArange = random.randint(1,1000)
listBrange = random.randint(1,1000)

# Metoda sample modułu random ma dwa argumenty - pierwszy to lista elementów z których losowo wybiera elementy, drugi to liczba elementów do wybrania
# Metoda range zwraca listę elementów. W przypadku poniższego kodu zwraca listę [1,2,3,...,1000] 
a = random.sample(range(1000), listArange)
b = random.sample(range(1000), listBrange)

# Metoda set zwraca obiekt podobny do listy ale nie zawierający zduplikowanych elementów. 
# Aby zamienić go ponownie w listę należy wszystko objąć metodą list()
commonList = list(set([x for x in a if x in b]))

print('Lista nr 1: ', a)
print('Lista nr 2: ', b)

if len(commonList) > 0:
	print('Elementy wspólne dla obu list: ', commonList)
else:
	print('Brak elementów wspólnych dla obu list.')