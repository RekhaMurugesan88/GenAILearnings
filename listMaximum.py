def find_largest(numbers):
    if not numbers:
        return "List is empty."

    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

# Example usage:
num_list = [23, 89, 12, 99, 45, 67]
result = find_largest(num_list)
print("Largest number in the list:", result)
