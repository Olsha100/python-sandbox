file_text = ''
summary = {}

with open('22.txt', 'r') as open_file:
    file_text = open_file.read()

file_text = file_text.split()

for name in file_text:
    if name in summary.keys():
        summary[name] += 1
    else:
        summary[name] = 1
    

print('W teście występuje następująca liczba imion: ')

for k,v in summary.items():
    print(k + ' - ' + str(v) + ' razy')