# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#Objective: Update the Nato Alphabet Alphabet converter to catch errors if uses input anything but a letter. 

import pandas

data = pandas.read_csv("Day48-catching-errors/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
