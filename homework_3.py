'''
3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
'''
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])
print(my_list[2][0], my_list[2][1], my_list[2][2],)
print('----------------------------')

'''
3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'
'''
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
sum =  0
for i in list_1:
    if isinstance(i, int):
        sum += i
print(sum)
for x in list_1:
    if isinstance(x, str):
        if 'a' in x:
            print(x)
print('----------------------------')

'''
3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
'''
animals = ['cat', 'dog', 'horse', 'cow']
xx = tuple(animals)
print(xx)
print('----------------------------')

'''
3.4. Напишите программу, которая определяет, какая семья больше.
      1) Программа имеет два input() - например, family_1, family_2.
      2) Членов семьи нужно перечислить через запятую.
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
'''
family_1 = input("Enter members of family 1: ").split(',')
family_2 = input("Enter members of family 2: ").split(',')
if len(family_1) > len(family_2):
    print(family_1)
elif len(family_2) > len(family_1):
    print(family_2)
else:
    print('Equal', family_1, family_2)
print('----------------------------')

'''
3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме.
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение
    '''
film = {
    'title': 'Poo',
    'director': 'Woo',
    'year': 2015,
    'budget': 200_000,
    'main_actor': 'Tommy',
    'slogan': 'Buzz Off'
}
print(film.keys())
print(film.values())
print(film.items())
print('----------------------------')

'''
3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
'''
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
total = 0
for i in my_dictionary.values():
    total += i
print(total)
print('----------------------------')

'''
3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
'''
doubles = [1, 2, 3, 4, 5, 3, 2, 1]
doubles_set_only = list(set(doubles))
print(doubles_set_only)
print('----------------------------')

'''
3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга 
'''
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))
dif = set1.difference(set2)
dif.update(set2.difference(set1))
print(dif)
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issubset(set1))
