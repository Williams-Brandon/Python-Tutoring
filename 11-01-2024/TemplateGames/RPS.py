import random
options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
while player_score < 2 and computer_score < 2:
    computer_choice = random.choice(options)
    player_choice = input("Choose your move ")
    if player_choice not in options:
        print("Invalid Input!")
        continue
    if computer_choice == player_choice:
        print("Draw")
    elif player_choice == "rock" and computer_choice == "scissors":
        player_score += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        player_score += 1
    elif player_choice == "paper" and computer_choice == "rock":
        player_score += 1
    else:
        computer_score += 1
    print(f"Computer chose {computer_choice}! Current score is {player_score}:{computer_score}!")
if(player_score==2):
    print("You WIN!")
if(computer_score==2):
    print("You have not win! You... DIED!")