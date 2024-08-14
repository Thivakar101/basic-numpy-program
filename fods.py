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
transposed_array_2d = array_2d.T
print("Original 2D array:")
print(array_2d)
print("Transposed 2D array:")
print(transposed_array_2d)

