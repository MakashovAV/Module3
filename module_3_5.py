# Самостоятельная работа по уроку "Рекурсия"
# Цель: применить знания о рекурсии в решении задачи.
#
# Задача "Рекурсивное умножение цифр"


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


print(get_multiplied_digits(40203))
print(get_multiplied_digits(203))
print(get_multiplied_digits(555))
print(get_multiplied_digits(1))
