import random

#word ko list
words=["python","car","game","Django"]

#pick random word
word=random.choice(words)
hidden=["_"] *len(word)

#chance (kati chance dine)

lives=7
print("======================= WELCOME TO HANGMAN GAME ==================================================")
print("word: "," ".join(hidden))

while lives>0:
    guess=input("Enter a letter of word: ").lower()

    #if already guessed
    if guess in hidden:
        print("you already guessed this letter! ")
        continue

    #correct guess vayo vane
    if guess in word:
        for i in range(len(word)):
            if word[i]== guess:
                hidden[i] = guess
        print("you have guess the correct letters of word")
    
    else:
        lives-=1
        print("sorry you cannot guess the correct word. Try again!  lives left : ", lives)

    print("Word: ", " ".join(hidden))

    #check win
    if "_" not in hidden:
        print("congratulation You win the game! ")
        print("The word was: ", word)
        break

if lives == 0:
    print("The GAME IS OVER! ")
    print("The word was: ", word)











































