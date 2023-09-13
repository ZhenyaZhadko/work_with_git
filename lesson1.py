from lesson2 import iterator

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

number = 10
print(number)
print(type(number))
# ячейка в памяти, переменная хранит ссылку на область в памяти, а не само значение
print(id(number))

number1 = number
print(id(number1))

number2 = 10
print(id(number2))
number2 = 20
print(id(number2))

print("----------------")

name = "Bob"
print(name)
print(type(name))

# int float bool str None
boolean = True
print(type(boolean))

noon = None
print(type(noon))

# type casting, приведение типов
print(name + " " + str(number2))
number3 = "66"
number4 = int(number3)
print(type(number4))
print(number2 + int(number3))

#  матем операции: *   **(возведение в степень) + - /    //(целочисленное делен) %(остаток от деления)

# input str
rot = input("Print a name:")
print("Hello, " + rot)
print('Hello, {}'.format(rot))
print(f'Hello, {rot}')

# input int
rat = int(input("Print a number:"))

iterator(4)
