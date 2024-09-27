n = int(input())
x = 1

while True:
    if 2 ** x != n:
        x += 1
    elif 2 ** x == n:
        print(x)
        break