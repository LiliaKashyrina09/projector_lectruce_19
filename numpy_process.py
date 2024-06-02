import numpy as np

# Task 1a: Create arrays
# a. Array of all zeros
zeros_array = np.zeros((4, 3))
print("Array of zeros:", zeros_array)
print(zeros_array)

# b. Array of all ones
ones_array = np.ones((4, 3))
print("\nArray of ones:")
print(ones_array)

# c. Array of numbers from 0 to 11
numbers_array = np.arange(12).reshape((4, 3))
print("\nArray of numbers from 0 to 11:")
print(numbers_array)

# Task 1b: Tabulate the function F(x) = 2x^2 + 5 for x ∈ [1, 100]
x_values = np.arange(1, 101)
f_x_values = 2 * x_values**2 + 5
tabulation_1b = np.column_stack((x_values, f_x_values))
print("\nTabulation of F(x) = 2x^2 + 5:")
print(tabulation_1b)


# Task 1c: Tabulate the function F(x) = e^−x for x ∈ [−10, 10]
x_values_2 = np.arange(-10, 11)
f_x_values_2 = np.exp(-x_values_2)
tabulation_1c = np.column_stack((x_values_2, f_x_values_2))
print("\nTabulation of F(x) = e^−x:")
print(tabulation_1c)
