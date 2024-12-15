# Task 1: Create User class
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    # Task 2: Add User class instance methods
    def change_name(self, new_name):
        self.name = new_name
    
    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password

# Task 3: Create BankUser subclass
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    # Task 4: Add BankUser class instance methods
    def show_balance(self):
        print(f'Balance: {self.balance:.2f}')

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    # Task 5: Transfer and request money
    def transfer_money(self, amount, recipient):
        print(f'{amount} to {recipient.name}')

        print('Authprization required')
        authorization_pin = int(input('Enter you pin:'))

        if authorization_pin == self.pin:
            self.withdraw(amount)
            recipient.deposit(amount)
            print('Success')
            return True
        else:
            print('Failed')
            return False
    
    def request_money(self, amount, donor):
        print(f'{amount} to {donor.name}')

        print('Authprization required')
        authorization_pin = int(input('Enter donor pin:'))
        user_password = input('Enter your password')

        if authorization_pin == donor.pin and user_password == self.password:
            donor.withdraw(amount)
            self.deposit(amount)
            print('Success')
            return True
        else:
            print('Failed')
            return False
        

""" Driver Code for Task 1 """
# user = User('jeff', 1234, 'password')
# print(user.name, user.pin, user.password)

""" Driver Code for Task 2 """
# user = User('jeff', 1234, 'password')
# print(user.name, user.pin, user.password)
# user.change_name('jeffery')
# user.change_pin(5678)
# user.change_password('password123')
# print(user.name, user.pin, user.password)

""" Driver Code for Task 3"""
# user = BankUser('jeff', 1234, 'password')
# print(user.name, user.pin, user.password, user.balance)

""" Driver Code for Task 4"""
# user = BankUser('jeff', 1234, 'password')
# user.show_balance()
# user.deposit(511.11)
# user.show_balance()
# user.withdraw(11.11)
# user.show_balance()

""" Driver Code for Task 5"""
user1 = BankUser('user1', 1234, 'user1')
user2 = BankUser('user2', 5678, 'user2')

user2.deposit(5000)

user2.show_balance()
user1.show_balance()

if user2.transfer_money(500, user1):
    user2.show_balance()
    user1.show_balance()
    user2.request_money(200, user1)

user2.show_balance()
user1.show_balance()




