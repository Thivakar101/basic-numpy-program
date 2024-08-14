#to add a border around an existing array
import numpy as np
arr = np.array([[1, 2, 3]])
pad_width = 1
arr_padded = np.pad(arr, pad_width=pad_width, mode='constant', constant_values=0)
print("Original array:")
print(arr)
print("\nArray with zero border:")
print(arr_padded)
#convert a list into arrays
import numpy as np
list_data = [1, 2, 3, 4, 5]
array_from_list = np.array(list_data)
print("Original list:", list_data)
print("NumPy array from list:", array_from_list)
import numpy as np
tuple_data = (6, 7, 8, 9, 10)
array_from_tuple = np.array(tuple_data)

print("Original tuple:", tuple_data)
print("NumPy array from tuple:", array_from_tuple)
