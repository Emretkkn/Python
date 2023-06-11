import numpy as np
list = [1,2,3,4,5,6,7,8,9] # Python List
np_array = np.array([1,2,3,4,5,6,7,8,9]) # Numpy Array
# print(type(list),type(np_array))
py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)
# print(py_multi)
# print(np_multi)
# print(np_array.ndim) # Boyut sayısını bastırır.
# print(np_multi.ndim)
print(np_array.shape) # (9,)
print(np_multi.shape) # (3,3)