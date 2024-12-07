# Task 4: The banking package
def show_balance(balance):
    print(f"Current Balance: ${balance:.2f}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    # Bonus Task 3
    if (amount > balance):
        print(f"Cannot withdraw ${amount:.2f}. You only have ${balance:.2f}.")
        return balance
    else:
        return balance - amount

def logout(name):
    print(f"Goodbye {name}!")
