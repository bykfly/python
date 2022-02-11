# задача 1 дз 4
def simple_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')

# задача 2 дз 4
a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
answer = []

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        answer.append(a[i+1])

print(answer)

# задача 3 дз 4
if __name__ == '__main__':
    result = (i for i in range(20, 241) if not i % 20 or not i % 21)

    print(list(result))

#задача 4 дз 4
def numers():
    if __name__ == '__main__':
        input_data = input('введите целые числа разделяя их пробелами: ')

    try:
        source_list = tuple(map(int, input_data.split()))
    except ValueError:
        print('Неверно введенные данные')
        exit(1)

    print('выборка чисел', list(numers(lambda x: source_list.count(x) > 1, source_list)))

#задача 5 дз 4
from functools import reduce

result = reduce(lambda accum, i: accum * i, range(100, 1001, 2))
print('Произведение чисел от 100 до 1000 включительно равно', result)

#задача 6 дз 4
from itertools import count

for el in count(int(input('Введите стартовое число '))):
    if el>10:
        break
    print(el)

from itertools import islice, cycle

my_list = ['Истина', 'где-то', 'Рядом']
for el in (islice(cycle(my_list), len(my_list)*3)):
    print(el)

#задача 7 дз 4
from math import factorial

def fact(n: int):

    for i in range(1, n + 1):
        yield factorial(i)
    if __name__ == '__main__':
        i = input('введите количество вычисленных факториалов: ')

    result = (fact())
    print(result)