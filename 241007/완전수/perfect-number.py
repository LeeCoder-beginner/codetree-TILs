start, end = map(int, input().split())
cnt = 0

for i in range(start, end+1):
    sum_val = 0
    for j in range(1, end+1):
        if i % j == 0 and i != j:
            sum_val += j
        
        if i < j:
            break
    if i == sum_val:
        cnt += 1

print(cnt)