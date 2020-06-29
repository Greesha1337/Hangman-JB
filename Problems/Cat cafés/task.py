a = []
b = []

while True:
    cafe = input()
    if cafe == "MEOW":
        break
    else:
        a.append(cafe.split(' ')[0])
        b.append(int(cafe.split(' ')[1]))

print(a[b.index(max(b))])