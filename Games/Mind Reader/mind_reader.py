import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Ask the user to guess the number
guess = int(input("Guess a number between 1 and 10: "))

# Keep track of the number of guesses
num_guesses = 1

# Loop until the user guesses correctly or uses all their guesses
while guess != number and num_guesses < 3:
    if guess < number:
        print("Too low!")
    else:
        print("Too high!")
    
    # Ask the user to guess again
    guess = int(input("Guess again: "))
    
    # Increment the number of guesses
    num_guesses += 1
    
# Check if the user guessed the number
if guess == number:
    print("Congratulations! You guessed the number in", num_guesses, "guesses.")
else:
    print("Sorry, you ran out of guesses. The number was", number)
