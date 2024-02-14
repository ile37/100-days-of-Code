import art
from game_data import data
import random
import os





def higher_lower_game():

    print(art.logo)
    print("Welcome to Higher and lower")

    score = 0

    while True:

        first_person = data[random.randint(0, len(data) - 1)]
        second_person = data[random.randint(0, len(data) - 1)]
        while first_person == second_person:
            second_person = data[random.randint(0, len(data) - 1)]
        
        print(f"{first_person['name']} is a {first_person['description']} from {first_person['country']} and has {first_person['follower_count']}M followers")

        print(art.vs)

        guess = input(f"{second_person['name']} is a {second_person['description']} from {second_person['country']} and  has Higher (type H) or lower (type L) followers? " )
        guess = guess.upper()

        if (guess == "H" and second_person["follower_count"] > first_person["follower_count"]) or (guess == "L" and second_person["follower_count"] < first_person["follower_count"]):
            score += 1
            print(f"Correct {second_person['name']} has {second_person['follower_count']}M followers")
        else:
            print(f"{second_person['name']} has {second_person['follower_count']}M followers")
            print(f"You lost, yor score was {score}")            
            break

while input("To play press 'y' ") == "y":
    os.system('cls')
    higher_lower_game()