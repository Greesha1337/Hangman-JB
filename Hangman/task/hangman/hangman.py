import random
words = ['python', 'java', 'kotlin', 'javascript']
try_count = 1
answer = words[random.randint(0, len(words) - 1)]
print("HANGMAN", sep='\n')

# user_answer = input(f'Guess the word {answer[:3] + "-" * len(answer[3:])}: > ')
# if user_answer == answer:
#     print("You survived!")
# else:
#     print("You are hanged!")
right_answer = list('-' * len(answer))

while try_count <= 8:
    print('\n', *right_answer, sep='')
    user_answer = input('Input a letter: ')
    if user_answer in answer:
        for letter in range(len(answer)):
            if answer[letter] == user_answer:
                right_answer[letter] = user_answer
            else:
                continue
    else:
        print('No such letter in the word\n')
    try_count += 1



print('''\nThanks for playing!
We\'ll see how well you did in the next stage''')



