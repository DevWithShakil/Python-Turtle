# Using and operator to check if a number is both even and greater than 5
for number in range(1, 11):
    if number % 2 == 0 and number > 5:
        print(number, "is both even and greater than 5.")
    else:
        print(number, "does not satisfy both conditions.")

# Using or operator to check if a number is either odd or less than 4
for number in range(1, 11):
    if number % 2 != 0 or number < 4:
        print(number, "is either odd or less than 4.")
    else:
        print(number, "does not satisfy either condition.")
