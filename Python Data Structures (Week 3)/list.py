#%%
## --List standards--
interger_list = [1, 2, 3]

list_length = len(interger_list)
print("The length of the list is: ", list_length)

print()
print("Moving on to a range list. Will be 0-9")
x = [i for i in range(10)]
print("The value at index 1: ", x[1])

#this will produce the last value in the list
print("The value at the end of the list is: ", x[-1])

print()
print("--------------------------------------------")
print("Now how do we add to or remove from a list?")
word_list = ['sup', 'whatever', 'and again!']
print(word_list)

#append
print("Simple we append, insert, pop, remove")
print("lets add the word 'hello'.")
word_list.append('hello')
print("The updated list is now ", word_list)

#remove
print("Let us remove the word 'sup'..")
word_list.remove('sup')
print("The new list is now: ", word_list)
print("Now lets see if the word 'sup' is in the list using bool")
print('sup' in word_list)
print("--------------------------------------------")
print()

# %%
## Sorting List
print("Now we will start sorting List.")
a = [1, 57, 12, 68]
print(a)
print("To sort a list we use the 'sort' function..... yeah... really..")
a.sort()
print(a)

print()
print("Let sort by key length...")
b = ['sup', 'another', 'word', 'still going']
print(b)
print("now we add the key length to the sort and...")
b.sort(key=len)
print(b)

print("\nSlide 11 has a ton of information.. Don't forget that Justin!")
#%%
##Slicing (Strings for this example)
print("\n Lets slice a string and see what happens... 'abcdefghijklmnopqrstuvwxyz'")
s = "abcdefghijklmnopqrstuvwxyz"
a = s[10]
print("A will become s[10].... so what will it be?")
print(a)
print("b will become the last three using s[-3:]")
b = s[-3:]
print(b)