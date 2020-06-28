string = input()
for letter in string:
    if letter.isupper():
        new_letter = '_' + letter
        print(string.replace(letter, new_letter).lower())
        break
else:
    print(string)
