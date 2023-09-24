def takeNumber():
	userNumber = input('Wpisz liczbę do sprawdzenia: ')

	while not userNumber.isnumeric():
		userNumber = input('Wpisz liczbę !: ') 

	return int(userNumber)

def isPrimary( value ):
	divisors = [2,3,5,7]

	for el in divisors:
		if value % el == 0 and value != el:
			return False
			
	return True

def printResult( result, value ):
	if result == True:
		print('Liczba ' + str(value) + ' jest liczbą pierwszą')
	else:
		print('Liczba ' + str(value) + ' nie jest liczbą pierwszą')

number = takeNumber()
printResult(isPrimary(number), number)