print("Welcome to the tip calculator.\n")

bill = float(input("What was the total bill? $"))

percentage = int(input("What percentage tip vould you like to give? 10, 12 or 15? "))

num_people = int(input("How many people to split the bill? "))

pay = (bill * (1 + percentage/100))/num_people

print(f'each person should pay: ${pay:.1f}')
