"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

t = int(input("введите время в секундах до 86 400"))
h = t // 3600
s = (t-h*3600) // 60
c = t-h*3600-s*60
print (f"{h}:{s}:{c}")
