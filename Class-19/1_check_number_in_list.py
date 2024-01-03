# Function to check if a number is in an ordered list
def is_number_in_list(ordered_list, number):
    return number in ordered_list

# Example usage
ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_to_check = int(input("Enter a number to check: "))

result = is_number_in_list(ordered_list, number_to_check)
print(f"The number {number_to_check} is in the list: {result}")
