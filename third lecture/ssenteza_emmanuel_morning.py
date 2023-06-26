# classes
class Human:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        # this is a constructor for class human

    def eat(self, name):
        print(f"{name} is eating")

    def sleep(self, color):
        print(f"A {self.color} man sleeping")

    def walk(self, age, name):
        print(f"At age {age}, {name} is still walking")


# human = Human("john", 21, "red")
# human.eat("John")
# human.walk(12, "Emma")
# human.sleep("blue")
