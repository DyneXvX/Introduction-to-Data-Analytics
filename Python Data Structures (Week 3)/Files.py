#%%
# How do you work with files?

path = 'data/file.txt'

example_file = open(path)
for line in example_file:
    print(line)

example_file.close
# %%

# Create a new file
# use the 'w' mode with the open statement

import random
odd_even = lambda num1: "Even Number" if num1 % 2 == 0 else "Odd Number"

with open('data/built.txt', 'w') as handle:
    handle.writelines('This is the start of the file. \n')
    for x in range(10):
        var1 = random.randrange(50,100)
        handle.write(str(var1) + ' is an ' + odd_even(var1) + '\n')
    
print("File created")
# %%
# Slide 36 has many good methods for working with files.