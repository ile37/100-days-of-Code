#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():

    nr_letters = random.randint(8,12)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password = []

    for i in range(nr_letters):
        password.append(random.choice(letters)) 

    for i in range(nr_symbols):
        password.append(random.choice(symbols))

    for i in range(nr_numbers):
        password.append(random.choice(numbers))
        
    random.shuffle(password)
    password = "".join(password)

    return password