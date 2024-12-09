# Task 2: Show homepage and initialize app data
def show_homepage():
    print("")
    print("         === DonateMe Homepage ===          ")
    print("--------------------------------------------")
    print("| 1.    Login       | 2.    Register       |")
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("| 3.    Donate      | 4.    Show Donations |")
    print("--------------------------------------------")
    print("|                5. Exit                   |")
    print("--------------------------------------------")

# Task 6: Donate functionality
def donate(username):
    donation_amt = float(input('Enter amount to donate: '))
    donation_string = f'{username} donated ${donation_amt:.2f}'
    print('Thank you for your donation!')
    return donation_string

# Task 7: Show Donations functionality
def show_donations(donations):
    print('\n         --- All Donations ---            ')

    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        total = 0.0
        for donation in donations:
            print(donation)
            current_donation_amt = float(donation[donation.index('$') + 1:])
            total = total + current_donation_amt
        
        print(f'Total = ${total:.2f}')
