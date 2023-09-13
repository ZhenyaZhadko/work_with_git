# data structures
# LISTS
list_numbers = list(map(int, input().split()))
print(sum(list_numbers) / len(list_numbers))

lst = [10, 24, 'hello', None, True, 24, 25.01]
print(id(lst))
print(lst)
print(lst[5], lst[-1])
print(lst.count(24))
print(lst.index(24))
lst4 = [x for x in lst if isinstance(x, int)]
print(len(lst4))
print("--------------")

# methods of lists:
# append, insert, index(индекс первого такого эл-та в списке),
# clear, remove, reverse,
# count(сколько раз встречается опред. значение), sun, min, max
# sort

print(len(lst))
text = "Bye"
lst.append(text)
print(lst)

lst[-1] = 100
print(lst)

lst.reverse()
print(lst)

lst2 = [x for x in lst if isinstance(x, int)]
# lst2 = []  тоже самое. что и верхняя строка с генерацией
# for i in lst:
#     if isinstance(i, int):
#         lst2.append(i)
print(lst2)
print(sum(lst2))
print(min(lst2))
print(max(lst2))

print(id(lst))

# генерация списков
l = [1, 20, 3, 40, 5, 16]
new_l = [x * x for x in l if x % 2 == 0]
print(new_l)

# sorted не изменяет первоначальный список!!
l66 = sorted(l)
print(l66)

# method sort returns None!! меняет список !!!
#l.sort()
print(l)



