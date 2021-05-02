# importing os to clear the screen for second calculation
import os

# function which except values and calculate accordingly
def calculate():

    try:                                                                # Getting first value
        a = int(input('what is your first value\n'))

    except ValueError:                                                  # excepting Errors
        print("\nOops!  That was no valid number.  Try again...")
        a = float(input('\n\nwhat is your first value\n'))

    try:
        b = float(input('\nwhat is your second value\n')
                  )               # Getting second value
    except ValueError:                                                  # excepting Errors
        print("\nOops!  That was no valid number.  Try again...")
        b = float(input('\n\nwhat is your first value\n'))

    # Getting operations to calculate
    expression = input('\nWhat is the expression\n')

    if expression == '+':                                               # Addition
        answer = str(a + b)
        print('answer = ' + answer)

    elif expression == '-':                                             # Substraction
        answer = str(a - b)
        print('answer = ' + answer)

    elif expression == '*':                                             # Multiplication
        answer = str(a * b)
        print('answer = ' + answer)

    elif expression == '**':                                            # Exponent
        try:
            answer = str(a ** b)
            print('answer = ' + answer)
        except OverflowError:
            print("\nOops!  That was a really big number. Sorry...")

    elif expression == '/':                                             # Division
        answer = str(a / b)
        print('answer = ' + answer)

    elif expression == '//':                                            # Interger Division
        answer = str(a // b)
        print('answer = ' + answer)

    input()
    # clearing the screen function
    os.system("CLS")


if __name__ == '__main__':
    # Calling function Calculate
    calculate()
