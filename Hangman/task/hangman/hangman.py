import random
words = ['python', 'java', 'kotlin', 'javascript']
answer = words[random.randint(0, len(words) - 1)]
print("H A N G M A N", sep='\n')
user_answer = input("Guess the word: > ")
if user_answer == answer:
    print("You survived!")
else:
    print("You are hanged!")
