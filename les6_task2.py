class Road:
    __length = None
    __width = None
    weigth_1m2 = 25
    tickness = 0.05
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def massa(self):
        massa = self.length * self.width * self.weigth_1m2 * self.tickness / 1000
        print(f'Масса асфальта {massa} тонн')

trassa_m95 = Road(20000, 20)
trassa_m95.massa()