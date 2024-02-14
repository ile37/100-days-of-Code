import random
import hangman_words
import hangman_pictures

print(hangman_pictures.logo)

chosen_word = random.choice(hangman_words.word_list)

display_word = ["_"] * len(chosen_word)

num_tries = 6
has_won = False

while not has_won:

    gess = input("Gess a letter: ").lower()

    for i, letter in enumerate(chosen_word):
        if letter == gess:
            display_word[i] = letter
    
    if gess not in chosen_word:
        num_tries -= 1
        if num_tries == 0:
            break

    if "_" not in display_word:
        has_won = True

    print(' '.join(display_word))
    print(hangman_pictures.stages[num_tries])

print(hangman_pictures.stages[num_tries])

if has_won:
    print("you won")
else:
    print("You lost")