def askForSequenceLength():
	sequenceLength = input('Jak długi ciąg Fibonacciego wygenerować?: ')

	while not sequenceLength.isnumeric():
		sequenceLength = input('Wpisz liczbę!: ')

	return int(sequenceLength)

def fibonacci( num ):
	fibList = [1,1]

	if num > 2:
		while len(fibList) < num:
			fibElement = fibList[-1] + fibList[-2]
			fibList.append(fibElement)
	else:
		fibList = fibList[0:num]
			
	print('Ciąg Fibonacciego ' + str(num) + ' elementów to: ', fibList)

fibonacci(askForSequenceLength())