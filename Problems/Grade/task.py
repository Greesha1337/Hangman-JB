grade = int(input())
max = int(input())
if 0.9 * max <= grade <= max:
    print("A")
elif 0.8 * max <= grade < 0.9 * max:
    print("B")
elif 0.7 * max <= grade < 0.8 * max:
    print("C")
elif 0.6 * max <= grade < 0.7 * max:
    print("D")
else:
    print("F")