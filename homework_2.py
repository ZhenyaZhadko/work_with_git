# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
health = int(input("Enter health level: "))
if health <= 0:
    print("False")
else:
    print("True")


def health_level_check():
    health1 = int(input("Enter health level: "))
    if health1 <= 0:
        print("False")
    else:
        print("True")


health_level_check()

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Четное")
else:
    print("Нечетное")


def even_odd_number_check():
    number1 = int(input("Enter a number: "))
    if number1 % 2 == 0:
        print("Четное")
    else:
        print("Нечетное")


even_odd_number_check()

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008)
# и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
year = int(input("Enter a year: "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("YES, it's a leap year")
else:
    print("NO, it's not a leap year")

# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()
text = input("Insert the text: ")
repetition = int(input("Enter a number of repetitions: "))
i = 0
for i in range(repetition):
    print(text)
    i += 1


def method_print_text():
    text1 = input("Enter a text: ")
    repetition1 = int(input("Enter number of repetitions: "))
    for i1 in range(repetition1):
        print(text1)
        i1 += 1


method_print_text()

# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}


def calculator():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter a operation sign: ")
    if operator == "+":
        result = num1 + num2
        print(f'{num1} {operator} {num2} = {result}')
    elif operator == "-":
        result = num1 - num2
        print(f'{num1} {operator} {num2} = {result}')
    elif operator == "*":
        result = num1 * num2
        print(f'{num1} {operator} {num2} = {result}')
    elif operator == "/":
        result = num1 / num2
        print(f'{num1} {operator} {num2} = {result}')
    elif operator == "//":
        result = num1 // num2
        print(f'{num1} {operator} {num2} = {result}')
    elif operator == "%":
        result = num1 % num2
        print(f'{num1} {operator} {num2} = {result}')
    else:
        print("The calculator doesn't support such operation")


calculator()
