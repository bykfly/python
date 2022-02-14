# задача 1 дз 5
my_f = open('out_file.txt', 'w', encoding='utf-8')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
        my_f.close()

# задача 2 дз 5
my_file = open('my_file_1.txt', 'r')
content = my_file.readlines()

print(f'Количество строк в файле - {len(content)}')

for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')

my_file.close()


# задача 3 дз 5
with open('zp_ip.txt', 'r', encoding='utf-8') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
            sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')

# задача 4 дз 5
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text.txt', 'r', encoding='utf-8') as file_obj:

    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('text_new.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)
