n = input("Введіть число n: ")
d = input("Введіть цифру d: ")

position = 0

for i in range(len(n) - 1, -1, -1):
    position += 1
    if n[i] == d:
        print(position)
        break
else:
    print(0)
