# Checking if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

my_string = "radar"
if is_palindrome(my_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
