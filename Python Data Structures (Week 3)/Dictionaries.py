#%%
#Dictionaries

empty_dict = {}
empty_dict2 = dict()

print('Working with a dictionary (see code)')
d1 = {'a': 'some values', 'b': [1,2,3,4]} 
print(d1)
grades = {"Joel": 80, "Tim": 95}
print("This is the grades dictionaires: ", grades)

print(d1['b'])
grades["Tim"] = 99
print("This is the grades dictionairy after Tim has been updated: ", grades)

all_values = grades.values()
print(all_values)

#%%
#Set

#Unordered collection of unique elements.

thisset = {"banana", "apple", "cheery"}
print(thisset)

#%%
# List Compresensions
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
comp = [x.upper() for x in strings if len(x) > 2]
print(comp)