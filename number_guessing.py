import random
import sys

def get_hint(number, guess):
    diff = abs(number - guess)
    if diff == 0:
        return "🎯 Perfect!"
    elif diff <= 5:
        return "🔥 Very Hot!"
    elif diff <= 10:
        return "🌡️ Warm"
    else:
        return "❄️ Cold"

def play_game():
    print("\n🎮 Welcome to the Advanced Number Guessing Game!")
    print("Choose difficulty level:")
    print("1. Easy (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 500)")
    print("4. Impossible (1 - 1000)\n")

    # Difficulty selection
    while True:
        try:
            choice = int(input("Enter difficulty (1-4): "))
            if choice == 1:
                max_range = 50
            elif choice == 2:
                max_range = 100
            elif choice == 3:
                max_range = 500
            elif choice == 4:
                max_range = 1000
            else:
                print("❌ Please choose a valid difficulty.")
                continue
            break
        except ValueError:
            print("❌ Enter a valid number (1-4).")

    number = random.randint(1, max_range)
    attempts = 0
    best_score = sys.maxsize

    print(f"\n🤖 I have selected a number between 1 and {max_range}.")
    print("Try to guess it!\n")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < 1:
                print("⚠️ Guess must be greater than 0. Try again.\n")
                continue

            # Hints based on closeness
            hint = get_hint(number, guess)

            if guess < number:
                print(f"⬇️ Too Low! ({hint})\n")
            elif guess > number:
                print(f"⬆️ Too High! ({hint})\n")
            else:
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Please enter a valid integer.\n")

    return attempts


# Main Game Loop (play again feature + high score)
def main():
    best_score = None

    while True:
        attempts = play_game()

        # Update best score
        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"🏆 New High Score: {best_score} attempts!")

        # Play again?
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Thanks for playing! Goodbye.\n")
            break


main()

