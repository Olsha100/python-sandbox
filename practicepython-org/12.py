import random

def askForList():
	print('********************************************* ')
	print(' Stwórz listę losowych liczb z danego zakresu ')
	print('********************************************* ' + '\n')

	listStart = input('Wpisz początkowy zakres listy: ')
	while not listStart.isnumeric():
		listStart = input('Wartość początkowa ma być liczbą!: ')

	listEnd = input('Wpisz końcowy zakres listy: ')
	while not listStart.isnumeric():
		listEnd = input('Wartość końcowa ma być liczbą!: ')

	listStart = int(listStart)
	listEnd = int(listEnd)
	
	# random.sample zwraca k-elementową listę elementów wybranych spośród listy przekazanej do niej w pierwszym argumencie
	# przekazywana lista jest pierwszym argumentem, k, które trzeba zdefiniować dosłownie jest drugim argumentem
	# # range wypisuje listęs składającą się po kolei z elementów w zakresie [ start, stop ) więc trzeba
	# # dodać 1 do elementu końcowego aby liczba końcowa też była brana pod uwagę w wypisywanej liście.
	# # # k nie może być < 0 oraz k nie może być większe niż długość listy z której następuje próbkowanie ! 
	return random.sample(range(listStart, listEnd + 1),k = random.randrange(listStart, listEnd))

def listReductor(arr):
	print('Oryginalna lista: ', arr)
	print('Zredukowana lista: ', [el for el in arr if el == arr[0] or el == arr[-1] ])

listReductor(askForList())