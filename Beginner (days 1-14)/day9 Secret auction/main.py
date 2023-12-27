import os
import art

print(art.logo)
print("Welcome to the secret auction program.")

bidders = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    
    bidders[name] = bid

    cmd = input("Are there any other bidders? Type 'yes' or press anything to see who won.\n")

    if cmd != "yes":
        break   

    os.system("cls")


winner_bid = 0
winner_name = ""

for key in bidders:
    if bidders[key] > winner_bid:
        winner_bid = bidders[key]
        winner_name = key

print(f"Winner of the auction is {winner_name} with a bid of {winner_bid}€")
