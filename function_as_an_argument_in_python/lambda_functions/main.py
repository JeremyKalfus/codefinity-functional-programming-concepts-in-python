def apply_to_list(list, func):
    """Applies the given function to each element in the numbers list."""
    # this is just the map function
    return [func(x) for x in list]

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using a lambda function to add 10 to each number
result_add = apply_to_list(numbers, lambda x: x + 10)
print("Adding 10:", result_add)

# Using a lambda function to multiply each number by 2
result_multiply = apply_to_list(numbers, lambda x: x * 2)
print("Multiplying by 2:", result_multiply)
