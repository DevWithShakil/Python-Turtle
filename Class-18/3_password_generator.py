import random
import string

# Password generator function
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a password with default length (8 characters)
password = generate_password()
print("Generated Password:", password)
