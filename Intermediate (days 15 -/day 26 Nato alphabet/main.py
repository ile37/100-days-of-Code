import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter a word: ")

name_chars = [data_dict[char.capitalize()] for char in name]

print("Your word in NATO alphabet is:")
print(name_chars)