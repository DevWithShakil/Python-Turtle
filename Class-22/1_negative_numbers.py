# Find negative numbers in a box
def find_negative_numbers(box):
    negative_numbers = [num for num in box if num < 0]
    return negative_numbers

# Example usage
numbers_in_box = [-10, 80, -56, 10, -20, 7, -13]
negative_numbers = find_negative_numbers(numbers_in_box)
print("Negative numbers in the box:", negative_numbers)
