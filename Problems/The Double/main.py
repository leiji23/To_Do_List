from string import ascii_lowercase

keys = list(ascii_lowercase)
double_alphabet = dict.fromkeys(keys)
for letter in ascii_lowercase:
    double_alphabet[letter] = letter*2
