class Cell():
    def __init__( self, size ):
        self.size = size

    def __str__( self ):
        return "Количество ячек клетки: {}".format( self.size )

    def __add__( self, other ):
        return Cell( self.size + other.size )

    def __sub__(self, other):
        if self.size <= other.size:
            print('Результат отрицательный')
            raise ValueError
        return Cell(self.size - other.size)

    def __mul__( self, other ):
        return Cell( self.size * other.size )

    def __truediv__( self, other ):
        return Cell( self.size // other.size )

    def make_order(self, count):
        while self.size > 0:
            for i in range(1, count + 1):
                print('x', end='')
                self.size -= 1
                if self.size <= 0:
                    break
            print('\n', end='')

a = Cell(15)
b = Cell(7)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

a.make_order(5)
b.make_order(5)