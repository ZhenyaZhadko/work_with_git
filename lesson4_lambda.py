result = lambda n: n * n
print(result(5))

list_1 = ['hi', 'ananas', 75, None, 'pizza', 100, 69]


def filter_and_sum(lst):
    new_list = []
    for x in lst:
        if isinstance(x, int):
            new_list.append(x)
    print(new_list)
    return sum(new_list)


print(filter_and_sum(list_1))

new_new_list = sum(filter(lambda x: isinstance(x, int), list_1))
print(new_new_list)
print(sum(filter(lambda x: isinstance(x, int), list_1)))
print(list(filter(lambda x: isinstance(x, int), list_1)))
print(list(filter(lambda x: isinstance(x, str), list_1)))
filtered = list(filter(lambda x: isinstance(x, str), list_1))
print(list(filter(lambda i: 'a' in i, filtered)))

filtered2 = list(filter(lambda x: isinstance(x, str) and 'a' in x, list_1))
print(filtered2)


from functools import reduce

result66 = reduce(lambda x, y: x * y, [1, 5, 8, 11, 13])
print(result66)
# reduce: результат перемножения всех чисел [1, 5, 8, 11, 13]

result77 = list(map(lambda x: x ** 2, [1, 5, 8, 11, 13]))
print(result77)
# map: каждый элемент последовательности [1, 5, 8, 11, 13] возведи в квадрат
# filter: фильтрует последовательность по указанному правилу

