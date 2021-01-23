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
    choice = int(input('Enter your menu option: '))
    print()

    if choice == 1:
        paint()
        main()
    elif choice == 2:
        bmi()
        main()
    else:
        print('Thank you for using a (c)Justin Thoms Python Program')
        exit()


main()

# %%
