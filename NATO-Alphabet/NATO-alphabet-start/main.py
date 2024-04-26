import pandas

with open('nato_phonetic_alphabet.csv') as file:
    df = pandas.read_csv(file)

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    user_word = input("Choose your word: ").upper()
    try:
        code_word_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code_word_list)


generate_phonetic()