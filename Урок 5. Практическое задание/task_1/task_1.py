"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
out_f = open("dz_1.txt", "w", encoding='utf-8')
str_list = ['Заместитель командира по вооружению –\n', 'начальник отдела вооружения\n', 'войсковой части 00000\n']
out_f.writelines(str_list)
out_f.close()
