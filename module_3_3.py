def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

vaues_list_2=[54.32, 'Строка']
my_list=[34, 56, 2]
values_list=[123, 'qwe', True]
values_dict={'a': "qwer", 'b': "asdf", 'c': "zxcv"}
print_params()
print_params(8)
print_params(5, 567)
print_params(b = 25)
print_params(c=[1,2,3])
print_params(*my_list)
print_params(*values_list)
print_params(**values_dict)
print_params(*vaues_list_2, 42)