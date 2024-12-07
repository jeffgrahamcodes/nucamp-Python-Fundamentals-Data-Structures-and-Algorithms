# Task 5: Use the banking package
from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

# Task 2: Registration
print("    === Automated Teller Machine ===    ")
# Bonus Task 1
while True:
    name = input("Enter name to register: ")
    if len(name) <= 1 or len(name) >= 10:
        print('Invalid Name! Name must be between 1 and 10 characters\n')
    else:
        break

# Bonus Task 2
while True:
    pin = input("Enter PIN: ")
    if len(pin) != 4:
        print('Invalid Pin! Pin must be 4 characters long\n')
    else:
        break

balance = 0.0
print(f"{name} has been registered with a starting balance of ${balance:.2f}\n")

# Task 3: Log in and prompt for menu option
while True:
    print("    === Automated Teller Machine ===    ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!\n")
        break
    
    print("Invalid credentials\n")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    # Task 5: Use the banking package
    if option == '1':
        account.show_balance(balance)
    elif option == '2':
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == '3':
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == '4':
        account.logout(name)
        exit()
    else:
        print('Invalid selection.')
