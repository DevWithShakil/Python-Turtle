import random

# Generate a random number between 1 and 5
secret_number = random.randint(1, 5)

# Allow the player 3 guesses
for _ in range(3):
    guess = int(input("Guess the number (between 1 and 5): "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")

print(f"The correct number was {secret_number}.")
