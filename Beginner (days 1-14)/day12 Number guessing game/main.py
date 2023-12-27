import random
from art import logo

TRIES_EASY = 10
TRIES_HARD = 5

def number_game():
    print(logo)
    print("Welcome to the number Guessing game")
    print("I'm thinking of a number between 1 and 100")
    
    number = random.randint(1, 100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        tries = TRIES_EASY
    elif difficulty == "hard":      
        tries = TRIES_HARD
    else:
        print("incorrect input")
        return

    stop_game = False
    while not stop_game:
        
        print(f"You have {tries} attemps remaining to guess the number.")

        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"you got it. The answer was {number}")
            stop_game = True
        elif guess > number:
            print("Too high")
        else:
            print("Too low")

        tries -= 1

        if tries == 0:
            print(f"You run out of guesses. The number was {number}. Game over")
            stop_game = True



while input("wanna play a number game? Type 'y' to play ") == "y":
    number_game()