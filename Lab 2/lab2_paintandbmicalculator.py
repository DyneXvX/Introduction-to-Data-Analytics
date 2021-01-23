# %%
from lab2_bmi import bmi
from lab2_paint import *


def main():
    print()
    print('Welcome to my Python program.')
    print('---------------------------')
    print()
    print('Your menu options are: ')
    print('     ', 'Enter 1 for calculating gallons of paint needed to paint a room.')
    print('     ', 'Enter 2 for calculating Body Mass Index')
    print('     ', 'Enter any other value to quit the program.')
    print()

    while True:
        try:
            choice = int(input('Enter your menu option: '))
            break
        except ValueError:
            print("Your choice must be a number. Please enter a valid choice.")

    print()

    if choice == 1:
        paint()
        main()
    elif choice == 2:
        bmi()
        main()
    else:
        print('Exiting program:')
        print('Thank you for using a (c)Justin Thoms Python Program')
        exit()


main()

# %%
