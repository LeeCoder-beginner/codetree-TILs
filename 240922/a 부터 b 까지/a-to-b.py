a, b = map(int, input().split())
print(a, end=" ")

for _ in range(a, b+1):
    if a % 2 == 1:
        a *= 2
        if a > b:
            break
        else:
            print(a, end=" ")
    elif a % 2 == 0:
        a += 3
        if a > b:
            break
        else:
            print(a, end=" ")