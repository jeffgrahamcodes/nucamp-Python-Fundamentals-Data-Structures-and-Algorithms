
# Task 4: Login functionality
def login(database, username, password):
    if username.lower() in database.keys() and database[username.lower()] == password:
        print(f'\nWelcome back {username}!')
        return username
    elif username.lower() in database.keys() and database[username] != password:
        print(f'\nIncorrect password for {username}')
        return ''
    else:
        print('User not found. Please register.')

# Task 5: Register functionality
def register(database, username):
    if username.lower() in database.keys():
        print('Username already registered')
        return ''
    else: 
        if len(username) > 10:
            print('username must not exceed 10 characters')
            return ''
        print(f'{username} has been registered')
        return username

