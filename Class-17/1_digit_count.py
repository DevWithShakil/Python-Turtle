# Finding how many digits are present in a string
my_string = "Hello123World456"
digit_count = sum(char.isdigit() for char in my_string)
print(f"There are {digit_count} digits in the string.")
