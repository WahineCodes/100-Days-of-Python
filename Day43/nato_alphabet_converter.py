import pandas

nato_alphabet  = pandas.read_csv("Day43/nato_phonetic_alphabet.csv")

#Creates a dictionary based on the nato_phonetic_alphabet.csv
nato_dict = {row.letter:row.code for (index,row) in nato_alphabet.iterrows()}

#Ask user for a word
word = str(input("Please type a word:\n")).upper()

#Separates the word into letters and matches to Nato Code
letters = [nato_dict[letter] for letter in word]
print(letters)



