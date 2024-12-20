# Task 2: Show homepage and initialize app data
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {'admin': 'password123'}
donations = []
authorized_user = ''

while True:
    show_homepage()
    if authorized_user == '':
        print('You must be logged in to donate.')
    else:
        print(f'Logged in as: {authorized_user}')

    option = input('Choose an option: ')

    # Task 3: Handle user input
    if option == '1':
        username = input('\nEnter username: ')
        password = input('Enter password: ')
        authorized_user = login(database, username, password)
    elif option == '2':
        while True:
            username = input('Enter username: ')
            if len(username) > 10:
                print('username must not exceed 10 characters')
            else:
                break
        while True:
            password = input('Enter password: ')
            if len(password) < 5:
                print('Password must be at least 5 characters long')
            else:
                break
        authorized_user = register(database, username)
        if authorized_user != '':
            database[username.lower()] = password
    elif option == '3':
        if authorized_user == '':
            print('You are not logged in')
        else:
            donation_string = donate(username) 
            donations.append(donation_string)  
    elif option == '4':
        show_donations(donations)
    elif option == '5':
        print('Goodbye.')
        exit()
