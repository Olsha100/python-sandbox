import random

counter = 0

while True:
	counter += 1
	print('Grasz ' + str(counter) + ' raz')
	
	guessNumber = random.randint(1,9)
	userNumber = input('Zgadnij jaką liczbę wylosował komputer z przedziału 1-10: ')
	
	while not userNumber.isnumeric():
		userNumber = input('Wpisywana wartość musi być liczbą! : ')
	
	userNumber = int(userNumber)
	
	if userNumber > guessNumber:
		print('Twoja liczba jest zbyt duża')
	elif userNumber < guessNumber:
		print('Twoja liczba jest zbyt mała')
	else:
		print('Trafiłeś!')
	
	playAgain = input('Czy grasz jeszcze raz? Wpisz tak lub nie: ')

	while playAgain != 'tak' and playAgain != 'nie':
		playAgain = input('Wpisz tak lub nie!: ')

	if playAgain == 'nie':
		break