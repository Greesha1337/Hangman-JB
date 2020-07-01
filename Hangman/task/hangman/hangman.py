import random

words = ['python', 'java', 'kotlin', 'javascript']
try_count = 1
answer = words[random.randint(0, len(words) - 1)]
already_exists_letters = []
print("HANGMAN", sep='\n')

# user_answer = input(f'Guess the word {answer[:3] + "-" * len(answer[3:])}: > ')
# if user_answer == answer:
#     print("You survived!")
# else:
#     print("You are hanged!")

right_answer = list('-' * len(answer))

while try_count <= 8:
    while True:
        print('\n', *right_answer, sep='')
        user_answer = input('Input a letter: ')
        if len(user_answer) != 1:
            print('You should input a single letter')
        elif user_answer.islower() and user_answer.isascii():
            break
        else:
            print('It is not an ASCII lowercase letter')

    # if user_answer in right_answer:
    #     try_count += 1
    #     print('No improvements')
    if user_answer in already_exists_letters or user_answer in right_answer:
        print('You already typed this letter')
    elif user_answer in answer:
        for letter in range(len(answer)):
            if answer[letter] == user_answer:
                right_answer[letter] = user_answer
    else:
        already_exists_letters.append(user_answer)
        try_count += 1
        print('No such letter in the word')

    if ''.join(right_answer) == answer:
        print(''.join(right_answer), '''\nYou guessed the word!
You survived!''')
        break
    else:
        continue

if try_count > 8:
    print('You are hanged!')


# print('''\nThanks for playing!
# We\'ll see how well you did in the next stage''')



