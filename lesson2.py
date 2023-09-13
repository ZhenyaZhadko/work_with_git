def iterator(i):
    i = i
    while i != 0:
        print(i)
        i -= 1
        if i == 3:
            continue


iterator(8)

print("********************")

# for i in range(n)

for i1 in range(10):
    print(i1)

for i2 in range(2, 11, 2):
    print(i2)

for i3 in range(1, 11, 2):
    print(i3)

for r in range(10, 1, -2):
    print(r)

# Значения приравненые к bool False: False, None, 0, 0.0, '', [], {}, set()

print(bool(''), bool(None), bool(0.0), bool([]), bool(set()))

f = 10
if f:
    print('True')
else:
    print('False')


def summa(x, y):
    return x + y


def power(n):
    x = summa(5, 8)
    result = x ** n
    return result


print(summa(7, 9))
print(power(5))

age = int(input("Please, enter your age: "))
if age < 18:
    print("Go home now!!")
else:
    print("You're welcome!")
