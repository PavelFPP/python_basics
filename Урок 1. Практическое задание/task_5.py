"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

profit = int(input('Введите значение прибыли'))
expense = int(input('Введите значение издержек'))
if profit <= expense:
    print("Фирма работает без прибыли(в убыток)")
else:
    people = int(input('Ввдите количество работников'))
    marga = profit - expense
    print(f'Финансовый результат - прибыль. Ее величина {marga}')
    rent = float(profit/expense)
    print(f'Рентабельность нашей выручки составит {rent:.2f}')
    marga_person = float(marga/people)
    print(f'Прибыль фирмы в расчете на одного сотрудника {marga_person:.2f}')
