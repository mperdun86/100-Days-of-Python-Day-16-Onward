import pandas
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
np_df = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in np_df.iterrows()}
print(phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Please enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)