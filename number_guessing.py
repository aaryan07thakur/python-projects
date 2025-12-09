import random

def get_hint(number,guess):
    diff=abs(number - guess)
    if diff== 0:
        return "perfect"
    elif diff<=5:
        return "Very Near"
    
    elif diff <=10:
        return "Still Little far"
    else:
        return "To Far"
    

def play_game():
    print("\n WELCOME TO NUMBER GUESSING GAME !")
    print("Choose Difficulty Level: ")
    print("1. Easy ( from 1 - 50 numbers only )")
    print("2. Medium (from 1 - 100 numbers only )")
    print("3. Hard (From 1 to 500 numbers only )")
    print("4. Impossible (From 1 to 1000 numbers only )\n")


    #Difficulty selection
    while True:
        try:
            choice=int(input("Enter difficulty Level from (1 - 4): "))
            if choice ==1:
                max_range=50
            elif choice==2:
                max_range=100
            elif choice==3:
                max_range=500
            elif choice==4:
                max_range=1000
            else:
                print("Please choose a valid Difficulty Level.")
                continue
            break
        except ValueError:
            print("Enter a valid numbers from (1 - 4) only")
    

    number=random.randint(1, max_range)
    attempts=0
    print(f"\n I have selected a number between 1 and {max_range}. ")
    print("Try to guess it! \n ")

    while True:
        try:
            guess=int(input("Guess Your Number: "))
            attempts +=1

            if guess < 1:
                print("Your Guessed Numer should be greater than 0. Try again. \n")
                continue

            #Hints based on closeness
            hint=get_hint(number,guess)

            if guess < number:
                print (f"Your number is Too Low! ({hint})\n")

            elif guess > number:
                print(f"Your number is Too High! ({hint})\n")
            else:
                print(f"\n Congratulations! You guessed the correct number in {attempts} attempts. ")
                break

        except ValueError:
            print("Please enter a valid integer. \n")
    
    return attempts


# Main Game loop(Plain again features and high score)

def main():
    best_score=None

    while True:
        attempts=play_game()

        #update best score
        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"New High Score: {best_score} attempts! ")

        #play again 
        again=input("\n Do you want to Play again? (y/n): ").lower()
        if again != 'y':
            print("\n Thanks For Playing! Goodbye. \n")
            break



main()













