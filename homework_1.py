# 1.1
# 2) Напишите и запустите программу.которая выводит строку "Hello world!"
print("Hello world!")

# 3) Напишите программу, которая на входе получает имя пользователя, сохраняет его  в
# переменную  user_name и  выводит строку "Hello {user_name}!"
user_name = input("Write your name, please: ")
print(f"Hello {user_name}!")

# 4) Напишите программу, которая на входе получает 2  числа, производит с ними
# арифметическую операцию(на ваше усмотрение), и выводит “Результат = {результат}”.
a, b = map(int, input().split())
result = a * b
print(f"Результат = {result}")

# 1.2
# 1) Напишите программу, чтобы вывести:
#
# ** ** ** ** *
# *           *
# *           *
# ** ** ** ** *
print('''
** ** ** ** *
*           *
*           *
** ** ** ** *''')

# 1.3. **
# Напишите программу для нахождения цифр четырёхзначного числа.Число вводится
# при помощи методa input()
#
# Пример: Input: 3498
#
# Output:
# Тысячи - 3
# Сотни - 4
# Десятки - 9
# Единицы - 8
a = int(input("Insert your number: "))
a1 = a % 10
a10 = a % 100 // 10
a100 = a % 1000 // 100
a1000 = a // 1000
print(f"Тысячи - {a1000}")
print(f"Сотни - {a100}")
print(f"Десятки - {a10}")
print(f"Единицы - {a1}")

# второй способ решения
b = input("Insert your number: ")
print(f"Тысячи - {b[-4]}")
print(f"Сотни - {b[-3]}")
print(f"Десятки - {b[-2]}")
print(f"Единицы - {b[-1]}")
