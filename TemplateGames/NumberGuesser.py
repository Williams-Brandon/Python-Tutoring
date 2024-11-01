import random

print("Welcome to the number guessing game!")
print("I am guessing of a number between 1 and 100")

secret_number = random.randint(1,100)

guess = None
attempts = 0

while guess != secret_number:
    guess = int(input("Guess a number: "))
    attempts += 1
    
    if guess > secret_number:
        print("Your number is too high!")
    elif guess < secret_number:
        print("Your number is too low")
    else:
        print(f"Congratulations! Your guessed the number in {attempts} attempts!")
