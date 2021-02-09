#%%
import numpy as np
from timeit import default_timer as timer
from datetime import timedelta

my_arr = np.arange(100000)
my_list = list(range(100000))

start = timer()

for _ in range(100):
    my_arr = my_arr * 2

end = timer()
print('Time take by Numpy: ', timedelta(milliseconds= end - start))

start = timer()
for _ in range(100):
    my_list2 = [x * 2 for x in my_list]

end = timer()
print('Time taken by list of list: ', timedelta(milliseconds= end - start))
# %%
