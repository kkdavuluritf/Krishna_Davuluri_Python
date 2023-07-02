import random

def game():
    print("Welcome to the Guessing Game!")
    target_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Enter your guess (between 1 and 20): "))
        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        game()
    else:
        print("Thank you for playing the game!")

game()