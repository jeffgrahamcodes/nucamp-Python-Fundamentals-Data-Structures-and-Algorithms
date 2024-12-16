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
    def is_valid_amount(self, amount):
        if amount > 0:
            return True
        return False

    def show_balance(self):
        print(f'{self.name} has an account balance of: ${self.balance:.2f}')

    def withdraw(self, amount):
        if self.is_valid_amount(amount):
            self.balance -= amount
        else:
            print('Amount of withdrawal must be greater than 0')

    def deposit(self, amount):
        if self.is_valid_amount(amount):
            self.balance += amount
        else:
            print('Amount of deposit must be greater than 0')

    # Task 5: Transfer and request money
    def transfer_money(self, amount, recipient):
        if self.is_valid_amount(amount):
            if amount <= self.balance:
                print(
                    f'\nYou are transferring ${amount:.2f} to {recipient.name}')

                print('Authprization required')
                authorization_pin = int(input('Enter you pin: '))

                if authorization_pin == self.pin:
                    self.withdraw(amount)
                    recipient.deposit(amount)
                    print('Transfer Authorized')
                    print(f'Transferring ${amount:.2f} to {recipient.name}')
                    return True
                else:
                    print('Invalid PIN: Transfer cancelled')
                    return False
            else:
                print(
                    f"You don't have enough to make that transfer. You only have ${self.balance:.2f}")
        else:
            print('Amount of transafer must be greater than 0')
            return False

    def request_money(self, amount, donor):
        if self.is_valid_amount(amount):
            if amount <= donor.balance:
                print(f'\nYou are requesting ${amount:.2f} from {donor.name}')

                print('Authprization required')
                authorization_pin = int(input(f"Enter {donor.name}'s pin: "))
                if authorization_pin != donor.pin:
                    print('Invalid Pin. Transaction cancelled')
                    return False

                user_password = input('Enter your password: ')
                if user_password != self.password:
                    print('Invalid Password. Transaction cancelled')
                    return False

                if authorization_pin == donor.pin and user_password == self.password:
                    donor.withdraw(amount)
                    self.deposit(amount)
                    print('Request Authorized')
                    print(f'{donor.name} sent ${amount:.2f}')
                    return True
            else:
                print(
                    f"{donor.name} doesn't have enough to make that transfer.")
        else:
            print('Amount of request must be greater than 0')
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
randolph = BankUser('randolph', 1234, 'randolphduke')
mortimer = BankUser('mortimer', 5678, 'mortimerduke')

mortimer.deposit(5000)

mortimer.show_balance()
randolph.show_balance()

if mortimer.transfer_money(500, randolph):
    mortimer.show_balance()
    randolph.show_balance()
    mortimer.request_money(25000, randolph)

mortimer.show_balance()
randolph.show_balance()
