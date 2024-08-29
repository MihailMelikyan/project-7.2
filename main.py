import io
from pprint import pprint
def custom_write(file_name, strings):
    with open(file_name,'w',encoding = 'utf-8') as file:
        line = 0
        string_position = dict()
        for string in strings:
            line += 1
            position = file.tell()
            string_position[(line,position)] = string
            file.write(string +'\n')
    file.close()
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
