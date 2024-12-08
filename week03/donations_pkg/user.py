def login(database, username, password):
    if username in database.keys() and database[username] == password:
        print(f'Welcome {username}')
        return username
    elif username in database.keys() and database[username] != password:
        print('Invalid password')
        return ''
    else:
        print('User not found. Please register.')

def register(database, username):
    if username in database.keys():
        print('Username already registered')
        return ''
    else: 
        print(f'{username} has been registered')
        return username

