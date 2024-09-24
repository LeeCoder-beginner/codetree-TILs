n = int(input())
sum_val = 0
cnt = 0
for i in range(1, 101):
    if sum_val >= n:
        break
    sum_val += i
    cnt += 1

print(cnt)