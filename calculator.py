def calculate():
    # Welcome user to the calculator
    print('''Welcome to Calculator''')

    # Prompting user to choose an operation
    operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
''')

    # Prompting user to enter two numbers
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    # Performing calculation based on user's operation choice
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '**':
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1 ** number_2)

    elif operation == '%':
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 % number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Prompting user if they want to calculate again
    def again():
        calc_again = input('''
Do you want to calculate again?
Please type Y(y) for YES or N(n) for NO.
''')

        # Accept 'y' or 'Y' by adding str.upper()
        if calc_again.upper() == 'Y':
            calculate()

        # Accept 'n' or 'N' by adding str.upper()
        elif calc_again.upper() == 'N':
            print('See you later.')

        else:
            again()

    again()

# Call calculate() outside of the function
calculate()
