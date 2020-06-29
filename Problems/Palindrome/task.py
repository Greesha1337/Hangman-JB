word = input()
if word[:len(word) // 2] == word[len(word) // 2:][::-1]:
    print('Palindrome')
else:
    print('Not palindrome')