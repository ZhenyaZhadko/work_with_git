# встроенные функции: min
min_item = min(20, 55, 88, 3)
print(min_item)


def person(age, first_name='DefaultName', last_name='DefaultFamilyName'):
    return f"Hello, my name is {first_name} {last_name}. I'm {age} years old."


print(person(88, "Anna", "Smith"))
print(person(77))
print(person(last_name="Bosyak", first_name="Ron", age=12))


def pattern(length, char1='', char2='*'):
    return (char1 + char2) * length + char1


print(pattern(9))
print(pattern(9, char1='/'))


# декораторы нужны для вычисления времени выполнения функции
def decorator_function(func):
    def wrapper(*args):
        print('Wrapper function')
        print(f'Wrapped function: {func.__name__}')
        print(f'Wrapped function with arguments: {args}')
        print('Wrapped function in process')
        print(func(*args))
        print('Exiting wrapper')

    return wrapper


@decorator_function
def hello(item):
    return f'I\'m a wrapped function, {item} is wrapped'


hello('Candy')

# пространства имен or namespace:
# local, enclosed, global, built-in
x = 15
y = 25


def sum_it(x, y):
    print(f'Locals: {locals()}')
    return x + y


print(f'Inside the function: {sum_it(10, 8)}')
print(f'Outside the function: {x + y}')
print(f'Globals: {globals()}')

name = 'Alice'


def outer_function():
    # name = 'Olga'
    def inner_function():
        # name = 'John'
        return name
    return inner_function


closure = outer_function()
result = closure()

print(result)
