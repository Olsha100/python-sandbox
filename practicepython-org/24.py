def ask_for_size():
    board_size = input('What size of the board would you like?: ')

    while not board_size.isnumeric():
           board_size = input('Type a number!: ')

    return int(board_size)


def print_board(size):    
    horizontal_pattern = (' ---' * size)
    
    vertical_pattern = ('|   ' * size)
    vertical_pattern = vertical_pattern + '|'
    
    for i in range(size):
        print(horizontal_pattern)
        print(vertical_pattern)

    print(horizontal_pattern)
    
if __name__ == '__main__':
    print_board(ask_for_size())