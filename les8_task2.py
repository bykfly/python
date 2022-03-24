class Div_Error(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
       x = int(input('Введите числитель:'))
       y = int(input('Введите знаменатель:'))
       if y == 0:
           raise Div_Error('Знаменатель не может быть равен нулю')
    except Div_Error as err:
        print(err)
    else:
        print(x / y)
        break
