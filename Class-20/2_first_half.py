# Function to return the first half of an even-length string
def get_first_half(text):
    length = len(text)
    return text[:length // 2]

# Example usage
input_string = input("Enter an even-length string: ")
result = get_first_half(input_string)
print(f"The first half is: {result}")
