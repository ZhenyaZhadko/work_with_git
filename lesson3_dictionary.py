my_dict = {
   'name' : 'Alex',
    'last_name': 'Smith',
    'age': 25,
    'dep': 'DEV',
}

print(my_dict)
print(my_dict['name'])
my_dict['dep'] = 'HR'
print(my_dict)
my_dict['salary'] = 50000
print(my_dict)
print(my_dict.pop('salary'))
print(my_dict)
print(my_dict.get('salary', 'If not found by such key - this text will be shown'))

#  methods: keys, values, items(пары кл-зн), get, clear, copy, len, type, min, max
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(len(my_dict))


def keywords(**kwargs):
    return kwargs


print(keywords(name='Alice', last_name='55'))
