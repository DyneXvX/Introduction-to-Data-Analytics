#%%
import pandas as pd

# Create a DataFrame from a dict
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

print(frame)
print()

# head method is only for the first five rows
print(frame.head())
print()
# %%
# DataFrames Columns

print(pd.DataFrame(data, columns=['year', 'state', 'pop']))
print()

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=[
                      'one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print()

#DataFrame Access one column at a time
print(frame2['state'])
print()

print(frame2.year)
print()

#DataFrame - access one row
print(frame2.loc['three'])
print()
# %%
# Columns can be modified by assignment
# Slide 26

import numpy as np

frame2['debt'] = 16.5
print(frame2)
print()

frame2['debt'] = np.arange(6.)
print(frame2)
print()
# %%
# Assigning lists or arrays to a column
# Slide 27

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val

print(frame2)
print()
# %%
# Creating a new column through assignment
# Slide 28

frame2['eastern'] = frame2.state == 'Ohio'

print(frame2)
print()

# del method can then be used to remove column
del frame2['eastern']

print(frame2.columns)
print()
# %%
# DataFrame – from nested dict of dicts
# Slide 29

pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)

print(frame3)
print()

# transpose the DataFrame (swap rows and columns)
print(frame3.T)
print()

# combining and sorting to form the index in the result
print(pd.DataFrame(pop, index=[2001, 2002, 2003]))
print()

# Dicts of Series
pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}

print(pd.DataFrame(pdata))
print()
# %%
# DataFrame – index, columns, values
# Slide 30

frame3.index.name = 'year'; frame3.columns.name = 'state'

print(frame3)
print()

# values returns 2-D ndarray
print(frame3.values)
print()
# %%
# Index Objects as Arrays
# Slide 32

import numpy as np

# using array as index labels
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
print()

print(index[1:])
print()

# share Index objects among data structures
labels = pd.Index(np.arange(3))

print(labels)
print()

obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)
print()

print(obj2.index is labels)
print()
# %%
# Index also behaves like a fixed-size set
# Slide 33

pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)

print(frame3)
print()

print(frame3.columns)
print()

print('Ohio' in frame3.columns)
print()

print(2003 in frame3.index)
print()

# Unlike Python sets, a pandas Index can contain duplicate labels

dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])

print(dup_labels)
# %%
