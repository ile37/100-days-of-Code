import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

printouts = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if player_choice >= 3 or player_choice < 0:
    print("Invalid input")
else:
    print("Your choice was")
    print(printouts[player_choice])
    print("Computer's choice was")
    print(printouts[computer_choice])

    if player_choice == computer_choice:
        print("It was a draw")
    elif player_choice == 0 and computer_choice == 2:
        print("You won")
    elif player_choice == 1 and computer_choice == 0:
        print("You won")
    elif player_choice == 2 and computer_choice == 1:
        print("You won")
    else:
        print("You lost")


