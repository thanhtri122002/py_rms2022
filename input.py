import pickle
import zipfile

def input_name():
    while True:
        try:
            fst, lst = input('. Enter name (first, last): ').strip().split(',')
        except ValueError:
            print('(!) Invalid input')
            continue
        if fst.strip() == '' or lst.strip() == '':
            print('(!) Invalid name')
            continue
        return fst.strip(), lst.strip()

def print_admin_action():
    print('''\n--------- Administrator ---------\n
                        \r  1. Dishes
                        \r  2. Employees
                        \r  3. Bills
                        \r  0. Quit''')

def print_tables(t):
    print(f'''\n------------- Tables -------------\n
            \r   [1]: {t[0]}     [2]: {t[1]}     [3]: {t[2]}
            \r   [4]: {t[3]}     [5]: {t[4]}     [6]: {t[5]}
            \r   [7]: {t[6]}     [8]: {t[7]}     [9]: {t[8]}
            \r\n----------------------------------''')

def write_data(str, list0, list1):      # str: 'dishes', 'employees', 'bills'
    with open(f'{str}.txt', 'wb') as f:
        pickle.dump(list0, f)
        pickle.dump(list1, f)

def read_data(str):
    list0 = []
    list1 = []
    with open(f'{str}.txt', 'rb') as f:
        list0 = pickle.load(f)
        list1 = pickle.load(f)
    return list0, list1

def compress_data():
    with zipfile.ZipFile(f'res_data.zip', 'w') as f:
        f.write(f'dishes.txt')
        f.write(f'employees.txt')
        # f.write(f'bills.txt')

def decompress_data():
    with zipfile.ZipFile(f'res_data.zip', 'r') as f:
        f.extractall()