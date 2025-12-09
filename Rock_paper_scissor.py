import random

choices=["rock","paper", "scissors"]
user_score = 0
Computer_score = 0 

print("============= ROCK - PAPER - SCISSORS GAME========================================")


while True:
    print("\n Your Score: ", user_score, "|  Computer score: ", Computer_score)
    user_choice = input("choose (rock/Paper/ scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Try again. ")
        continue

#computer choices from choices
    computer_choice=random.choice(choices)

    print(f"Your choice: {user_choice}")
    print(f"Computer Choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie! ")

    elif (user_choice=="rock" and computer_choice =="scissors") or \
         (user_choice=="paper" and computer_choice =="rock") or \
         (user_choice=="scissors" and computer_choice =="paper"):
        print("Congratulation You win this round!")

        user_score +=1
    else:
        print("Computer wins this round! ")

        Computer_score +=1
    
    play_again=input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("\n final Scores:  ")
        print("Your Score: ", user_score)
        print("Computer score: ", Computer_score)

        print("Thanks For Playing! Gud Bye")

        break















