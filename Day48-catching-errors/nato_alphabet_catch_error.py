# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("Day48-catching-errors/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


try:
    word = input("Enter a word: ").upper()
except:
    
    print("Sorry, only letters in the alphabet please")
    word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
