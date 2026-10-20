a = int(input())
b = int(input())

for i in range(a, b + 1):
    s = str(i)

    for digit in "0123456789":
        if s.count(digit) == 3:
            print(i)
            break
