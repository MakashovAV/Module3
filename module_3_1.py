# Цель: применить на практике начальные знания о пространстве имён и оператор global.
# Закрепить навыки из предыдущих модулей.

# Задача "Счётчик вызовов":

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (x.lower() for x in list_to_search)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Hello, world!'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(is_contains('321', ['123', '321, ', '222', '321']))
print(is_contains('HhH', ['hH', 'rohhan, ', '', 'Hhhhagrid']))
print(calls)
