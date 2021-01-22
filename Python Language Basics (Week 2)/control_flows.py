# %%

# if, else, elif, for, while, break, continue

x = 4784

if x > 2:
    message = 'if only 1 were greater than two...'
elif x > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use the else code."
print(message)

parity = "even" if x % 2 == 0 else "odd"
print(parity)
# %%
# for loops

sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value
print(total)

for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)

# remember that break only termindates the inntermost loop it is on.

for i in range(4):
    for j in range(4):
        if j > i:
            break
        print((i, j))
# %%
#while loop

x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2
    print(x)
print(x)
# %%
# range function
range(3)
list(range(3))

for i in range(5):
    print(i)

print('--------range(2,5)----------')
for i in range (2,5):
    print(i)

print()
for i in range(0,10,2):
    print(i)

print()
a =['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
# %%
