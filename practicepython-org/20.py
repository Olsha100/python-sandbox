import random

list = random.sample(range(50), k=21)
list.sort()

checked_value = 20

def simple_check():

    global checked_value, is_present
    is_present = False

    for el in list:
        if el == checked_value:
            is_present = True
            
    if is_present:
        print('Liczba '+ str(checked_value) +' znajduje się na liście')
    else:
        print('Liczba '+ str(checked_value) +' nie znajduje się na liście')



def binary_check():

    global checked_value, list

    print('lista: ', list)
    print('-----------------------------------------')

    while len(list) > 1:
        list_length = len(list)
        middle_element_index = list_length // 2

        if list[middle_element_index] > checked_value:
            list = list[:middle_element_index]
        
        elif list[middle_element_index] < checked_value:
            list = list[middle_element_index:]
        
        else:
            print('Liczba '+ str(checked_value) +' znajduje się na liście')
            return

    print('Liczba '+ str(checked_value) +' nie znajduje się na liście')

    

if __name__ == "__main__":
    
    # simple_check()
    binary_check()