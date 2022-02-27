class Matrix:
    def __init__(self, arr):
            self.arr = arr

    def __str__(self):
        return '\n'.join(str(s) for s in self.arr)

    def __add__(self, other):
        len_of_matrix = len(self.arr[0])
        hig_of_matrix = len(self.arr)
        if not (len_of_matrix == len(other.arr[0]) and hig_of_matrix == len(other.arr)):
            print("К сложению принимаются матрицы одинаковых размеров.")
            raise ValueError
        result = [[self.arr[y][x] + other.arr[y][x] for x in range(len_of_matrix)]
                  for y in range(hig_of_matrix)]
        return Matrix(result)

matrix1 = Matrix([ [3,2,1],[2,3,4],[5,6,7] ])
matrix2 = Matrix([ [6,0,-1],[5,4,0],[4,3,-2] ])

print( 'сумма матриц:', matrix1 + matrix2, end = '\n\n', sep = '\n' )




