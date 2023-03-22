import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Ask the user to guess the number
guess = int(input("Guess a number between 1 and 10: "))

# Keep track of the number of guesses
num_guesses = 1

# Set initial score to 100
score = 100

# Loop until the user guesses correctly or uses all their guesses
while guess != number and num_guesses < 3:
    if guess < number:
        print("Too low!")
        if number % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
    else:
        print("Too high!")
        if number % 3 == 0:
            print("Hint: The number is divisible by 3.")
        else:
            print("Hint: The number is not divisible by 3.")
    
    # Ask the user to guess again
    guess = int(input("Guess again: "))
    
    # Increment the number of guesses
    num_guesses += 1
    
    # Reduce the score with each incorrect guess
    score -= 10
    
# Check if the user guessed the number
if guess == number:
    print("Congratulations! You guessed the number in", num_guesses, "guesses.")
    print("Your score is:", score)
else:
    print("Sorry, you ran out of guesses. The number was", number)
    print("Your score is:", score)
