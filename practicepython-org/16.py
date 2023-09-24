import random
import string

def ask_password_length():
    pass_length = input('Napisz ile znaków ma zawierać hasło: ')

    while not pass_length.isnumeric():
        
        print('-----------------------------------------------' + 
              '\n' + 
              'Długość hasła ma być wyrażona liczbą całkowitą!'+ 
              '\n' + 
              '-----------------------------------------------')
        
        pass_length = input('Napisz ile znaków ma zawierać hasło: ')

    return int(pass_length)

def random_element( value ):
   return value[random.randint(0,len(value) - 1)]


def generate_password( pass_length ):

    password = ''

    charType = ['small_letter','big_letter','number','special_character']
    pass_pattern = random.choices(charType, k = pass_length)

    small_letters = string.ascii_lowercase
    big_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    for el in pass_pattern:

        if el == 'small_letter':
            password += random_element(small_letters)
        elif el == 'big_letter':
            password += random_element(big_letters)
        elif el == 'number':
            password += random_element(numbers)
        else:
            password += random_element(special_characters)
    
    print('Wygenerowane hasło:' + '\n', password)

generate_password(ask_password_length())