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