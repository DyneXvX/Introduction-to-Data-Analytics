#%%
# What is a tuple
# a tuple is a fixed-length.
# a tuple cannot be modified like a list
print("Parenthis are nice but not required.. First is with them in the code"
      "\nHowever the second is without.")
a = (0, 1, 2, 3)
print(a)
b = 4, 5, 6
print(b)
print("I have no clue why we use these.... List just seem better in practice..")
#%%
# Built in sequence mapping

some_list = ["Hello", "World", "!"]
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i

print(mapping)

#%%
# Built in sequence of sort and reverse

horse_list = 'horse list'
print("List will be 'horse list'...."
      "\nDon't judge me")

print("\nLets sort the list first.")
sorted_horse_list = sorted(horse_list)
print(sorted_horse_list)

print("\nNow lets reverse our strange list.")
revese_horse_list = list(reversed(horse_list))
print(revese_horse_list)

#%%
# Zip Function
pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
print(pitchers)
first_names, last_names = zip(*pitchers) # * captures positional arguments <-- what ever the hell that means
print(first_names)


# %%
