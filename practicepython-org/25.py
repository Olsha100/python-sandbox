computer_guess = 0
try_number = 1
start_el_index = 0
end_el_index = -1

def check_number():
    global try_number 
    
    user_answer = input('Is this your number ? ' + str(computer_guess) + ' :')

    while not user_answer in ['yes','y','no','n']:
        user_answer = input('Type yes or no: ')

    if  user_answer.lower() in ['yes', 'y']:
        print(f"It took {try_number} times to guess the number.")
        return
    else:
        try_number += 1
        
        generate_guess()
        check_number()
        

def generate_guess():
    global computer_guess 
    full_list = list(range(1,101))
    

    start_el = full_list[start_el_index]
    end_el = full_list[end_el_index]

    if computer_guess == start_el:
        computer_guess = end_el
    else:
        computer_guess = start_el
    
    
check_number()