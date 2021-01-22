# %%
# Lambda functions

from typing import Sequence


def short_function(x):
    return x * 2


# lambda is for a quick short function.
# I have no clue why I would use this and not write it out??
def equiv_anon(x): return x * 2


def apply_to_list(some_list, f):
    return [f(x) for x in some_list]


ints = [4, 0, 1, 5, 6]

apply_to_list(ints, lambda x: x * 2)

# so here we are multiplying each int by 2.. this is suppose to be the better way of using it.
strings = ['foo', 'card', 'bar', 'aaaa']
strings.sort(key=lambda x: len(set(list(x))))
print(strings)

# my idea is to use this for passing a function in a function..
# %%
# Built in functions: map
numbers = (1, 2, 3, 4)
results = map(lambda x: x + x, numbers)
print(list(results))

print('We are adding the numbers in \
the first array to the numbers in the second.')
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

results = map(lambda x, y: x + y, numbers1, numbers2)
print(list(results))

print('Now this next part is listing each char value.')
l_str = ['sat','bat','cat','mat']
test = list(map(list, l_str))
print(test)
# %%
# Built in functions: filter

def fun(variable):
    letters = ['a', 'e','i','o','u']
    if (variable in letters):
        return True
    else:
        return False

sequence = ['g', 'e', 'e', 'j', 's']
filtered = filter(fun, sequence)

print('The letters in the filter function are: ')
for s in filtered:
    print(s)

print()
print('Now we will filter out even numbers in a list.')

seq = [1,3,4,55,6645,32,65,784,2]
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

print('Ok.. so lets filter out the odd in the same list.')
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
# %%
# let build exception functions

try:
    print(0/0)
except ZeroDivisionError:
    print('You can not divide by zero dumb ass.')


# %%
