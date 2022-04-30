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