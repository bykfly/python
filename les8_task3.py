class Error_data(Exception):
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
         while True:
            try:
                val = int(input('Введите значения  '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f'Недопустимое значение ')
                choise = input(f'Попробовать еще раз? Y/N ')

                if choise == 'Y' or choise == 'y':
                    print(try_except.my_input())
                elif choise == 'N' or choise == 'n':
                    return f'Конец ввода данных'
                else:
                    return f'Вы вышли'

try_except = Error_data(1)
print(try_except.my_input())