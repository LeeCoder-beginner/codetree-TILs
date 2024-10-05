a, b = map(int, input().split())
cnt = 1

for i in range(9):
    for j in range(b, a-1, -1):
        if j % 2 == 0:
            print(f"{j} * {cnt} = {j*cnt}", end=" ")
            if j <= b and j > a:
                print("/", end=" ")
    cnt += 1
    print()