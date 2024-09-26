cnt = 0

while True:
    n = int(input())
    if n % 2 == 1:
        continue
    elif n % 2 == 0:
        if cnt == 3:
            break
        else:
            print(n // 2)
            cnt += 1