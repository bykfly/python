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
with open('zp_ip.txt', encoding='utf-8') as my_file:
    my_file = my_file.readlines()
    summ_salary = 0

    for i in my_file:
        name, salary = i.split()

        try:
            salary = float(salary)
        except ValueError:
            continue

        summ_salary += salary
        if salary < 20000:
            print(name)
    print('средний оклад ', round(summ_salary / len(my_file), 2))

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

# задача 5 дз 5
def total():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))

    except ValueError:
        print('Ошибка ввода-вывода')
total()

# задача 6 дз 5
if __name__ == "__main__":
    subjects = {}

    with open('my_file_6.txt', encoding='utf-8') as my_file:
        lines = my_file.readlines()

    for line in lines:
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())

    print(subjects)

# задача 7 дз 5
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('my_file_7.txt', 'r', encoding="utf-8") as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')