# задача 1 дз 3
def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'error'
print(div(3,2))

#задча 2 дз 3
def anketa(**kwargs):
    return list(kwargs.values())
print(anketa(name=input('имя: '),
            s_name=input('фамилия: '),
            b_date=input('год рождения: '),
            l_town=input('город: '),
            email=input('email: '),
            tel=input('телефон: ')))

#задча 3 дз 3
def summa(a, b, c):
    s = [a, b, c]
    s.remove(min(a, b, c))
    return sum(s)
print(summa(1, 6, 2))

#задча 4 дз 3
def extent(x, y):
    return 1 / x ** abs(y)
print(extent(5, -2))

def extent_2(a,b):
    i=-1
    result = a
    while i > b:
        result = result * a
        i -= 1
    return (1 / result)
print(extent_2(5,-2))

#задча 5 дз 3
def total():
    i=0
    while True:
        spisok = (1, 2, '$', 3, 4).split()
        #spisok = list(spisok)
        if '$' not in spisok:
            i += summa(spisok)
        else:
            del '$' in spisok
            i += summa(spisok)
            print(s)

    return(total())
print(total())


#задча 6 дз 3
def capital(text):
    return(text.title())
text = 'о сколько нам ошибок трудных готовит просвещенья дух'
print(capital(text))