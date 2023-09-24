import random

computer_guess,user_guess = '',''
round_counter = 0
win = False


def generate_number(): 

    global computer_guess

    for i in range(4):
        computer_guess += str(random.randint(0,9))

def ask_for_guess():

    guess = input('Wpisz 4-cyfrową liczbę do zgadnięcia: ')

    while not ( guess.isnumeric() and len(guess) == 4 ):
        guess = input('Wpisz liczbę składającą się z 4 cyfr!: ') 

    global user_guess
    user_guess = str(guess)

def asess_guess():

    global round_counter
    round_counter += 1
    
    score = [0,0]

    for i in range(4):
        if computer_guess[i] == user_guess[i]:
            score[0] += 1
        elif computer_guess.find(user_guess[i]) != -1:
            score[1] += 1

    if score[0] == 4:
        global win 
        win = True
    
    print('Cows: ' + str(score[0]) + ' || Bulls: ' + str(score[1]))

    
if __name__ == '__main__':

    generate_number()

    while not win:

        ask_for_guess()
        asess_guess()

    print('Wygrałeś! Liczba podejść do gry wynosiła:', round_counter)
        
