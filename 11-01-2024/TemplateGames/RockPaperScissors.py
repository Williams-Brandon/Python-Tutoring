import random

print("Let's play rock, paper, scissors")

choices = ['rock', 'paper', 'scissors']

player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    player_choice = input('Your choice: ').lower()
    
    if player_choice not in choices:
        print('Please enter rock, paper, or scissors')
        continue
    
    computer_choice = random.choice(choices)
    print(f"The computer chose {computer_choice}")
    
    if player_choice == computer_choice:
        print('DRAW')
    elif(player_choice == 'rock' and computer_choice == 'scissors'):
        print('You win this round')
        player_score += 1
    elif(player_choice == 'scissors' and computer_choice == 'paper'):
        print('You win this round')
        player_score += 1
    elif(player_choice == 'paper' and computer_choice == 'rock'):
        print('You win this round')
        player_score += 1
    else:
        print('Computer wins this round')
        computer_score += 1
    
    print(f"Score: You - {player_score}, Computer - {computer_score}\n")
print("GAME COMPLETE!")    
if player_score > computer_score:
    print('You won!')
elif player_score < computer_score:
    print('You lose!')
else:
    print('You tied!')
        
    
    