#задача 1 дз 4
def zp_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {zp_calc() }')

#задача 2 дз 4
a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
spisok = []

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        spisok.append(a[i+1])
print(spisok)

#задача 3 дз 4
if __name__ == '__main__':
    result = (i for i in range(20, 241) if not i % 20 or not i % 21)

    print(f"Is generator object: {result.__class__.__name__ == 'generator'}")
    print(list(result))

#задача 4 дз 4
from functools import reduce


result = reduce(lambda accum, i: accum * i, range(100, 1001, 2))
print('Произведение чисел от 100 до 1000 включительно равно', result)

#задача 5 дз 4
