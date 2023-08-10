class Circle(object):
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Call the introduce method for each person
person1.introduce()
person2.introduce()


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f} into account {self.account_number}. New balance: {self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f} from account {self.account_number}. New balance: {self.balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance:.2f}")

    def account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance:.2f}")

# Create an instance of the BankAccount class
account1 = BankAccount("123456789", "Alice")

# Perform operations on the account
account1.deposit(1000)
account1.withdraw(200)
account1.check_balance()
account1.account_info()
# dir(BankAccount)
