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
import numpy as np
# Create an initial array
array = np.array([1, 2, 3, 4, 5])

# Values to add
values_to_add = [6, 7, 8]
# Append values to the end of the array
new_array = np.append(array, values_to_add)
import numpy as np
# Create an empty array of shape (2, 3)
empty_array = np.empty((2, 3))
print("Empty array:")
print(empty_array)
import numpy as np
# Create a full array of shape (2, 3) with the value 7
full_array = np.full((2, 3), 7)
print("Full array:")
print(full_array)
import numpy as np
complex_array = np.array([[1 + 2j, 3 + 4j], [5 + 6j, 7 + 8j]])
real_part = complex_array.real
imaginary_part = complex_array.imag
print("Complex array:")
print(complex_array)
print("Real part:")
print(real_part)
print("Imaginary part:")
print(imaginary_part)

print("Original array:", array)
print("New array:", new_array)
import numpy as np

def celsius_to_fahrenheit(celsius_array):
    fahrenheit_array = (celsius_array * 9/5) + 32
    return fahrenheit_array
celsius_array = np.array([0, 20, 37, 100])
fahrenheit_array = celsius_to_fahrenheit(celsius_array)

print("Celsius array:")
print(celsius_array)

print("Fahrenheit array:")
print(fahrenheit_array)

import numpy as np
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])
transposed_array_2d = array_2d.

import numpy as np

# Create a 5-dimensional array with dimensions 2x3x4x5x6
array_5d = np.zeros((2, 3, 4, 5, 6))

# Verify that the array has 5 dimensions
print("Array shape:", array_5d.shape)
print("Number of dimensions:", array_5d.ndim)
print("Original 2D array:")
print(array_2d)
print("Transposed 2D array:")
print(transposed_array_2d)

import numpy as np

# Create a boolean array
boolean_array = np.array([True, False, True, False, True, False])

# Sort the boolean array
sorted_array = np.sort(boolean_array)

print("Original boolean array:", boolean_array)
print("Sorted boolean array:", sorted_array)

import numpy as np

# Define the arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([60, 70, 80, 90, 100])

# Combine the last element of array1 and the first element of array2
combined_array = np.array([array1[-1], array2[0]])

print("Combined array:", combined_array)

import numpy as np

# Define the arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([30, 50])

# Find indices
indices = np.where(np.in1d(array1, array2))[0]

print("Indices:", indices)

