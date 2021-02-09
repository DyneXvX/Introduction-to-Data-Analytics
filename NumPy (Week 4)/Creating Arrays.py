#%%
import numpy as np

data = np.random.randn(2,3) #two rows by 3 columns
print(data)
print()

print(data * 10)
print()

print(data.shape)
print()

print(data.dtype)
print()
# %%
#Creating the Array

data1 = [6,7.5,10,0,-7]
arr1 = np.array(data1)
print(data1)
print(arr1)
print(arr1.ndim) #number of dimesions.
print(arr1.shape)
print(arr1.dtype)
print()


# %%
print(np.zeros(10), '\n')
print(np.zeros((3,6)), '\n' )
print(np.eye(4,7), '\n')
print(np.empty((2,3,2), dtype=int), '\n')
# %%
