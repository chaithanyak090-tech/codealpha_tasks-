#Hangama Game

import random

# Step 1: List of predefined words
words = ["Apple", "Lion", "Python", "Tiger", "Monkey"]

# Step 2: Select a random word
word = random.choice(words)

# Step 3: Initialize game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6


print("       WELCOME TO HANGMAN         ")

print("Guess the hidden word!")
print("You have 6 incorrect guesses allowed.\n")

# Step 4: Main game loop
while incorrect_guesses < max_attempts:

    # Display the word with hidden letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the word
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

    # Step 5: Take input from the player
    guess = input("\nGuess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter. Try another!")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Step 6: Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        remaining = max_attempts - incorrect_guesses

        print("Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses)
        print("Remaining attempts:", remaining)

# Step 7: Check game result
else:
    print("\nYou lost! Better luck next time.")
    print("The correct word was:", word)

print("\n          GAME OVER          ")
