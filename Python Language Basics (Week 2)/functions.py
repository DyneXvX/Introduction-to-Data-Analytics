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

##stopping for lunch at 8:51 seconds in the video.
# %%
