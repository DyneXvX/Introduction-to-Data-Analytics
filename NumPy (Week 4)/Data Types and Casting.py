#%%
import numpy as np;

arr1 = np.array([1,2,3], dtype=np.float)
arr2 = np.array([1.1,2.4,3.7], dtype=np.int)

print(arr1)
print(arr1.dtype, '\n')

print(arr2)
print(arr2.dtype, '\n')
# %%
#Convert to another data type
arr = np.array([1,2,3,4,5])
print(arr)
print(arr.dtype, '\n')

float_arr = arr.astype(np.float)
print(float_arr)
print(float_arr.dtype, '\n')
# %%
# Arithmetic with Numpy Arrays

arr = np.array([[1,2,3], [4,5,6]])
print(arr, '\n')

print(arr * arr, '\n')
print(arr - arr, '\n')
print(1/arr, '\n')
print(arr ** 0.5, '\n') # raised too.

arr2 = np.array([[2,3,4], [5,1,7]])
print(arr>arr2)
# %%
