n = int(input())
cnt = 1

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=" ")
        elif cnt == 9:
            print(cnt, end=" ")
            cnt //= 9
        else:
            print(cnt, end=" ")
            cnt += 1
    print()