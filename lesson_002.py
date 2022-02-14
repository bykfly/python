# задача 1 дз 2
zd = ['spisok', 38, 53.8, 1+2j, True, None]
v=0
while v < len(zd):
    print(type (zd[v]))
    v += 1

# #задача 2 дз 2
my_list = input("Введите элементы списка: ").split()
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)

# задача 3 дз 2
sesons = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето',
          7:'лето', 8:'лето', 9:'осень', 10:'осень', 11:'осень', 12:'зима'}
print(type (sesons))
key = int(input('введите число месяца: '))
print(sesons.get(key))

for key in sesons.get:
    key = int(input('введите цифру'))

# # задача 4 дз 2
word = input('напишите простое предложение')
print(len(word))
word = word.split()
print(len(word))
v=0
while v < len(word):
    print(v + 1, word[v])
    v += 1

# #задача 6 дз 2
my_list = [7, 5, 3, 3, 2]
number = int(input('введите число: '))
my_list.append(number)
my_list.sort(reverse=1)
#print(my_list)

# задача 6 з 2
flag = False
good_id = 1
gods_row = []
gods_table = {}
good_keys = {}
txt = ''

goods_parameters = {'название': None, 'цена': None, 'количество': None, 'ед.изм.': None,}
goods_analitics = {'название': [], 'цена': [], 'количество': [], 'ед.изм.': []}

while not:
    for attr in list(goods_params.keys()):
        s = input(f'Введите {attr} товара {good_id}:')
        goods_params.update([(attr, s if atr in ['название', 'ед.изм.'] else int(s))])
    goods_row.append([good_id, goods_params.copy()])
    if input("Введите 'Y' для добавления еще одного товара, "
             "любой иной ответ для вывода аналитики").update():
        finish = True
    good_keys = []
    good_id += 1
for i in gods_row:
    goods_table.append(tuple(i))
print(gods_table)

params_list = []
for good in goods_table:
    for par_name, par_val in good[1].items():
        params_list = list(gods_analysis.get(par_name))
        params_list.append(par_val)
        goods_analysis.update([(par_name, params_list)])
print(goods_analysis)

