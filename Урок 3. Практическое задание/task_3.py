"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(a, b, c):
    z = [a, b, c]
    y = sorted(z, reverse=True)
    return y[1]+y[0]


print(my_func(int(input('первый аргумент')), int(input('второй аргумент')), int(input('третий аргумент'))))
