  # Get user input for the number
number = int(input("Enter a number for the multiplication table (1 to 8): "))

# Generate and print the multiplication table
print(f"Multiplication Table for {number}:")
for i in range(1, 8):
    result = number * i
    print(f"{number} x {i} = {result}")
