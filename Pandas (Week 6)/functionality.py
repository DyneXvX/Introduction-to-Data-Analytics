# %%
import pandas as pd
import numpy as np

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
print()
# Calling reindex rearranges the data according to the new index
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])

print(obj2)
print()

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
print()

# ffill method - forward fills the values
print(obj3.reindex(range(6), method='ffill'))
print()

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=[
                     'a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])

print(frame)
print()

# When passed only a sequence, reindexes the rows
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)
print()

# columns can be reindexed with the columns keyword
states = ['Texas', 'Utah', 'California']
frame3 = frame2.reindex(columns=states)
print(frame3)
print()

# reindex by label-indexing with loc
frame4 = frame3.loc[['a', 'b', 'c', 'd'], states]
print(frame4)

# %%
# Dropping Entries from an Axis
# Slide 38

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
print()

# drop method will return a new object with the indicated value
new_obj = obj.drop('c')
print(new_obj)
print()

# drop method can be used for deleting values from an axis
print(obj.drop(['d', 'c']))
# %%
# Deleting index values
# Slide 39

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=[
                    'Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])

print(data)
print()

# Calling drop with a sequence of labels will drop values from the row labels (axis 0)
print(data.drop(['Colorado', 'Ohio']))
print()

# drop values from the columns by passing axis=1 or axis='columns'
print(data.drop('two', axis=1))
print()

print(data.drop(['two', 'four'], axis='columns'))
print()

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
print()

# in-place method modify the size or shape of a Series or DataFrame without returning a new object
obj.drop('c', inplace=True)
print(obj)
# %%
# Series Indexing
# Slide 40


obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])

print(obj)
print()

print(obj['b'])
print()

print(obj[1])
print()

print(obj[2:4])
print()

print(obj[['b', 'a', 'd']])
print()

print(obj[[1, 3]])
print()

print(obj[obj < 2])
print()
# %%
# Slicing with Labels
# Slide 41

print(obj['b':'c'])
print()

# Setting using these methods modifies the corresponding section of the Series
obj['b':'c'] = 5
print(obj)
print()

# %%
# Retrieving Columns in DataFrame
# Slide  42

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=[
                    'Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])

print(data)
print()

print(data['two'])
print()

print(data[['three', 'one']])
print()
# %%
# DataFrame: Selecting Data using Slicing
# Slide 43

print(data[:2])
print()

print(data[data['three'] > 5])
print()

print(data < 5)
print()

data[data < 5] = 0

print(data)
print()

print()
print()