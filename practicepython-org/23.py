file_a = file_b = file_common = ''


with open('23-a.txt','r') as file_23_a:
    file_a = file_23_a.read()


with open('23-b.txt','r') as file_23_b:
    file_b = file_23_b.read()

file_a = file_a.split()
file_b = file_b.split()

file_common = [el for el in file_a if el in file_b]

with open('23-common.txt', 'w') as file_23_common:
    for el in file_common:
        file_23_common.write(str(el) + '\n')