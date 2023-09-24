def reverseString():
    inputText = input('Write a text to be reversed: ')

    inputText = inputText.split(' ')
    inputText = inputText[::-1]
    inputText = " ".join(inputText)

    print(inputText)

reverseString()