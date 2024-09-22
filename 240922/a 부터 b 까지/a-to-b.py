a, b = map(int, input().split())

for _ in range(a, b+1):
    if a >= b:
        print(a, end=" ")
        break
    elif a % 2 == 1:
        print(a, end=" ")
        a *= 2
    elif a % 2 == 0:
        print(a, end=" ")
        a += 3