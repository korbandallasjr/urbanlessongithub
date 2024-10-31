def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# списки и словари по заданию
values_list = [1, 'строчка_точка', False]
values_dict = {'a': 'Вася', 'b': 2, 'c': True}
values_list_2 = [54.32, 'Строка']
# вызовы функции с разным количеством параметров
print_params()
print_params(16, 'random')
print_params('random3', True, 28)
# работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)
print_params(c=[1, 2, 3])
# распаковка списка и словаря
print_params(*values_list)
print_params(**values_dict)
# распаковка списка + отдельный параметр
print_params(*values_list_2, 42)
