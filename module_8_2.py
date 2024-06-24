class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = 'InvalidDataException' + '. ' + message

class ProcessingException(Exception):
    def __init__(self, message):
        self.message = 'ProcessingException' + '. ' + message

def quadratic_equations(a, b, c):
    try:
        a, b, c = int(a), int(b), int(c)
    except:
        raise InvalidDataException('Можно вводить только числа!')
    d = int(b) ** 2 - 4 * int(a) * int(c)
    if d < 0:
        raise ProcessingException('Ахтунг, у этого уравнения нет корней!')
    elif d == 0:
        print(f'Единственный корень: {-b / (2 * a)}')
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(f'Корни этого уравнения: {x1} и {x2}.')

# print('Давайте решим квадратное уравнение! Принимаются только целые числа.')
# a = input('Введите старший коэффициент: ')
# b = input('Введите средний коэффициент: ')
# c = input('Введите свободный член: ')
# try:
#     quadratic_equations(a, b, c)
# except Exception as e: #Перехватываем обе возможные ошибки
#     print(f'Капитан, на борту ошибка: {e.message}') #Выводим соответствующее сообщение об ошибке

def solution(a, b, c):
    try:
        quadratic_equations(a, b, c)
    except Exception as e:
        print(f'Капитан, на борту ошибка: {e.message}')

print('Пример вызова первой ошибки')
solution('a', 'b', 'c')
print('Пример вызова второй ошибки')
solution(1, 0, 1)
print('Пример решения уравнения с одним корнем')
solution(1, 2, 1)
print('Пример решения уравнения с двумя корнями')
solution(1, 4, 1)