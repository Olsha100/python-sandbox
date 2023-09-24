userInput = input('Write a word which to check whether is a palindrome: ')

for i in range(len(userInput)):

    if userInput[i] != userInput[-i-1]:
        print(userInput + ' is not a palindrome')
        break
    elif i == len(userInput) - 1: 
        print(userInput + ' is a palindrome')        