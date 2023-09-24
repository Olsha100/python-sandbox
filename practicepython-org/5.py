import random 

listA = []
listB = []

listALength = random.randrange(1,50)
listBLength = random.randrange(1,50)

for el in range(listALength):
    el = random.randrange(1,20)
    listA.append(el)

for el in range(listBLength):
    el = random.randrange(1,20)
    listB.append(el)


commonList = []

for el in listA:
    if el in listB and el not in commonList:
        commonList.append(el)
        
commonList.sort()

print('List A: ', listA)
print('List B: ', listB)
print('Common elements: ', commonList)
