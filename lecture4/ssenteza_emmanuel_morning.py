# inheritance Examples

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking")


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def meow(self):
        print(f"{self.name} is meowing")

# dog = Dog("Fido", "Lab")

# multiple inheritance


class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Flayable:
    def fly(self):
        print(f"{self.name} is flying")


class Bird(Animals, Flayable):
    # this is where we show multiple inheritance
    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings

    def display(self):
        super().display(self)
        print(f"{self.name} has {self.wings} wings")


# create the bird object
bird = Bird("Pigeon", 4)
# bird.fly()
# bird.display()

# Method overriding


class Animal:

    def make_sound(self):
        print(f"Animal is making sound")


class Dog(Animal):
    def make_sound(self):
        print(f"Dog is barking")


class Cat(Animal):
    def make_sound(self):
        print(f"Cat is meowing")


def make_animal_sound(animal):
    animal.make_sound()


animal = Animal()
dog = Dog()
cat = Cat()
# make_animal_sound(cat)

# polymorphism allows yout o write code that can work with different objects
