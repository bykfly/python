# #задача 1 дз 4
# def zp_calc():
#     x = float(input('Введите количество отработанных часов : '))
#     y = float(input('Введите суммы оплаты труда за 1 час : '))
#     c = float(input('Укажите размер премии - '))
#     pay = x * y
#     return pay + c
# print(f'Размер заработной платы составил: {zp_calc() }')
#
# #задача 2 дз 4
# a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# spisok = []
#
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         spisok.append(a[i+1])
# print(spisok)

#задача 3 дз 4
# if __name__ == '__main__':
#     result = (i for i in range(20, 241) if not i % 20 or not i % 21)
#
#     print(list(result))
#
# #задача 5 дз 4
# from functools import reduce
#
# result = reduce(lambda accum, i: accum * i, range(100, 1001, 2))
# print('Произведение чисел от 100 до 1000 включительно равно', result)

#задача 6 дз 4
from typing import Iterable
from itertools import cycle

def get_repeated(iterable: Iterable, count: int):
    """
    Создает генератор на count раз с iterable
    :param iterable: итерируемый повторяемый объект
    :param count: сколько раз повторить
    """

    # if not isinstance(count, int):
    #     raise TypeError(f"count '{count.__class__.__name__}' is illegat type")
    #
    # if count < 0:
    #     raise ValueError(f"count 'can't be less than 0")

    # убираем брекется и получаем стандартный режим работы sycle
    iterator = cycle([iterable])

    while count:
        yield next(iterator)
        count -= 1


if __name__ == '__main__':
    input_data = input('Пожалуйста введите целые числа разделяя их пробелами (максимум 4 числа): ')
    repeate = input('Сколько раз повторить выше введенную последовательность?: ')

    try:
        source_list = [int(i) for i in input_data.split()][:4]
        repeate = int(repeate)
    except ValueError:
        print('Неверно введенные данные')
        exit(1)

    print(list(get_repeated(source_list, repeate)))

