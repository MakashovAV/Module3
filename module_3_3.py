# Домашнее задание по уроку "Распаковка позиционных параметров".
# Цель задания: Освоить создание функций с параметрами по умолчанию и практику вызова этих функций с различным количеством аргументов.


def  print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params()
print_params(1,2,3)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, False, 'стр']
values_dict = {'a': 222, 'b': 'string', 'c': 0.5}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3456, 'второй']
print_params(*values_list_2, 42)