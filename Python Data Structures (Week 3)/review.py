##Week 3 Quiz - After the test I built the code to see what would happen.
#%%
print((4,7) + (8,4))

#%%
a={1:"A",2:"B",3:"C"}
for i,j in a.items():
    print(i,j,end=" ")
# %%

l1=[1,2,3]
l2=[4,5,6]
[x*y for x in l1 for y in l2]
# %%
aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[2:3]))
# %%
s = {100,200,300}

s.union(set([300,400,500]))
print(s)
# %%
a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]
print(b)

# %%
a = list(range(10))
b = a
b[0] = 100
print(a)
# %%
