#%%
import math
print("""What is the square root of 2? 
Using Math.pow we can do just that.""")
rt2 = math.sqrt(2)
print(rt2)

a = 2
b = 3
math.pow(a, b)


# %%
#Defining a new function

def print_courseinfo():
    print('CAP 4784')
    print('Introduction to Data Analytics')

print_courseinfo()

def student_class(name):
    print('Hello my name is ' + name)
    print('I am a student in')
    print_courseinfo()

student_class("Justin")

##doubt strings???
def double_string(string):
    return 2*string

print()
double_string('osprey')
print()

print('So now how do we do default messages?')
def my_print(message='my default message'):
    print(message)

my_print()
print()
print("""Setup subtraction default values
Lets set a to 0 and b to 0.
Then we build a method to do the work.""")
def subtraction(a=0, b=0):
    return a - b


subtraction(100, 27)


# %%
#returning multiple values

def f():
    a = 5
    b = 6
    c = 7
    return a,b,c

f()

# %%
import re
# re is for regular expressions

states = [' Alabama', 'Georgia!' , 'Georgia', 'georgia',
' FlOrida', 'south carolina##', 'West virginia?']

print('So our states data is all jacked up.')
print(states)
print()

print('We need to clean this so we build a clean function')
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        #striping the random spaces
        value = re.sub('[!#?]' , '' , value)
        #removing all of these random char and spaces.
        value = value.title()
        #capitalizing the title/first letter
        result.append(value)
    return result

clean_strings(states)

# %%
