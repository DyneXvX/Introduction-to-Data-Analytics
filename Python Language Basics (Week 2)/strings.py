#%%
single_quote_string = 'data science'
double_quote_string = "Data Science"
escaped_string = 'Isn\'t this fun?'
another_string = "Isn't this fun?"
really_long_string = 'This is a really long string. \
It has multiple parts \
but all of it will be on one line.'
multi_line_string = """This is the first line
and this is the second line
and congrats this is the third line."""

print(single_quote_string)
print(double_quote_string)
print(escaped_string)
print(another_string)
print(really_long_string)
print(multi_line_string)
# %%
#raw string
raw_div_string = r"4/3"
print(raw_div_string)
# %%
#string operations
print('Goat')
print('However can we multiple the string itself? yes we can.')
goat = "goat" * 3
print(goat)
print()
a = 'Welcome to intro to data analytics'
print(a)
print('We replace the analytics now with science')
b = a.replace('analytics', 'science')
print(b)
# %%
#string template:

template = '{0:.2f} {1:s} are worth US${2:d}'
print(template.format(73.1976, 'Indian Rupee', 1))

# %%
#date and time
from datetime import date, datetime

a = datetime(1999, 12, 12, 12 , 12, 12)
print(a)
print('The year is ', a.year)
print('The month is ', a.month)

b = datetime.today()
c = datetime.now()
print(b)
print(c)
# %%
