#  в кортеже нельзя изменить элементы,
#  но можно конвертнуть тапл ин лист для этого и обратно
tpl = 1, 2, 3
print(type(tpl))

tpl2 = ("f", "d", "w")
print(type(tpl2))
lst2 = list(tpl2)
lst2[1] = 456
print(lst2)
tpl2 = tuple(lst2)
print(tpl2)

tpl3 = ("f")
print(type(tpl3))

# *args - это произвольное количество аргументов
def sum_it(*args):
    return sum(args)


print(sum_it(2, 22, 44, 55))


def fun(*args):
    for item in args:
        return item * item


print(fun(3, 4, 5))

# methods: .index(), count, sum, min, max, len()
