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

# Exercise calculate the employees bonuses for salary of 0.15 bonus
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        print(f"{self.name} bonus is {self.salary * 0.15}")


# employee1 = Employee("Emmanuel's", 15000)
# employee1.bonus()
# employee2 = Employee("Ssaava's", 23000)
# employee2.bonus()

# Encapsulation example with bank account

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds:")

    def balance(self):
        return self._balance


my_account = BankAccount("1234567890", 1000)

# Access Bank object and modify encupsluted attributes indirectly
my_account.deposit(500)
# print(f"New balance: {my_account._balance}")

my_account.withdraw(100)
# print(f"New balance: {my_account._balance}")

# exercise: Convert temperature Celsiuc to ferenheit


class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def ferenheit(self):
        return (self.__celsius * 9 / 5) + 32


temperature = Temperature(37)

temperature.__celsius = 100

# print(f"{temperature.ferenheit()} Ferenheit")

# Excercise Show encapsulation with employee information to give a pay increamentation
#  (Salary with employee information to new Salary) e.g from 85000 to 100000


class Employee2:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary  # encapsulation is shown here

    def salary(self):
        return f"{self.__salary} is your salary before increment"

    def increment(self, increment):
        return f"{self.__name}'s new salary is {self.__salary + increment}"


employee2 = Employee2("Emmanuel", 20000)
print(employee2.salary())
print(employee2.increment(500))
