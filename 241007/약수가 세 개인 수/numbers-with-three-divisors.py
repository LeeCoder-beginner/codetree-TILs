start, end = map(int, input().split())
meo = 0
for i in range(start, end+1):
    cnt = 0
    for j in range(1, i):
        if i % j == 0:
            cnt += 1
    if cnt == 3:
        meo += 1
print(meo)