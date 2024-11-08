import random
words = ["death","phone","woman","books","plane","plain","plans","plows","rings","paper","guess"]



wordle_word = random.choice(words)
turns = 0
while turns <= 6:
    turns += 1
    response = ""
    guess = input("Guess a word!1!11!11!!!!!").lower()
    letternumber = 0
    for letter in guess:
        if letter == wordle_word[letternumber]:
            response+="🟩"
        elif letter in wordle_word:
            response+="🟨"
        else:
            response+="⬜️"
    letternumber += 1
    if guess!=wordle_word:
        print(response)
    else:
        print(f"U1 n {turns}")