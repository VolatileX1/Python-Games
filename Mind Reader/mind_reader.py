import random
import time

# Function to get a player's guess and keep track of their score
def get_guess(player_num):
    print("Player", player_num, "turn")
    guess = int(input("Guess a number between 1 and 10: "))
    return guess

# Function to play the game in singleplayer mode
def play_singleplayer():
    # Generate a random number between 1 and 10
    number = random.randint(1, 10)

    # Set the time limit to 10 seconds
    time_limit = 10
    start_time = time.time()

    # Keep track of the number of guesses and score
    num_guesses = 1
    score = 100

    # Loop until the user guesses correctly or uses all their guesses or runs out of time
    while guess != number and num_guesses < 3 and (time.time() - start_time) < time_limit:
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

        # Increment the number of guesses and reduce the score with each incorrect guess
        num_guesses += 1
        score -= 10

    # Check if the user guessed the number or ran out of time
    if guess == number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        print("Your score is:", score)
    elif (time.time() - start_time) >= time_limit:
        print("Sorry, you ran out of time. The number was", number)
        print("Your score is:", score)
    else:
        print("Sorry, you ran out of guesses. The number was", number)
        print("Your score is:", score)


# Function to play the game in multiplayer mode
def play_multiplayer():
    # Generate a random number between 1 and 10
    number = random.randint(1, 10)

    # Set the time limit to 10 seconds
    time_limit = 10
    start_time = time.time()

    # Keep track of each player's turn and score
    num_players = 2
    player_turn = 1
    player_scores = {1: 0, 2: 0}

    # Loop until a player guesses the correct number or runs out of time
    while True:
        # Get the current player's guess
        guess = get_guess(player_turn)

        # Check if the guess is correct or if time has run out
        if guess == number:
            print("Congratulations! Player", player_turn, "guessed the number in", player_scores[player_turn]+1, "guesses.")
            break
        elif (time.time() - start_time) >= time_limit:
            print("Sorry, time's up! The number was", number)
            break

        # Provide a hint based on the guess
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

        # Switch to the next player's turn and record their score
        player_scores[player_turn] += 1
        player_turn = 2 if player_turn == 1 else 1

    # Display each player's score at the end of the game
    for player, score in player_scores.items():
        print("Player", player, "score:", score*10)

# Ask the user to choose between singleplayer or multiplayer mode
mode_choice = input("Choose game mode (singleplayer/multiplayer): ")

# Play the game in the chosen mode
if mode_choice.lower() == "singleplayer":
    play_singleplayer()
elif mode_choice.lower() == "multiplayer":
    play_multiplayer()
else:
    print("Invalid choice. Please try again.")
