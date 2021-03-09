#%%
import pandas as pd
from pandas import Series, DataFrame

# one dimensional array

obj = pd.Series([4,7,-5,3])
print(obj)
print()

print(obj.values)
print()

print(obj.index)
print()
# %%
# Series - Referencing Elements

print('Creating a new array')
obj2 = pd.Series([4,7,-5,3], index=['d', 'b', 'a', 'c'])
print('Print the new array with custom index rules')
print(obj2)
print()

print('These are the values of the new array.')
print(obj2.values)
print()

print('This is how the custom index is setup.')
print(obj2.index)
print()

print('The value found at index a is:')
print(obj2['a'])
print()

print('The value at index d is:')
print(obj2['d'])
print()
print('Lets change the value of d to a 6 now and print.')
obj2['d'] = 6
print(obj2[['c','a','d']])
print()
# %%
# NumPy function 

import numpy as np

print('Lets only print items in obj2 array that are greater than 0')
print(obj2[obj2 > 0])
print()

print('Now lets multiple everything in obj2 by 2')
print(obj2 * 2)
print()

print('No clue. Has something to do with numpy exponents.\n'
'Need to look this up')
print('np.exp(obj2)...... yeah no clue')
print(np.exp(obj2))
print()
# %%
# Ordered Dictionary

sData = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sData)

print(obj3)
print()

print('Check the value for a index in the dictionary')
print(obj3[1])
print()
print(obj3[3])
if((obj3[1]) > (obj3[3])):
    print('Index 1 is greater then index 3')
else:
    print('fail')

# %%
