import re

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

full_fields = 0

def player_move(player_sign):
    global full_fields, board

    while True:
        player_input = input( f'Wpisz koordynaty pola na którym chcesz postawić {player_sign}, w formie wiersz,kolumna: ' )

        # Check if the player's input is in a proper format and the coordinates are betwen 1 and 3
        regex = re.compile(r"[1-3],[1-3]")
        while not re.fullmatch(regex, player_input):
            player_input = input(f'Wpisz koordynaty {player_input} w formacie "x,y", gdzie x i y są liczbami z zakresu 1-3 !: ')

        # Format the coordinates to a list of integers
        player_input = player_input.split(',')
        player_input = [int(el) for el in player_input]

        x_coordinate = player_input[0] - 1
        y_coordinate = player_input[1] - 1

        # Fulfill the board field checking at first if it is empty
        if board[x_coordinate][y_coordinate] == 0:
            board[x_coordinate][y_coordinate] = player_sign
            print('Aktualny stan planszy: ', board)
            return
        else:
            print('To pole na planszy jest już wypełnione!')

if __name__ == '__main__':

    while full_fields < 9: 
        player_move('x')
        player_move('o')