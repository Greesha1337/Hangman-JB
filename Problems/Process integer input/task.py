user_list = []
while True:
    user_input = int(input())
    if 10 <= user_input <= 100:
        user_list.append(user_input)
    elif user_input > 100:
        break

for i in range(len(user_list)):
    print(user_list[i])