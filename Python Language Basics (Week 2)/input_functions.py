# %%
# employee data information

name = input("Enter the employees name: ")
salary = input("Enter the salary: ")
company = input("Enter the company name: ")

print("------------------------\n")
print("Printing employee details")
print("Name", "Salary", "Company")
print(name, salary, company)

# %%
# How to accept integer input from the user

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

print("\n")
print("Your First number was: ", first_number)
print("Your second number was: ", second_number)

total = first_number + second_number
print("The total of your two numbers is: ", total)
# %%
# How to only accept interger values from the user

while True:
    try:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
        break
    except ValueError:
        print("One of your values was not a number.")

print("\n")
print("Your First number was: ", first_number)
print("Your second number was: ", second_number)

total = first_number + second_number
print("The total of the numbers is ", total)

# %%
# Lets setup a way to Calculate Wages


def main():
    '''Get all user input and the values here for hours and pay.'''

    active = True
    while active:
        print("-----------Wage Calculator---------")
        try:
            name = input("Enter your name: ")
            hours = float(input("Please input your total hours worked: "))
            pay = float(input("Please enter your hourly wage: "))
            
            total = getwages(hours, pay)
            print('{name} worked for a total of {hours} hours at a wage of {pay: .2f} per hour.'.format(locals()))
            print('They made a total of {total: .2f}'.format(locals()))
            active = False


        except ValueError:
            print("Please enter the correct hours and pay.")


def getwages(totalhours, hourlywages):
    if totalhours <= 40:
        totalwages = totalhours * hourlywages
    elif totalhours > 40 & totalhours <= 59:
        totalwages = totalhours * (1.5 * hourlywages)
    else:
        totalwages = totalhours * (2 * hourlywages)
    return totalwages

main()
# %%
