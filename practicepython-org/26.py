winner_is_2 = [[2, 2, 2],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

is_winner = 0

def check_row(matrix):
    global is_winner
    
    for list in matrix:

        if list[0] == list[1] == list[2] == 1:
            print('Wygrał gracz 1')
            is_winner = 1
            return
        if list[0] == list[1] == list[2] == 2:
            print('Wygrał gracz 2')
            is_winner = 1
            return
        
def check_column(matrix):
    global is_winner

    iterator = 0

    while iterator < 3:

        score = [list[iterator] for list in matrix]
       
        if score == [1,1,1]:
            print('Wygrał gracz 1')
            is_winner = 1
            return
        if score == [2,2,2]:
            print('Wygrał gracz 2')
            is_winner = 1
            return
       
        iterator += 1


def check_diagonal(matrix):
    global is_winner

    if matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] == matrix[2][0]:
        
        if matrix[1][1] == 1:
            print('Wygrał gracz 1')
            is_winner = 1
            return
        if matrix[1][1] == 2:
            print('Wygrał gracz 2')
            is_winner = 1
            return
        
def check_board(matrix):
    
    check_row(matrix)
    check_column(matrix)
    check_diagonal(matrix)

    if is_winner == 0:
        print('Nie wygrał żaden z graczy')

check_board(also_no_winner)