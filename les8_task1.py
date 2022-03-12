class Data:
    def __init__(self, day_month_year):
       self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Правильный ввод данных'
                else:
                    return f'Проверьте год'
            else:
                return f'Проверьте  месяц'
        else:
            return f'Проверьте день'

today = Data('13 - 3 - 2022')

print(Data.valid(13, 3, 2022))
print(today.valid(3, 13, 2022))
print(Data.extract('1 - 1 - 2022'))
print(today.extract('11 - 11 - 2020'))

