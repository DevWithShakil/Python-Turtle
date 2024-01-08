# Vowel checker
def check_vowel(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")

# Example usage
character = input("Enter a character: ")
check_vowel(character)
