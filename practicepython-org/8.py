playAgain = 'tak'
gameOptions = ['kamień', 'papier', 'nożyce']

while playAgain == 'tak':
    while True:
        userAInput = input('Gracz 1. Wybierz - kamień, papier lub nożyce: ')
        if gameOptions.count(userAInput) > 0:
            break
        else:
            print('Wpisz jedną z następujących opcji: kamień, papier, nożyce: ')

    while True:
        userBInput = input('Gracz 2. Wybierz - kamień, papier lub nożyce: ')
        if gameOptions.count(userBInput) > 0:
            break
        else:
            print('Wpisz jedną z następujących opcji: kamień, papier, nożyce: ')

    if userAInput == userBInput:
        print('remis')
    elif (userAInput == 'kamień' and userBInput == 'nożyce') or (userAInput == 'nożyce' and userBInput == 'papier') or (userAInput == 'papier' and userBInput == 'kamień'):
        print('Użytkownik 1 wygrał')
    else:
        print('Użytkownik 2 wygrał')


    while True:
        playAgain = input('Czy chcesz zagrać jeszcze raz: ')
        if playAgain == 'tak':
            break
        elif playAgain == 'nie':
            break
        else:
            print('Wpisz tak lub nie: ')
