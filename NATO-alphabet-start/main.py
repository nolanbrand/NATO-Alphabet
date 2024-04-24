import pandas

#TODO 1. Create a dictionary in this format:

with open('nato_phonetic_alphabet.csv') as file:
    df = pandas.read_csv(file)

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Choose your word: ").upper()

code_word_list = [nato_dict[letter] for letter in user_word]

print(code_word_list)
