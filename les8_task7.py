class ComplexNumber:
    def __init__(self, real, image):
        self.a = real
        self.b = image

    def __add__(self, other):
        print(f'Сумма комплексных чисел равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел равно')
        return f'z = {self.a * other.a} + {self.b * other.b} * i'

    def __str__(self):
        return f'Комплексное число = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)