def input_num(str):     # Input a quantity of something
    while True:
        try:
            num = int(input(f'\nEnter number of {str}: '))
            while num < 1:
                print('(!) Invalid input')
                num = int(input(f'\nEnter number of {str}: '))
            return num
        except ValueError:
            print('(!) Invalid input')