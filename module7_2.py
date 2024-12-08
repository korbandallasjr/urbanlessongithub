def custom_write(file_name, strings):
     string_positions = {}
     file = open(file_name, 'r+', encoding='utf-8')
     for value in strings:
         index = strings.index(value)
         file.write(f'{strings[index]}\n')
         string_positions[(index+1, file.tell())] = value
     return string_positions
     file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)