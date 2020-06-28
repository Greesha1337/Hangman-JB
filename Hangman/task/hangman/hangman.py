import random
words = ['python', 'java', 'kotlin', 'javascript']
answer = words[random.randint(0, len(words) - 1)]
print("H A N G M A N", sep='\n')
user_answer = input(f'Guess the word {answer[:3] + "-" * len(answer[3:])}: > ')
if user_answer == answer:
    print("You survived!")
else:
    print("You are hanged!")
