import random

name=input("What is your name? \n")
print(("Good Luck! ", name))

words=['rainbow', 'computer','cience','programming','python','mathematics','player','condition',
       'reverse','water','board','geeks']

words=random.choice(words)

print("Guess the characters of word: ")

guesses=''
turns=12

while turns >0:
    failed = 0
    for char in words:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed +=1

    if failed ==0:
        print("congratulation You win the game")
        print("The word is: ", words)

        break
    print()
    guess= input("guess a character: ").lower()
    guesses +=guess

    if guess not in words:
        turns -=1
        print(" It is wrong")
        print("you have ", +turns, "guesses more")

        if turns ==0:
            print("sorry You Loose the Game!")




















