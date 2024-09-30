import os

def custom_write(file_name, strings):
    dict = {}
    if os.path.exists(file_name) == False:
        file = open(file_name, 'w+', encoding='utf8')
    else:
        file = open(file_name, 'a', encoding='utf8')
    for s in strings:
        pos = file.tell()
        i = strings.index(s) + 1
        dict[(i, pos)] = s
        file.write(f"{s}\n")
    file.close()
    return dict
    


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)