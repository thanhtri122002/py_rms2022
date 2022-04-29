import pickle

passwords = {}
roles = {'1': 'Admin', '2': 'Staff'}
default_password = {'Admin': 'admin', 'Staff': 'staff'}

# read passwords from file
def read_passwords():
    try:
        with open('passwords.pkl', 'rb') as file:
            passwords = pickle.load(file)
    except FileNotFoundError:
        print('No password file found. Creating new file.')
        write_passwords()

def write_passwords():
    with open('passwords.pkl', 'wb') as file:
        pickle.dump(passwords, file)


# add a new password
def change_password(role, password):
    print('''Choose a role:
            \r  1. Admin    2. Staff''')
    role = input('Choice (1, 2): ')
    if role not in roles.keys():
        role = input('Role not found. Try again: ')
    else:
        role = roles[role]
        passwords[role] = password
        write_passwords()
        print('Password changed.')
