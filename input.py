def input_num(str):     # Input a quantity of something
    while True:
        try:
            num = int(input(f'\nEnter number of {str}: '))
            return num
        except ValueError:
            print('(!) Invalid input')