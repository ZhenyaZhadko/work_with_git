class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def hello(self):
        return f'Hello, my name is {self.name} {self.surname}.'

    def walk(self):
        return 'I can walk!'

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name


person_1 = Person("Alex", "Baker", 28)
print(person_1.name, person_1.surname)

person_2 = Person('Anna', 'Smith', 35)
print(person_2.name, person_2.surname)
print(person_2.hello())
print(person_2.walk())
person_2.name = 'Zhenya'
print(person_2.name, person_2.surname)
print(Person.__dict__)
print(person_1.__dict__)
# получаю значение приватного поля:
print(person_2._Person__age)


class Tester(Person):

    def __init__(self, name, surname, age, framework):
        super().__init__(name, surname, age)
        self.framework = framework

    def test(self):
        return 'I love testing!'


tester_1 = Tester('Borya', 'Popov', 33, 'pytest')
print(tester_1.name)
print(tester_1.framework)
print(tester_1.hello())
tester_1._Person__age = 88
print(tester_1._Person__age)
print(tester_1.__dict__)
tester_1.set_name('Vava')
print(tester_1.get_name())

# class ManualTester(Tester):
#     def __init__(self):
#         super().__init__()
