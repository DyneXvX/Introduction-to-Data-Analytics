#%%
#

import numpy as np

arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
print()

arr[5:8] = 12
print(arr[5:8])
print(arr)
print()

arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
print(arr_slice)
print()
print(arr)
# %%
print('3d Array')
arr3d = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]])
print(arr3d)
print()
print('3D Array First')
print(arr3d[0])
print()
print('3D Array Second')
print(arr3d[1])
print()
old_values = arr3d[0].copy()
arr3d[0] = 42
print('Replaced first array with 42')
print(arr3d, '\n')
print('These are the old values')
print(old_values, '\n')

print('Put back the original array values.')
arr3d[0] = old_values
print(arr3d)
# %%
#Index with Slices - Good Luck this is tough to keep up with.

print('First Array')
arr = np.array([0,1,2,3,4,64,64,64,8,9])
print(arr, '\n')
print(arr[1:6], '\n')

print('Second Array')
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d, '\n')

print('Slice along axis 0 (rows) first two rows.')
print(arr2d[:2], '\n')

print('Remove first column with 2 rows, ')
print(arr2d[:2, 1:], '\n')

print('Second row only first two columns')
print(arr2d[1, :2], '\n')

print('Just the second row without the value at index 2')
print(arr2d[2:, :2 ], '\n')

print('Now print Array 2D where the value is not 2')
print(arr2d != 2)
# %%
#Fancy Indexing

arr = np.empty((8,4))
for i in range(8):
    arr[i] = i

print(arr, '\n')

print(arr[[4, 3, 7]], '\n')

print('Built 0 - 32 and shaped as a 8 by 4')
arr = np.arange(32).reshape((8,4))
print(arr, '\n')



# %%
