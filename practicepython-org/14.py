def removeDuplicatesWithSet(arr):
	print(list(set(arr)))

def removeDuplicatesWithLoop(arr):
	uniqueArr = []
	
	for el in arr:
		if el not in uniqueArr:
			uniqueArr.append(el)
	
	print(uniqueArr)

a = [1,2,2,3,4,6,2,5]

print('List deduplicated using set method: ')
removeDuplicatesWithSet(a)

print('* * * \n * * * ')

print('List deduplicated using loop: ')
removeDuplicatesWithLoop(a)