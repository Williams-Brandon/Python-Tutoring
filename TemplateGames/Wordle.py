import random

# Word bank with five-letter words (can be expanded)
word_bank = ["apple", "grape", "peach", "berry", "mango", "lemon", "melon"]
secret_word = random.choice(word_bank)  # Choose a random word from the word bank
max_attempts = 6  # Limit the player to 6 valid guesses

print("Welcome to Wordle!")
print("Try to guess the five-letter word. You have 6 attempts.")
print(f"The available words are {word_bank}")

# Track the number of valid attempts
attempt = 1

# Game loop
while attempt <= max_attempts:
    # Get a guess from the player
    guess = input(f"Attempt {attempt}/{max_attempts}: ").lower()

    # Check if the guess is valid (must be a five-letter word in the word bank)
    if len(guess) != 5 or guess not in word_bank:
        print("Invalid guess. Please enter a valid five-letter word from the list.")
        continue  # Invalid guess does not count as an attempt

    # Provide feedback for each letter
    feedback = []
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append("🟩")  # Green for correct letter in correct position
        elif guess[i] in secret_word:
            feedback.append("🟨")  # Yellow for correct letter in wrong position
        else:
            feedback.append("⬜")  # White for incorrect letter

    # Show feedback
    print(" ".join(feedback))

    # Check if the player has guessed the word
    if guess == secret_word:
        print("Congratulations! You've guessed the word correctly!")
        break

    # Increment the attempt counter only after a valid guess
    attempt += 1

else:
    print(f"Out of attempts! The word was '{secret_word}'. Better luck next time!")
