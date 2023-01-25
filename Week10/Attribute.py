class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark (self):
        print("Woof Woof!")

    def get_age(self):
        return self.age

dog1 = Dog("Fido", 3)
print(dog1.name)
dog1.bark()
print(dog1.get_age())


__init__ is a special method in Python classes, also known as a constructor. It is automatically called when an object of the class is created, and it allows you to set the initial state of the object.
The __init__ method takes at least one argument, self, which refers to the object being created. self is a convention in Python, and it is used to refer to the current object.

