# Function to perform FizzBuzz
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

# Example usage
number_to_check = int(input("Enter a number for FizzBuzz: "))
result = fizz_buzz(number_to_check)

# Separate cases for Fizz, Buzz, and FizzBuzz
if result == "FizzBuzz":
    print("Fizz and Buzz")
elif result == "Fizz":
    print("Fizz")
elif result == "Buzz":
    print("Buzz")
else:
    print(result)
