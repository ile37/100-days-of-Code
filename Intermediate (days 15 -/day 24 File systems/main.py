#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()


with open("./Input/Letters/starting_letter.txt") as start_letter:
    letter_template = start_letter.read()


for name in name_list:
    name = name.strip("\n")
    letter_content = letter_template.replace("[name]", name)    

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
        completed_letter.write(letter_content)


