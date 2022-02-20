class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки: \n Ручка пишет')
class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки: \n Карандаш чертит')
class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки: \n Маркер рисует')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()