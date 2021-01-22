#%%

# variables and objects
x = [1,3,5]
y = x
x[0] = 2
print(y)
# what will y be?
#%%
a = 4.5
b = 2
pi = 3.141592
number_of_planets = 9
print(type(pi))
print(type(number_of_planets))
print('a is {0}, b is {1}'.format(a,b))
print(a + b)
# what type will number_of_planets be?
# %%
# casting variables to something else
pi = 3.141592
print(type(pi))
# this will show pi is a float.. however,
pi_int = int(pi)
print(type(pi_int))
# by adding the "int" to pi we can cast pi as an int now.
print(pi_int)

# keep in mind
answer = 'string'
# can we cast the string answer to an int? 
answer_int = int(answer)
print(answer_int)
# short answer no that doesn't even make since.
# %%
