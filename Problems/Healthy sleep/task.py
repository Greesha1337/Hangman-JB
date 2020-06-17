A = int(input())
B = int(input())
H = int(input())

if A <= B:
    if A <= H <= B:
        print("Normal")
    elif H < A:
        print("Deficiency")
    else:
        print("Excess")
else:
    print("Wrong input")