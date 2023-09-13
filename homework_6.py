class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def speak(self):
        return f'I can make sounds!'

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f'I can meow!'

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f'I can bark!!'

cat1 = Cat('Kasya', 8, 'persian')
dog1 = Dog('Pow', 77, 'pug')
print(cat1.get_name())
cat1.set_name('Tom')
print(cat1.__dict__)
print(Cat.__dict__)
print(cat1._Animal__name)
print(cat1.speak())
print(dog1.speak())
