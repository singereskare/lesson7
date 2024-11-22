#1. Создайте модуль под названием 'module_1_6.py'

#2. Работа со словарями:

my_dict = {'Ruslan' : 1996, 'Emil' : 1997, 'Rinat' : 1995}
print(my_dict)
print(my_dict.get('Ruslan'))
print(my_dict.get('Anatoly', 'Такого ключа нет'))
print(my_dict)
my_dict.update({'Ayk' : 1999,
                'Vladislav' : 2000})
del my_dict['Emil']
print(my_dict)

#3. Работа с множествами:
my_set = {1, 2, 3, 3, 2, 1, (1, 2, 3), 'number'}
print(my_set)
my_set.add(4)
my_set.add('word')
print(my_set.remove(1))
print(my_set)