import random
number = random.randint(1,10)
guessed_sucessfully = False
attempts = 0
while not guessed_sucessfully:
    attempts += 1
    guess = int(input("Enter number: "))
    if guess > 100 or guess < 1 or int(guess)!=guess:
        print("Invalid input!")
    elif guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print(f"Correct in {attempts} attempts")
        guessed_sucessfully = True